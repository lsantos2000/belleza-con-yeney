from pathlib import Path
import argparse,hashlib,json,os,subprocess
from PIL import Image,ImageDraw,ImageFont,ImageOps
import imageio_ffmpeg
HERE=Path(__file__).resolve().parent
MEDIA=HERE.parents[1]/'public/media/video-promocional'
WORK=HERE/'build'
FF=imageio_ffmpeg.get_ffmpeg_exe()
COLOR='#7C293D';CREAM='#FFF7ED';GOLD='#D7AE68'
OUT=MEDIA/'video/el-metodo-cabello-saludable-promo-3-minutos.mp4'
def run(args):subprocess.run([FF,'-hide_banner','-loglevel','error','-y',*map(str,args)],check=True)
def font(size,bold=False):
    choices=[os.environ.get('PROMO_FONT_BOLD' if bold else 'PROMO_FONT'),'C:/Windows/Fonts/'+('arialbd.ttf' if bold else 'arial.ttf'),'/usr/share/fonts/truetype/dejavu/DejaVuSans'+('-Bold.ttf' if bold else '.ttf')]
    for p in choices:
        if p and Path(p).exists():return ImageFont.truetype(p,size)
    raise FileNotFoundError('Set PROMO_FONT and PROMO_FONT_BOLD to TTF paths')
