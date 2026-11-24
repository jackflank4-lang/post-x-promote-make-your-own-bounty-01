#!/usr/bin/env python3
"""Generate meme.png for post-x-promote-make-your-own-bounty-01.

Composites the official make.fun ghost mark (mark-1024.png from the press
kit, used as-is, scaled proportionally) onto an original poster drawn in
this session with PIL + DejaVu Sans Bold. Run: python3 gen_meme.py
Reads /tmp/ghost.png (press-kit mark, NOT committed to the repo).
Writes meme.png (1024x1024) in the repo root.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
GHOST_PATH = "/tmp/ghost.png"
OUT_PATH = "meme.png"

# Palette (make.fun magenta + deep purple night)
NAVY_TOP = (16, 8, 42)
PURPLE_BOT = (46, 12, 84)
MAGENTA = (255, 46, 136)
MAGENTA_DARK = (214, 0, 110)
WHITE = (255, 255, 255)
GOLD = (255, 210, 63)
INK = (18, 10, 30)

DEJAVU_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size):
    return ImageFont.truetype(DEJAVU_BOLD, size)


def vertical_gradient(w, h, top, bottom):
    """Return an RGB image with a smooth top-to-bottom gradient."""
    img = Image.new("RGB", (w, h))
    draw = ImageDraw.Draw(img)
    for y in range(h):
        t = y / max(h - 1, 1)
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    return img


def star4(draw, cx, cy, r, fill):
    """Draw a 4-pointed sparkle (diamond star) centred at (cx, cy)."""
    k = 0.22
    pts = [
        (cx, cy - r),
        (cx + r * k, cy - r * k),
        (cx + r, cy),
        (cx + r * k, cy + r * k),
        (cx, cy + r),
        (cx - r * k, cy + r * k),
        (cx - r, cy),
        (cx - r * k, cy - r * k),
    ]
    draw.polygon(pts, fill=fill)


def centered_text(draw, cx, y, text, fnt, fill, stroke=0, stroke_fill=None):
    """Draw text centred on cx at top y; return its (width, height)."""
    bbox = draw.textbbox((0, 0), text, font=fnt)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = cx - w / 2 - bbox[0]
    if stroke:
        draw.text((x, y), text, font=fnt, fill=fill,
                  stroke_width=stroke, stroke_fill=stroke_fill)
    else:
        draw.text((x, y), text, font=fnt, fill=fill)
    return w, h


def main():
    img = vertical_gradient(W, H, NAVY_TOP, PURPLE_BOT).convert("RGBA")
    draw = ImageDraw.Draw(img)

    # Soft magenta glow behind the badge area.
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([512 - 330, 540 - 330, 512 + 330, 540 + 330],
               fill=MAGENTA_DARK + (70,))
    from PIL import ImageFilter
    glow = glow.filter(ImageFilter.GaussianBlur(90))
    img.alpha_composite(glow)
    draw = ImageDraw.Draw(img)

    # Scattered sparkles in the background.
    for (x, y, r, col) in [
        (90, 120, 14, WHITE), (930, 90, 11, GOLD), (120, 880, 12, MAGENTA),
        (905, 860, 13, WHITE), (830, 300, 9, GOLD), (180, 320, 9, WHITE),
        (70, 520, 10, GOLD), (955, 520, 10, WHITE), (300, 60, 8, MAGENTA),
        (700, 70, 8, WHITE),
    ]:
        star4(draw, x, y, r, col + (255,) if len(col) == 3 else col)

    # Headline.
    centered_text(draw, 512, 58, "MAKE YOUR OWN", font(88), WHITE,
                  stroke=3, stroke_fill=INK)
    centered_text(draw, 512, 158, "BOUNTY", font(150), MAGENTA,
                  stroke=4, stroke_fill=INK)

    # Official ghost mark, scaled proportionally, pasted with its alpha.
    ghost = Image.open(GHOST_PATH).convert("RGBA")
    badge_size = 430
    ghost = ghost.resize((badge_size, badge_size), Image.LANCZOS)
    img.alpha_composite(ghost, (512 - badge_size // 2, 330))

    # Sub lines.
    centered_text(draw, 512, 798, "DESCRIBE ANY TASK. SET THE REWARD.",
                  font(40), WHITE)
    centered_text(draw, 512, 848, "KEEP A SHARE OF EVERY FEE.",
                  font(40), GOLD)

    # Bottom pill with the sponsor link.
    pill = [150, 912, 874, 982]
    draw.rounded_rectangle(pill, radius=35, fill=MAGENTA_DARK)
    draw.rounded_rectangle(pill, radius=35, outline=WHITE, width=3)
    centered_text(draw, 512, 925, "make.fun/sponsor/new", font(44), WHITE)

    img.convert("RGB").save(OUT_PATH, "PNG")
    print("wrote", OUT_PATH)


if __name__ == "__main__":
    main()
