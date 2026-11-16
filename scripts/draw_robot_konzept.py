"""Konzept-Skizze von Prima (PIL, lokal, kein KI-Render).

Erstellt: renders/roboter_konzept.png
Merkmale (identisch mit Exposé/Shotlist): cremefarbene matte Schale mit
rostfarbenen Kratzern, ein großes rundes bernsteinfarbenes Auge, dünne leuchtend
rote Antenne, kleiner abgenutzter grauer Rucksack, kurze dicke Beine.
"""

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

random.seed(17)
W, H = 1600, 1200
img = Image.new("RGB", (W, H))
draw = ImageDraw.Draw(img)

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

# Hintergrund-Verlauf (gedämpfte Erdtöne: Moosgrün/Schiefergrau)
top, bottom = (35, 43, 40), (22, 26, 24)
for y in range(H):
    draw.line([(0, y), (W, y)], fill=lerp(top, bottom, y / H))

# Bau-Silhouetten (dezent)
for (x, w, h) in [(60, 300, 520), (420, 220, 640), (1020, 260, 560), (1330, 220, 700)]:
    draw.rectangle([x, 620 - h, x + w, 620], fill=(30, 37, 34))
    for wy in range(620 - h + 40, 600, 90):
        for wx in range(x + 30, x + w - 40, 70):
            if random.random() < 0.5:
                draw.rectangle([wx, wy, wx + 34, wy + 44], fill=(38, 46, 41))

# Efeu-Andeutungen an den Bauten
for (x0, y0) in [(60, 620), (420, 620), (1020, 620), (1330, 620)]:
    for _ in range(40):
        x = x0 + random.randint(0, 250)
        y = y0 - random.randint(0, 300)
        draw.ellipse([x, y, x + random.randint(8, 20), y + random.randint(8, 20)], fill=(48, 62, 45))

# Boden
draw.rectangle([0, 980, W, H], fill=(28, 33, 28))
for _ in range(120):
    x = random.randint(0, W)
    y = random.randint(985, H - 5)
    r = random.randint(4, 14)
    draw.ellipse([x, y, x + r, y + r], fill=(40, 54, 40))

# Signal in der Ferne (roter Lichtpunkt)
def glow(draw, img, cx, cy, color, r_max, steps=18):
    for i in range(steps, 0, -1):
        r = int(r_max * i / steps)
        a = int(60 * (1 - i / steps) ** 2)
        ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
        od = ImageDraw.Draw(ov)
        od.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, a))
        img2 = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
        img.paste(img2, (0, 0))
        draw = ImageDraw.Draw(img)
    return draw

draw = glow(draw, img, 1360, 210, (255, 70, 50), 90)
draw.ellipse([1352, 202, 1368, 218], fill=(255, 120, 90))

# Schatten unter dem Roboter
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sd = ImageDraw.Draw(shadow)
sd.ellipse([600, 1000, 1000, 1060], fill=(0, 0, 0, 120))
shadow = shadow.filter(ImageFilter.GaussianBlur(12))
img = Image.alpha_composite(img.convert("RGBA"), shadow).convert("RGB")
draw = ImageDraw.Draw(img)

CX = 800

# Beine (kurze, dicke)
for fx in (735, 865):
    draw.rounded_rectangle([fx - 28, 830, fx + 28, 975], radius=26, fill=(82, 86, 88))
    draw.ellipse([fx - 55, 955, fx + 55, 1000], fill=(64, 68, 70))
    draw.ellipse([fx - 55, 955, fx + 55, 975], fill=(90, 94, 96))

# Rucksack (rechts, abgenutztes Grau)
draw.rounded_rectangle([930, 560, 1080, 800], radius=45, fill=(110, 110, 104))
draw.rounded_rectangle([950, 600, 1060, 690], radius=25, fill=(94, 94, 90))
for _ in range(10):
    x = random.randint(940, 1065)
    y = random.randint(575, 790)
    draw.line([(x, y), (x + random.randint(6, 16), y + random.randint(2, 8))], fill=(78, 78, 75), width=2)

# Körper (cremefarbene matte Schale, Verlauf oben heller)
body_top, body_bot = (236, 231, 217), (204, 198, 181)
for y in range(430, 851):
    t = (y - 430) / 420
    dx = int(180 * math.sqrt(max(0.0, 1 - ((y - 640) / 210) ** 2)))
    if dx > 0:
        draw.line([(CX - dx, y), (CX + dx, y)], fill=lerp(body_top, body_bot, t))
draw.ellipse([620, 430, 980, 850], outline=(150, 145, 130), width=3)

# Riemen des Rucksacks (über die Schultern)
draw.line([(760, 500), (990, 610)], fill=(88, 88, 84), width=26)
draw.line([(735, 690), (985, 760)], fill=(88, 88, 84), width=26)

# Rostfarbene Kratzer auf der Schale
for _ in range(26):
    for _ in range(3):
        x = random.randint(640, 960)
        y = random.randint(450, 830)
        if ((x - 800) / 175) ** 2 + ((y - 640) / 200) ** 2 < 0.85:
            l = random.randint(8, 34)
            ang = random.uniform(0, math.pi)
            x2 = x + l * math.cos(ang)
            y2 = y + l * math.sin(ang)
            draw.line([(x, y), (x2, y2)], fill=(163, 92, 51), width=random.choice([2, 3]))
            break

# Gesichtsscheibe (leicht dunkleres Creme)
draw.ellipse([650, 450, 950, 750], fill=(222, 216, 200))
draw.ellipse([650, 450, 950, 750], outline=(160, 154, 138), width=3)

# Auge (Bernstein, radial: dunkel außen, hell innen)
for r in range(100, 0, -2):
    t = r / 100
    draw.ellipse([800 - r, 600 - r, 800 + r, 600 + r], fill=lerp((255, 205, 120), (150, 80, 20), t))
draw.ellipse([700, 500, 900, 700], outline=(90, 50, 15), width=4)
draw.ellipse([755, 545, 815, 605], fill=(255, 240, 210, 255))  # Highlight
draw.ellipse([762, 552, 802, 592], fill=(255, 252, 240))
draw.ellipse([820, 570, 840, 590], fill=(255, 245, 225))  # kleines zweites Glitzern

# Auge-Heft: roter Signal-Reflex in der Pupille
draw.ellipse([838, 618, 858, 638], fill=(255, 90, 60))

# Antenne (dünne, leuchtend rot)
draw.line([(800, 432), (800, 300)], fill=(60, 58, 55), width=9)
draw = glow(draw, img, 800, 288, (255, 59, 48), 70)
draw.ellipse([782, 270, 818, 306], fill=(255, 59, 48))
draw.ellipse([790, 278, 810, 298], fill=(255, 140, 120))

# Moos an den Füßen
for _ in range(25):
    x = random.randint(680, 920)
    y = random.randint(960, 1005)
    r = random.randint(5, 16)
    draw.ellipse([x, y, x + r, y + r], fill=(52, 70, 48))

out = Path(__file__).resolve().parent.parent / "renders" / "roboter_konzept.png"
out.parent.mkdir(exist_ok=True)
img.save(out)
print("Gespeichert:", out)