def contain(im,path,box):
    x,y,w,h=box;p=ImageOps.contain(ImageOps.exif_transpose(Image.open(path)).convert('RGB'),(w,h),Image.Resampling.LANCZOS)
    im.paste(p,(x+(w-p.width)//2,y+(h-p.height)//2))
def frame(sec,s,n):
    im=Image.new('RGB',(1280,720),COLOR);d=ImageDraw.Draw(im)
    d.text((34,20),sec['title'],font=font(34,True),fill=CREAM);d.line((34,73,1246,73),fill=GOLD,width=2)
    d.text((34,681),'EL MÉTODO CABELLO SALUDABLE',font=font(17,True),fill=CREAM)
    d.text((938,681),'belleza-con-yeney.pages.dev',font=font(15),fill='#F6D8D1')
    if s['kind']=='cta':
        p=ImageOps.fit(Image.open(MEDIA/s['photo']).convert('RGB'),(468,565),Image.Resampling.LANCZOS,centering=(.5,.38));im.paste(p,(16,88))
        d.rounded_rectangle((510,118,1240,615),radius=34,fill=CREAM,outline=GOLD,width=3)
        for xy,text,size,bold,color in [((545,143),'Información de compra',36,True,COLOR),((545,193),'El Método Cabello Saludable',30,True,'#111111'),((545,258),'Amazon Books · Libro impreso y digital',26,True,COLOR),((545,295),'https://www.amazon.com/dp/B0HFHC2QL7',23,False,'#333333'),((545,348),'Google Play Books · Edición digital',27,True,COLOR),((545,385),'https://play.google.com/store/books/',22,False,'#333333'),((545,412),'details?id=8VgDEgAAQBAJ',22,False,'#333333'),((545,461),'YouTube Demo',27,True,COLOR),((545,499),'https://www.youtube.com/watch?v=xUI1K6fISGw',22,False,'#333333'),((545,560),'Reserva tu copia HOY MISMO.',32,True,COLOR)]:d.text(xy,text,font=font(size,bold),fill=color)
        d.line((545,240,1200,240),fill='#C98278',width=3)
    elif s['kind']=='collage':
        count=len(s['pages']); width=1208//count
        for i,page in enumerate(s['pages']):
            contain(im,MEDIA/f'paginas-libro/pagina-{page:02}.jpeg',(36+i*width,98,width-14,545))
    else:
        right=s.get('side')=='right'
        x,y,w,h=(529 if right else 16,88,735,565)
        d.rounded_rectangle((x,y,x+w,y+h),radius=18,fill='#88364A',outline='#A76776',width=1)
        if 'photo' in s:
            contain(im,MEDIA/s['photo'],(x+13,y+9,w-26,h-18))
        contain(im,MEDIA/f"paginas-libro/pagina-{s['page']:02}.jpeg",(16 if right else 770,88,494,565))
    p=WORK/f'frame-{n:02}.png';im.save(p);return p
def dhash(p):
    v=list(ImageOps.exif_transpose(Image.open(p)).convert('L').resize((9,8)).getdata())
    return sum(int(v[y*9+x]>v[y*9+x+1])<<(y*8+x) for y in range(8) for x in range(8))
def validate(sections):
    scenes=[s for sec in sections for s in sec['scenes']];paths=[MEDIA/s['photo'] for s in scenes if 'photo' in s]
    assert all(s['kind']=='cta' or 'page' in s or 'pages' in s for s in scenes)
    assert all(s['kind'] in ('pair','collage','cta') for s in scenes), 'No repeated text panels'
    assert not any(p.name in ('yeney-08.jpeg','yeney-16.jpeg') for p in paths), 'Excluded photograph'
    embedded={15:{5,7,41},17:{11,14,22,23},19:{25,27,29,31,33},21:{24,26,30,32,35}}
    for s in scenes:
        if s['kind']=='pair':
            photo=int(Path(s['photo']).stem.split('-')[-1])
            assert photo not in embedded.get(s['page'],set()), 'Photo repeated inside facing page'
    sides=[s['side'] for s in scenes if s['kind']=='pair']
    assert all(a!=b for a,b in zip(sides,sides[1:])), 'Author sides must alternate'
    assert len(paths)==len(set(paths)), 'Repeated photo path'
    hashes=[hashlib.sha256(p.read_bytes()).hexdigest() for p in paths]
    assert len(hashes)==len(set(hashes)), 'Identical files under different names'
    vh=[dhash(p) for p in paths];near=[]
    for i,h in enumerate(vh):
        for j in range(i+1,len(vh)):
            if (h^vh[j]).bit_count()<=5:near.append([i+1,j+1])
    assert not near,f'Visually similar photographs require review: {near}'
    pages=[p for s in scenes for p in s.get('pages',([s['page']] if 'page' in s else []))];assert pages==sorted(set(pages))
    report={'photos':len(paths),'pages':len(pages),'exact_duplicates':0,'perceptual_candidates':near,'collages':len(set(pages)&{17,19,21}),'duration_seconds':180,'all_scenes_include_book':True,'author_sides_alternate':True,'mirror_photo_excluded':True}
    report.update(kitchen_photo_excluded=True,text_panels=0,multi_page_scenes=sum(s['kind']=='collage' for s in scenes))
    (MEDIA/'verification.json').write_text(json.dumps(report,indent=2),encoding='utf-8');return report
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--preview',action='store_true');args=ap.parse_args()
    WORK.mkdir(exist_ok=True);sections=json.loads((HERE/'storyboard.json').read_text(encoding='utf-8'))
    print(validate(sections),flush=True);images=[]
    for sec in sections:
        for s in sec['scenes']:images.append(frame(sec,s,len(images)))
    sheet=Image.new('RGB',(1920,180*((len(images)+5)//6)),COLOR)
    for i,p in enumerate(images):sheet.paste(Image.open(p).resize((320,180)),((i%6)*320,(i//6)*180))
    sheet.save(MEDIA/'storyboard.jpg',quality=94)
    if args.preview:return
    chapters=[];n=0
    for c,sec in enumerate(sections):
        count=len(sec['scenes']);cores=[round((j+1)*720/count)-round(j*720/count) for j in range(count)];shots=[]
        for j,core in enumerate(cores):
            shot=WORK/f'shot-{n:02}.mp4';shots.append(shot)
            run(['-loop','1','-framerate',24,'-i',images[n],'-frames:v',core+(12 if j<count-1 else 0),'-an','-c:v','libx264','-pix_fmt','yuv420p','-preset','veryfast','-crf',20,shot]);n+=1
        inputs=[]
        for p in shots:inputs+=['-i',p]
        graph=[];acc=0
        for j in range(1,count):
            acc+=cores[j-1];prev='0:v' if j==1 else f'v{j-1}'
            graph.append(f'[{prev}][{j}:v]xfade=transition=fade:duration=0.5:offset={acc/24:.8f}[v{j}]')
        chapter=WORK/f'chapter-{c}.mp4';chapters.append(chapter)
        run([*inputs,'-filter_complex_threads',1,'-filter_complex',';'.join(graph),'-map',f'[v{count-1}]','-frames:v',720,'-an','-c:v','libx264','-pix_fmt','yuv420p','-preset','veryfast','-crf',20,chapter])
        print(f'Block {c+1}/6 completed',flush=True)
    OUT.parent.mkdir(exist_ok=True)
    inputs=[];graph=[]
    for i,p in enumerate(chapters):
        inputs+=['-i',p]
        graph.append(f'[{i}:v]tpad=stop_mode=clone:stop_duration=0.5[c{i}]')
    for i in range(1,len(chapters)):
        prev='c0' if i==1 else f'm{i-1}'
        graph.append(f'[{prev}][c{i}]xfade=transition=fade:duration=0.5:offset={i*30}[m{i}]')
    run([*inputs,'-i',MEDIA/'audio/narracion.m4a','-filter_complex_threads',1,'-filter_complex',';'.join(graph),'-map',f'[m{len(chapters)-1}]','-map',f'{len(chapters)}:a','-t',180,'-c:v','libx264','-preset','veryfast','-crf',20,'-pix_fmt','yuv420p','-c:a','aac','-ar',48000,'-b:a','160k','-movflags','+faststart',OUT])
    run(['-i',OUT,'-f','null','-']);print(f'Full decode verified: {OUT}',flush=True)
if __name__=='__main__':main()
