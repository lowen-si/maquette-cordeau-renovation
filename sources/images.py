# Recadre et compresse les photos Pexels (originaux/) vers assets/img/.
import os, sys
from PIL import Image
here = os.path.dirname(os.path.abspath(__file__))
src = os.path.join(here, 'originaux'); dst = os.path.join(here, '..', 'assets', 'img')
MAP = {
  '15798784': 'echoppe-chantier', '7587859': 'echoppe-livree', '19866428': 'echoppe-detail',
  '3990359': 'cuisine-chantier', '6580220': 'cuisine-livree',
  '4756489': 'sdb-chantier', '15369789': 'sdb-livree',
  '5973909': 'trait', '4263067': 'pose-parquet', '15066939': 'batons-rompus',
}
for pid, name in MAP.items():
  im = Image.open(os.path.join(src, pid + '.jpg')).convert('RGB')
  w, h = im.size
  if h / w > 2/3 + .01:  # ramène au 3:2
    nh = int(w * 2/3); top = (h - nh) // 2; im = im.crop((0, top, w, top + nh))
  for tw in (1800, 900):
    r = im.resize((tw, int(im.size[1] * tw / im.size[0])), Image.LANCZOS)
    r.save(os.path.join(dst, f'{name}-{tw}.webp'), 'WEBP', quality=74 if tw > 1000 else 72, method=6)
print('ok')
