# SPDX-FileCopyrightText: 2026 A3 Audio <contact@a3-audio.com>
# SPDX-License-Identifier: CC-BY-SA-4.0
"""Draws the A3 Motion pictogram for hardware revision V03.

V03 is the screen on top and the panel below it: three staggered rows of four
knobs (two rows of encoders, one of pots), eight columns of four pads in the
middle and a column of six function keys at each end. Proportions are taken
from the photo src/assembly/pics_assembly/v03/a3motion_v03_panel_front.jpg.

Same frame, stroke and colours as the other device pictograms (400 x 400,
a 180 x 352 outline with a 6 px stroke, #292F36 on #FFFFF3).

Run from the repository root:  python3 tools/diagrams/motion_pictogram.py
Writes a3-motion-icon_{light,dark}.png into src/user/pics_user/ and
src/user/pics_user/grafic_design/, and a3-motion-icon_dark.svg into the
scratch path given with --svg (the homepage keeps its own copy).
"""

import argparse
import os

import cairo

from diagram_style import INK, PAPER

SIZE = 400
FRAME = (110, 24, 180, 352)     # x, y, width, height of the outer outline, as before
STROKE = 6
PAD_PITCH = 15.2
PAD_SIZE = 12.4
KNOB_RADIUS = 5


def rounded_rect(ctx, x, y, w, h, r):
    ctx.new_sub_path()
    ctx.arc(x + w - r, y + r, r, -1.5708, 0)
    ctx.arc(x + w - r, y + h - r, r, 0, 1.5708)
    ctx.arc(x + r, y + h - r, r, 1.5708, 3.1416)
    ctx.arc(x + r, y + r, r, 3.1416, 4.7124)
    ctx.close_path()


def motion_shapes():
    """The device in 400 x 400 coordinates, as primitives:
    ('outline', x, y, w, h, radius), ('box', x, y, w, h, radius) or ('dot', cx, cy, r)."""
    fx, fy, fw, fh = FRAME
    half = STROKE / 2
    shapes = [("outline", fx + half, fy + half, fw - STROKE, fh - STROKE, 0),
              # the 7" screen, portrait 3:4
              ("outline", 128 + half, 38 + half, 144 - STROKE, 192 - STROKE, 2)]

    grid_left = 124
    grid_bottom = 362
    grid_top = grid_bottom - 4 * PAD_PITCH
    inset = (PAD_PITCH - PAD_SIZE) / 2
    pads = [(column, row) for column in range(1, 9) for row in range(4)]
    pads += [(column, row) for column in (0, 9) for row in range(-2, 4)]
    for column, row in pads:
        shapes.append(("box", grid_left + column * PAD_PITCH + inset, grid_top + row * PAD_PITCH + inset,
                       PAD_SIZE, PAD_SIZE, 1.5))

    knob_rows = [(grid_top - 3.43 * PAD_PITCH, 1.5), (grid_top - 2.1 * PAD_PITCH, 2.5),
                 (grid_top - 0.62 * PAD_PITCH, 1.5)]
    for y, first in knob_rows:
        for i in range(4):
            shapes.append(("dot", grid_left + (first + 2 * i) * PAD_PITCH, y, KNOB_RADIUS))
    return shapes


def draw_motion(ctx, ink):
    """Draws motion_shapes(); the caller sets up scale and translation."""
    ctx.set_source_rgb(*ink)
    ctx.set_line_width(STROKE)
    for shape in motion_shapes():
        kind = shape[0]
        if kind == "dot":
            _, cx, cy, r = shape
            ctx.arc(cx, cy, r, 0, 6.2832)
            ctx.fill()
            continue
        _, x, y, w, h, r = shape
        if r:
            rounded_rect(ctx, x, y, w, h, r)
        else:
            ctx.rectangle(x, y, w, h)
        if kind == "outline":
            ctx.stroke()
        else:
            ctx.fill()


def ring_path(x, y, w, h):
    """The outline of a stroked rectangle (centre line x, y, w, h) as outer minus inner edge."""
    half = STROKE / 2

    def box(left, top, right, bottom):
        return f"M{left:.2f} {top:.2f}H{right:.2f}V{bottom:.2f}H{left:.2f}Z"

    return box(x - half, y - half, x + w + half, y + h + half) + box(x + half, y + half, x + w - half, y + h - half)


def svg_markup(dark):
    """A compact hand-written SVG of the icon, for the homepage."""
    ground, ink = ("#292F36", "#FFFFF3") if dark else ("#FFFFF3", "#292F36")
    lines = ['<svg width="400" height="400" viewBox="0 0 400 400" fill="none" xmlns="http://www.w3.org/2000/svg">',
             f'<rect width="400" height="400" rx="6" fill="{ground}"/>']
    for shape in motion_shapes():
        kind = shape[0]
        if kind == "dot":
            _, cx, cy, r = shape
            lines.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r}" fill="{ink}"/>')
            continue
        _, x, y, w, h, r = shape
        if kind == "outline":
            # a filled ring rather than a stroke, as the other pictograms are drawn
            lines.append(f'<path fill-rule="evenodd" fill="{ink}" d="{ring_path(x, y, w, h)}"/>')
        else:
            lines.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{r}" fill="{ink}"/>')
    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def paint_icon(ctx, dark):
    ground, ink = (INK, PAPER) if dark else (PAPER, INK)
    ctx.set_source_rgb(*ground)
    ctx.paint()
    draw_motion(ctx, ink)


def write_png(path, dark):
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, SIZE, SIZE)
    paint_icon(cairo.Context(surface), dark)
    surface.write_to_png(path)


def write_svg(path, dark):
    with open(path, "w", encoding="utf-8") as svg:
        svg.write(svg_markup(dark))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--svg", help="also write the dark icon as SVG to this path")
    args = parser.parse_args()
    for folder in ("src/user/pics_user", "src/user/pics_user/grafic_design"):
        for variant, dark in (("light", False), ("dark", True)):
            path = os.path.join(folder, f"a3-motion-icon_{variant}.png")
            write_png(path, dark)
            print(path)
    if args.svg:
        write_svg(args.svg, True)
        print(args.svg)


if __name__ == "__main__":
    main()
