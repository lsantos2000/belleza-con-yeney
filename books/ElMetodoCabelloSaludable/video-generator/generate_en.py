from pathlib import Path
import argparse, asyncio, hashlib, json, os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageOps
import imageio_ffmpeg
import edge_tts

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
AUTHOR = ROOT / 'resources/images/author/video-source'
PAGES = ROOT / 'resources/images/books/ElMetodoCabelloSaludable/en/demo-pages'
VIDEO = ROOT / 'resources/videos/ElMetodoCabelloSaludable'
AUDIO_DIR = ROOT / 'resources/audio/ElMetodoCabelloSaludable'
STORYBOARD_IMAGE = ROOT / 'resources/images/books/ElMetodoCabelloSaludable/en/storyboard.jpg'
WORK = HERE / 'build-en'
FF = imageio_ffmpeg.get_ffmpeg_exe()
COLOR = '#7C293D'; CREAM = '#FFF7ED'; GOLD = '#D7AE68'; GREEN = '#176F5B'
SCALE = 1.5
WIDTH, HEIGHT = 1920, 1080
OUT = VIDEO / 'the-healthy-hair-method-promo-3-minutes.mp4'
AMAZON = 'https://www.amazon.com/dp/B0HJ55BM9L'
GOOGLE = 'https://play.google.com/store/books/details?id=Gm8KEgAAQBAJ'
WEBSITE = 'belleza-con-yeney.pages.dev'

def scaled(value):
    return round(value * SCALE)

def point(values):
    return tuple(scaled(value) for value in values)

def run(args):
    subprocess.run([FF, '-hide_banner', '-loglevel', 'error', '-y', *map(str, args)], check=True)

def font(size, bold=False):
    choices = [os.environ.get('PROMO_FONT_BOLD' if bold else 'PROMO_FONT'),
               'C:/Windows/Fonts/' + ('arialbd.ttf' if bold else 'arial.ttf'),
               '/usr/share/fonts/truetype/dejavu/DejaVuSans' + ('-Bold.ttf' if bold else '.ttf')]
    for candidate in choices:
        if candidate and Path(candidate).exists():
            return ImageFont.truetype(candidate, scaled(size))
    raise FileNotFoundError('Set PROMO_FONT and PROMO_FONT_BOLD to TTF paths')

def page_path(page):
    return PAGES / f'The_Healthy_Hair_Method_page_{page:03}_en.jpg'

