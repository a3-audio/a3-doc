# SPDX-FileCopyrightText: 2026 A3 Audio <contact@a3-audio.com>
# SPDX-License-Identifier: CC-BY-SA-4.0
"""Brings src/user/pics_user/a3-connecting-diagram.png up to date, in place.

The picture was drawn in Figma (src/user/pics_user/grafic_design/A3-Webseite Assets.fig)
and only exists as a PNG here. This script edits that PNG rather than
redrawing it: it paints the V03 A3 Motion over the old one and adds StemDeck
beside A3 Core, in the same ink, paper, line weight and typeface (XXII Aven,
from the homepage's src/style/font/).

Run from the repository root, once, on the old picture:
  FONTCONFIG_FILE=<a fonts.conf that adds the homepage's font folder> \\
      python3 tools/diagrams/connecting_diagram.py
"""

import math

import cairo

from diagram_style import INK, PAPER, draw_text
from motion_pictogram import draw_motion

PATH = "src/user/pics_user/a3-connecting-diagram.png"
FONT = "XXII Aven"


def replace_motion(ctx):
    ctx.set_source_rgb(*PAPER)
    ctx.rectangle(540, 68, 72, 122)
    ctx.fill()
    ctx.save()
    scale = 0.3
    ctx.translate(548 - 110 * scale, 75 - 24 * scale)
    ctx.scale(scale, scale)
    draw_motion(ctx, INK)
    ctx.restore()


def open_arrow_head(ctx, x, y, angle, size=7):
    for side in (-1, 1):
        ctx.move_to(x, y)
        ctx.line_to(x - size * math.cos(angle + side * 0.7), y - size * math.sin(angle + side * 0.7))
    ctx.stroke()


def add_stemdeck(ctx):
    ctx.set_source_rgb(*INK)
    ctx.set_line_width(2)
    # a laptop: screen with two decks on it, and its base
    ctx.rectangle(172, 207, 64, 40)
    ctx.stroke()
    for cx in (191, 217):
        ctx.arc(cx, 227, 7, 0, 2 * math.pi)
        ctx.stroke()
        ctx.arc(cx, 227, 1.5, 0, 2 * math.pi)
        ctx.fill()
    ctx.move_to(162, 251)
    ctx.line_to(246, 251)
    ctx.line_to(242, 256)
    ctx.line_to(166, 256)
    ctx.close_path()
    ctx.fill()
    draw_text(ctx, 204, 275, "StemDeck", 14, INK, align="center", family=FONT)

    # into A3 Core
    ctx.set_line_width(2)
    ctx.move_to(256, 238)
    ctx.line_to(318, 238)
    ctx.stroke()
    open_arrow_head(ctx, 319, 238, 0)
    draw_text(ctx, 287, 224, "Audio", 14, INK, align="center", family=FONT)


def main():
    surface = cairo.ImageSurface.create_from_png(PATH)
    ctx = cairo.Context(surface)
    replace_motion(ctx)
    add_stemdeck(ctx)
    surface.write_to_png(PATH)
    print(PATH)


if __name__ == "__main__":
    main()
