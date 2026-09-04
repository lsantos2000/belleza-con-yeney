"""Compare carousel assets without modifying source photographs."""
from pathlib import Path
from PIL import Image, ImageOps
import re
import hashlib
from itertools import combinations

root = Path(__file__).resolve().parents[1]
source = (root / 'app/author-carousel.tsx').read_text(encoding='utf-8')
order = [int(x) for x in re.search(r'const order=\[([^]]+)\]', source)[1].split(',')]
new_order = [int(x) for x in re.search(r'const newOrder=\[([^]]+)\]', source)[1].split(',')]
gallery = [root / f'resources/images/author/gallery/yeney-{n:02}.jpg' for n in order + [18,48]]
gallery += [root / f'resources/images/author/video-source/yeney-{n:02}.jpeg' for n in new_order]
def dhash(p):
    with Image.open(p) as im:
        pixels = list(ImageOps.exif_transpose(im).convert('L').resize((17,16)).get_flattened_data())
    return sum((pixels[y*17+x] > pixels[y*17+x+1]) << (y*16+x) for y in range(16) for x in range(16))
known = [(p, dhash(p)) for p in gallery]
assert not set(order) & {1,4,9,27,47,49}, 'Excluded photo reintroduced'
assert len(gallery) == len(set(gallery)), 'Repeated path'
hashes = [hashlib.sha256(p.read_bytes()).hexdigest() for p in gallery]
assert len(hashes) == len(set(hashes)), 'Exact duplicate'
candidates = [(str(a.relative_to(root)),str(b.relative_to(root)),(ha^hb).bit_count())
              for (a,ha),(b,hb) in combinations(known,2) if (ha^hb).bit_count() <= 12]
print(f'{len(gallery)} images; no repeated paths or exact duplicates.')
print('Near-duplicate candidates (manual review required):', candidates)
assert not candidates, 'Review near-duplicate candidates before adding photos'