def contain(canvas, path, box):
    x, y, w, h = point(box)
    image = ImageOps.contain(ImageOps.exif_transpose(Image.open(path)).convert('RGB'), (w, h), Image.Resampling.LANCZOS)
    canvas.paste(image, (x + (w-image.width)//2, y + (h-image.height)//2))

def base_frame(title):
    image = Image.new('RGB', (WIDTH, HEIGHT), COLOR)
    draw = ImageDraw.Draw(image)
    draw.text(point((34, 20)), title, font=font(34, True), fill=CREAM)
    draw.line(point((34, 73, 1246, 73)), fill=GOLD, width=scaled(2))
    draw.text(point((34, 681)), 'THE HEALTHY HAIR METHOD', font=font(17, True), fill=CREAM)
    draw.text(point((1238, 681)), WEBSITE, anchor='ra', font=font(15), fill='#F6D8D1')
    return image, draw

def frame(section, scene, number):
    image, draw = base_frame(section['title'])
    if scene['kind'] == 'pair':
        author_right = scene['side'] == 'right'
        x, y, w, h = (529 if author_right else 16, 88, 735, 565)
        draw.rounded_rectangle(point((x, y, x+w, y+h)), radius=scaled(18), fill='#88364A', outline='#A76776', width=scaled(1))
        contain(image, AUTHOR / scene['photo'], (x+13, y+9, w-26, h-18))
        contain(image, page_path(scene['page']), (16 if author_right else 770, 88, 494, 565))
    elif scene['kind'] == 'book':
        draw.rounded_rectangle(point((108, 88, 1172, 653)), radius=scaled(20), fill=CREAM, outline=GOLD, width=scaled(3))
        contain(image, page_path(scene['page']), (126, 101, 1028, 539))
    else:
        contain(image, AUTHOR / scene['photo'], (20, 90, 440, 560))
        draw.rounded_rectangle(point((485, 102, 1240, 646)), radius=scaled(34), fill=CREAM, outline=GOLD, width=scaled(3))
        items = [
            ((525, 130), 'Purchase information', 36, True, COLOR),
            ((525, 185), 'The Healthy Hair Method', 30, True, '#111111'),
            ((525, 250), 'Amazon · Printed book and Kindle', 27, True, COLOR),
            ((525, 290), AMAZON, 21, False, '#333333'),
            ((525, 355), 'Google Play Books · PDF/ePub', 27, True, GREEN),
            ((525, 395), GOOGLE, 20, False, '#333333'),
            ((525, 480), 'Download the free sample at', 25, True, COLOR),
            ((525, 516), 'belleza-con-yeney.pages.dev/en/demo-libro', 21, False, '#333333'),
            ((525, 574), 'Get your copy TODAY.', 34, True, COLOR),
        ]
        for xy, text, size, bold, color in items:
            draw.text(point(xy), text, font=font(size, bold), fill=color)
        cover = ImageOps.contain(Image.open(page_path(scene['page'])).convert('RGB'), point((150, 195)), Image.Resampling.LANCZOS)
        image.paste(cover, point((1050, 435)))
    path = WORK / f'frame-{number:02}.png'
    image.save(path)
    return path

def validate(sections):
    scenes = [scene for section in sections for scene in section['scenes']]
    photos = [AUTHOR / scene['photo'] for scene in scenes if 'photo' in scene]
    pages = [scene['page'] for scene in scenes]
    assert len(photos) == len(set(photos)), 'Repeated author photo path'
    assert len(pages) == len(set(pages)), 'Repeated book page'
    assert all(path.exists() for path in photos), 'Missing author photograph'
    assert all(page_path(page).exists() for page in pages), 'Missing English book page'
    hashes = [hashlib.sha256(path.read_bytes()).hexdigest() for path in photos]
    assert len(hashes) == len(set(hashes)), 'Duplicate author image content'
    sides = [scene['side'] for scene in scenes if scene['kind'] == 'pair']
    assert all(a != b for a, b in zip(sides, sides[1:])), 'Author sides must alternate'
    assert len(sections) == 6 and all(len(section['scenes']) == 4 for section in sections)
    return {'photos': len(photos), 'pages': len(pages), 'duration_seconds': 180,
            'resolution': f'{WIDTH}x{HEIGHT}', 'author_sides_alternate': True,
            'duplicate_photos': 0, 'duplicate_pages': 0}

def narration(sections):
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    text_path = WORK / 'narration-en.txt'
    raw_audio = WORK / 'narration-en.mp3'
    output = AUDIO_DIR / 'narration-en.m4a'
    narration_text = '\n\n'.join(section['text'] for section in sections)
    text_path.write_text(narration_text, encoding='utf-8')
    asyncio.run(edge_tts.Communicate(narration_text, 'en-US-AriaNeural', rate='+8%').save(str(raw_audio)))
    probe = subprocess.run([FF, '-i', raw_audio], capture_output=True, text=True)
    import re
    match = re.search(r'Duration: (\d+):(\d+):(\d+(?:\.\d+)?)', probe.stderr)
    duration = int(match.group(1))*3600 + int(match.group(2))*60 + float(match.group(3))
    tempo = duration / 177.5
    run(['-i', raw_audio, '-filter:a', f'atempo={tempo:.6f},apad=pad_dur=2.5', '-t', 180,
         '-c:a', 'aac', '-ar', 48000, '-b:a', '160k', output])
    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--preview', action='store_true')
    args = parser.parse_args()
    WORK.mkdir(exist_ok=True)
    sections = json.loads((HERE/'storyboard-en.json').read_text(encoding='utf-8'))
    print(validate(sections), flush=True)
    images = [frame(section, scene, number) for section in sections for scene in section['scenes']
              for number in [sum(len(item['scenes']) for item in sections[:sections.index(section)]) + section['scenes'].index(scene)]]
    sheet = Image.new('RGB', (1920, 180*((len(images)+5)//6)), COLOR)
    for index, path in enumerate(images):
        sheet.paste(Image.open(path).resize((320,180)), ((index%6)*320, (index//6)*180))
    STORYBOARD_IMAGE.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(STORYBOARD_IMAGE, quality=94)
    if args.preview:
        return
    audio = narration(sections)
    chapters=[]; index=0
    for chapter_number, section in enumerate(sections):
        shots=[]
        for _scene in section['scenes']:
            shot=WORK/f'shot-{index:02}.mp4'; shots.append(shot)
            run(['-loop','1','-framerate',24,'-i',images[index],'-frames:v',192,'-an','-c:v','libx264','-pix_fmt','yuv420p','-preset','veryfast','-crf',20,shot])
            index += 1
        inputs=[]
        for shot in shots: inputs += ['-i', shot]
        graph='[0:v][1:v]xfade=transition=fade:duration=0.5:offset=7.5[v1];[v1][2:v]xfade=transition=fade:duration=0.5:offset=15[v2];[v2][3:v]xfade=transition=fade:duration=0.5:offset=22.5[v3]'
        chapter=WORK/f'chapter-{chapter_number}.mp4'; chapters.append(chapter)
        run([*inputs,'-filter_complex_threads',1,'-filter_complex',graph,'-map','[v3]','-frames:v',720,'-an','-c:v','libx264','-pix_fmt','yuv420p','-preset','veryfast','-crf',20,chapter])
        print(f'Block {chapter_number+1}/6 completed', flush=True)
    inputs=[]; graph=[]
    for i, chapter in enumerate(chapters):
        inputs += ['-i', chapter]
        graph.append(f'[{i}:v]tpad=stop_mode=clone:stop_duration=0.5[c{i}]')
    for i in range(1, len(chapters)):
        previous='c0' if i == 1 else f'm{i-1}'
        graph.append(f'[{previous}][c{i}]xfade=transition=fade:duration=0.5:offset={i*30}[m{i}]')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    run([*inputs,'-i',audio,'-filter_complex_threads',1,'-filter_complex',';'.join(graph),'-map',f'[m{len(chapters)-1}]','-map',f'{len(chapters)}:a','-t',180,'-c:v','libx264','-preset','veryfast','-crf',20,'-pix_fmt','yuv420p','-c:a','aac','-ar',48000,'-b:a','160k','-movflags','+faststart',OUT])
    run(['-i',OUT,'-f','null','-'])
    print(f'Full decode verified: {OUT}', flush=True)

if __name__ == '__main__':
    main()
