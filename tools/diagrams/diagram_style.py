# SPDX-FileCopyrightText: 2026 A3 Audio <contact@a3-audio.com>
# SPDX-License-Identifier: CC-BY-SA-4.0
"""Shared drawing style for the A3 docs diagrams, drawn with pycairo.

The look follows the draw.io signal-flow diagram of 2022: cream paper,
coloured blocks with a bold header, white section rows ("input",
"processing", "output"), thin black audio arrows and light red OSC arrows.
"""

import cairo

PAPER = (1.0, 1.0, 243 / 255)
INK = (41 / 255, 47 / 255, 54 / 255)
BLACK = (0, 0, 0)
WHITE = (1, 1, 1)
OSC_LINE = (234 / 255, 107 / 255, 102 / 255)


def rgb(hex_colour):
    hex_colour = hex_colour.lstrip("#")
    return tuple(int(hex_colour[i:i + 2], 16) / 255 for i in (0, 2, 4))


def set_font(ctx, size, bold=False, family="Nimbus Sans"):
    weight = cairo.FONT_WEIGHT_BOLD if bold else cairo.FONT_WEIGHT_NORMAL
    ctx.select_font_face(family, cairo.FONT_SLANT_NORMAL, weight)
    ctx.set_font_size(size)


def draw_text(ctx, x, y, text, size, colour=BLACK, bold=False, align="left", family="Nimbus Sans"):
    """Draws one line of text with its vertical centre on y."""
    set_font(ctx, size, bold, family)
    extents = ctx.text_extents(text)
    if align == "center":
        x -= extents.x_advance / 2
    elif align == "right":
        x -= extents.x_advance
    font_extents = ctx.font_extents()
    baseline = y + (font_extents[0] - font_extents[1]) / 2
    ctx.set_source_rgb(*colour)
    ctx.move_to(x, baseline)
    ctx.show_text(text)


def arrow_head(ctx, x, y, direction, colour, size=6):
    """A filled head whose tip is at (x, y); direction is 'right', 'left', 'down' or 'up'."""
    dx, dy = {"right": (-1, 0), "left": (1, 0), "down": (0, -1), "up": (0, 1)}[direction]
    px, py = -dy, dx
    ctx.set_source_rgb(*colour)
    ctx.move_to(x, y)
    ctx.line_to(x + dx * size + px * size * 0.45, y + dy * size + py * size * 0.45)
    ctx.line_to(x + dx * size - px * size * 0.45, y + dy * size - py * size * 0.45)
    ctx.close_path()
    ctx.fill()


def polyline(ctx, points, colour, width=1.0):
    ctx.set_source_rgb(*colour)
    ctx.set_line_width(width)
    ctx.move_to(*points[0])
    for point in points[1:]:
        ctx.line_to(*point)
    ctx.stroke()
