# SPDX-FileCopyrightText: 2026 A3 Audio <contact@a3-audio.com>
# SPDX-License-Identifier: CC-BY-SA-4.0
"""Draws A3 Core's REAPER routing: src/configuration/pics_configuration/reaper_routing.png.

Read off two files of the a3-core package, as of 2026-09-30:
  .local/share/a3-core/config/REAPER/ProjectTemplates/a3-reaper.RPP  (tracks, receives, FX, hardware outs)
  .local/share/a3-core/config/rncbc.org/a3-patchbay.xml              (JACK connections)
and, for the OSC arrows, .local/share/a3-core/layout.json and .local/bin/a3-core.py.

Run from the repository root:  python3 tools/diagrams/reaper_routing.py
Needs pycairo, ImageMagick and the Nimbus Sans font (Debian: fonts-urw-base35).
"""

import os
import subprocess

import cairo

from diagram_style import (BLACK, OSC_LINE, PAPER, WHITE, arrow_head, draw_text, polyline, rgb)

OUT_DIR = "src/configuration/pics_configuration"
LOGO = "src/_static/a3_logo_dark-200px.png"
DATE = "2026-09-30"

WIDTH, HEIGHT = 2420, 1820
BLOCK_W = 196
ROW_H = 22
TITLE_LINE_H = 15
STEP_H = 10
FONT = 11

YELLOW = rgb("#FFFC31")
ORANGE = rgb("#F0A30A")
BOOTH = rgb("#FA6800")
GREEN = rgb("#60A917")
TEAL = rgb("#00D9C0")
VIOLET = rgb("#C3A6DC")
MAGENTA = rgb("#BF1363")
GREY = rgb("#D5D5CC")


class Block:
    """A track or JACK client: header, then input / processing / output sections."""

    def __init__(self, x, y, colour, title, inputs=(), processing=(), outputs=(),
                 text_colour=BLACK, width=BLOCK_W, osc=False):
        self.x, self.y, self.w = x, y, width
        self.colour, self.text_colour = colour, text_colour
        self.title = title.split("\n")
        self.osc = osc
        self.rows = []      # (kind, key, text, y_top, height)
        self.anchor = {}
        y_cursor = y + len(self.title) * TITLE_LINE_H + 10
        sections = [("input", "in", inputs), ("processing", "fx", processing), ("output", "out", outputs)]
        present = [s for s in sections if s[2]]
        for index, (label, prefix, rows) in enumerate(present):
            if not osc:
                self.rows.append(("label", None, label, y_cursor, ROW_H))
                y_cursor += ROW_H
            for key, text in rows:
                self.rows.append(("row", f"{prefix}:{key}", text, y_cursor, ROW_H))
                self.anchor[f"{prefix}:{key}"] = y_cursor + ROW_H / 2
                y_cursor += ROW_H
            if index < len(present) - 1:
                self.rows.append(("step", None, "", y_cursor, STEP_H))
                y_cursor += STEP_H
        self.bottom = y_cursor

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.w

    def draw(self, ctx):
        header_h = len(self.title) * TITLE_LINE_H + 10
        ctx.set_line_width(1)
        header_fill = WHITE if self.osc else self.colour
        header_text = BLACK if self.osc else self.text_colour
        ctx.rectangle(self.x, self.y, self.w, header_h)
        ctx.set_source_rgb(*header_fill)
        ctx.fill_preserve()
        ctx.set_source_rgb(*(OSC_LINE if self.osc else BLACK))
        ctx.stroke()
        for i, line in enumerate(self.title):
            draw_text(ctx, self.x + self.w / 2, self.y + 5 + TITLE_LINE_H * (i + 0.5), line, FONT,
                      header_text, bold=not self.osc, align="center")
        for kind, _key, text, top, height in self.rows:
            fill = WHITE if kind == "label" else self.colour
            ctx.rectangle(self.x, top, self.w, height)
            ctx.set_source_rgb(*fill)
            ctx.fill_preserve()
            ctx.set_source_rgb(*(OSC_LINE if self.osc else BLACK))
            ctx.stroke()
            if kind == "label":
                draw_text(ctx, self.x + self.w / 2, top + height / 2, text, FONT, BLACK, align="center")
            elif kind == "row":
                draw_text(ctx, self.x + 5, top + height / 2, text, FONT, self.text_colour)
            else:
                cx = self.x + self.w / 2
                polyline(ctx, [(cx, top + 1), (cx, top + height - 1)], BLACK)
                arrow_head(ctx, cx, top + height - 1, "down", BLACK, size=5)


def route(ctx, src, src_key, dst, dst_key, lane, colour=BLACK, width=1.0):
    """Right side of src's row, along a vertical lane at x=lane, into the left side of dst's row."""
    ys = src.anchor[src_key]
    yd = dst.anchor[dst_key]
    points = [(src.right, ys), (lane, ys), (lane, yd), (dst.left - 1, yd)]
    polyline(ctx, points, colour, width)
    arrow_head(ctx, dst.left, yd, "right", colour)


def route_path(ctx, points, colour=BLACK):
    """An explicit path; the last segment must be horizontal and end on a block's left side."""
    polyline(ctx, points[:-1] + [(points[-1][0] - 1, points[-1][1])], colour)
    direction = "right" if points[-1][0] > points[-2][0] else "left"
    arrow_head(ctx, points[-1][0], points[-1][1], direction, colour)


def osc_loop(ctx, src, src_key, dst, dst_key, offset):
    """An OSC block above its target in the same column: out on the left, down, back in on the left."""
    ys = src.anchor[src_key]
    yd = dst.anchor[dst_key]
    x = src.left - offset
    polyline(ctx, [(src.left, ys), (x, ys), (x, yd), (dst.left - 1, yd)], OSC_LINE)
    arrow_head(ctx, dst.left, yd, "right", OSC_LINE)


def build():
    c = [30 + i * 262 for i in range(10)]
    b = {}

    # JACK clients in front of REAPER (patchbay)
    b["sys_in"] = Block(c[0], 170, TEAL, "system\n(audio interface)", outputs=[("cap", "capture 1–10")])
    b["mpd"] = Block(c[0], 290, TEAL, "MPD", outputs=[("lr", "left, right")])
    b["n2j"] = Block(c[0], 380, TEAL, "zita-n2j\n(StemDeck over the network)", outputs=[("out", "out 1–10")])
    b["stemdeck"] = Block(c[0], 500, TEAL, "StemDeck\n(on the Core)",
                          outputs=[("out", "12 outputs: bus 1–4, aux, phones")])

    # REAPER's input tracks
    b["analog"] = Block(c[1], 170, GREY, "#29  Analog in  (10 ch)",
                        inputs=[("cap", "[in 1–10] system capture 1–10"), ("mpd", "[in 7–8] MPD, too")],
                        outputs=[("1", "1–2 → channel 1"), ("2", "3–4 → channel 2"), ("3", "5–6 → channel 3"),
                                 ("4", "7–8 → channel 4"), ("x", "9–10 not used")])
    b["adat"] = Block(c[1], 430, GREY, "#30  ADAT In  (8 ch)",
                      inputs=[("none", "no record input set")], outputs=[("2", "3–4 → channel 2")])
    b["zita"] = Block(c[1], 590, GREY, "#31  zita-n2j  (12 ch)",
                      inputs=[("n2j", "[in 11–20] zita-n2j out 1–10"), ("stem", "[in 11–22] StemDeck, 12 outs")],
                      outputs=[("1", "1–2 → channel 1  (bus 1)"), ("2", "3–4 → channel 2  (bus 2)"),
                               ("3", "5–6 → channel 3  (bus 3)"), ("4", "7–8 → channel 4  (bus 4)"),
                               ("aux", "9–10 → Return  (aux)"), ("x", "11–12 not used  (phones)")])

    # One A3 channel, drawn once for all four
    b["osc_in"] = Block(c[2], 170, MAGENTA, "osc  /channel/N/…  /fx/…", osc=True, text_colour=WHITE,
                        processing=[("gain", "gain"), ("eq", "eq/high · eq/mid · eq/low"),
                                    ("fx", "fx · /fx/mode · frequency · resonance")])
    b["input"] = Block(c[2], 300, YELLOW, "N-input\n#12 · #16 · #20 · #24  (2 ch)",
                       inputs=[("analog", "[1–2] Analog in, pair N"), ("adat", "[1–2] ADAT In 3–4  (ch 2 only)"),
                               ("zita", "[1–2] zita-n2j, pair N")],
                       processing=[("gain", "PurestGain · gain"), ("eq", "SmoothEQ3 · EQ"),
                                   ("hp", "TAL-Filter-2 · high-pass"), ("lp", "TAL-Filter-2 · low-pass"),
                                   ("noise", "pink noise  (ch 1 only, muted)")],
                       outputs=[("multi", "[1–2] → N-multi-enc"), ("stereo", "[1–2] → N-stereo-enc"),
                                ("vu", "[1–2] → VU-Meters N  (mono)")])
    b["osc_3d"] = Block(c[3], 170, MAGENTA, "osc  /channel/N/…", osc=True, text_colour=WHITE,
                        processing=[("3d", "3d  (A³ Motion's pot)"), ("pots", "pot_1 · pot_2  (freq · Q)")])
    b["multi"] = Block(c[3], 280, YELLOW, "N-multi-enc  · moving\n#11 · #15 · #19 · #23",
                       inputs=[("input", "[1–2] N-input")], processing=[("gain", "PurestGain · 3d share")],
                       outputs=[("bus", "[1–2] → N-channelbus 3–4"), ("inv", "[1–2] → N-stereo-enc 3–4")])
    b["stereo"] = Block(c[3], 520, YELLOW, "N-stereo-enc  · steady\n#10 · #14 · #18 · #22",
                        inputs=[("input", "[1–2] N-input"), ("inv", "[3–4] N-multi-enc, phase inv.")],
                        processing=[("gain", "2 × PurestGain · steady share"), ("iso", "Isolator3 · freq, Q"),
                                    ("iso2", "Isolator3")],
                        outputs=[("bus", "[1–4] → N-channelbus 1–4")])
    b["osc_bus"] = Block(c[4], 170, MAGENTA, "osc  /channel/N/…", osc=True, text_colour=WHITE,
                         processing=[("vol", "volume"), ("send", "fx-send"), ("pfl", "pfl")])
    b["bus"] = Block(c[4], 300, YELLOW, "N-channelbus\n#9 · #13 · #17 · #21  (4 ch)",
                     inputs=[("stereo", "[1–4] N-stereo-enc"), ("multi", "[3–4] N-multi-enc")],
                     processing=[("vol", "2 × PurestGain · volume")],
                     outputs=[("pfl", "send 1 → N-pfl  (pre FX)"), ("ph", "send 2 → ph-mix"),
                              ("fx", "send 3 → enc_fx  (FX send)"), ("main", "send 4 → enc_main")])
    b["osc_ret"] = Block(c[4], 580, MAGENTA, "osc  /master/…", osc=True, text_colour=WHITE,
                         processing=[("ret", "return")])
    b["ret"] = Block(c[4], 650, YELLOW, "#28  Return  (2 ch)",
                     inputs=[("zita", "[1–2] zita-n2j 9–10  (aux)")],
                     processing=[("gain", "PurestGain · return"), ("g2", "PurestGain")],
                     outputs=[("main", "[1–2] → enc_main 17–18"), ("ph", "[1–2] → ph-mix 17–18"),
                              ("master", "master send  (no hardware out)")])

    # The room
    b["osc_az"] = Block(c[5], 90, MAGENTA, "osc  MultiEncoder, port 1337+n", osc=True, text_colour=WHITE,
                        processing=[("az", "azimuth · elevation")])
    b["enc_main"] = Block(c[5], 160, ORANGE, "#26  enc_main  (18 ch)",
                          inputs=[("bus", "[1–16] N-channelbus, 4 ch each"), ("ret", "[17–18] Return")],
                          processing=[("gain", "8 × PurestGain"), ("enc", "MultiEncoder")],
                          outputs=[("amb", "[1–16] Ambisonics")])
    b["osc_dd"] = Block(c[5], 390, MAGENTA, "osc  DualDelay, port 1340", osc=True, text_colour=WHITE,
                        processing=[("bpm", "delayBPM  (the beat)")])
    b["enc_fx"] = Block(c[5], 460, ORANGE, "#25  enc_fx  (16 ch)",
                        inputs=[("bus", "[1–16] N-channelbus send 3")],
                        processing=[("gain", "8 × PurestGain"), ("enc", "MultiEncoder"), ("dd", "DualDelay")],
                        outputs=[("amb", "[1–16] Ambisonics"), ("ph", "[1–2] → enc_phones 1–2")])
    b["osc_master"] = Block(c[6], 90, MAGENTA, "osc  /master/…", osc=True, text_colour=WHITE,
                            processing=[("vol", "volume")])
    b["dec_master"] = Block(c[6], 160, ORANGE, "#1  dec_master  (16 ch)",
                            inputs=[("main", "[1–16] enc_main"), ("fx", "[1–16] enc_fx")],
                            processing=[("gain", "8 × PurestGain · master volume"),
                                        ("vis", "EnergyVisualizer → A³ Motion"),
                                        ("allrad", "AllRADecoder"), ("simple", "SimpleDecoder")],
                            outputs=[("main", "[1–8] → Main"), ("vu", "[2–5] → VU-Meters 6–9")])
    b["main"] = Block(c[7], 160, ORANGE, "#33  Main  (8 ch)",
                      inputs=[("dec", "[1–8] dec_master")],
                      processing=[("fader", "fader, shipped at −17.6 dB")],
                      outputs=[("hw", "hardware out 1–8")])
    b["dec_rec"] = Block(c[6], 470, VIOLET, "#32  dec_rec  (16 ch)",
                         inputs=[("main", "[1–16] enc_main"), ("fx", "[1–16] enc_fx")],
                         processing=[("bin", "BinauralDecoder")],
                         outputs=[("hw", "hardware out 7–8"), ("vu", "[1–2] → VU-Meters 5  (mono)")])
    b["osc_booth"] = Block(c[6], 700, MAGENTA, "osc  /master/…", osc=True, text_colour=WHITE,
                           processing=[("booth", "booth")])
    b["dec_booth"] = Block(c[6], 770, BOOTH, "#2  dec_booth  (18 ch)",
                           inputs=[("none", "nothing routed in")],
                           processing=[("gain", "8 × PurestGain · booth volume"), ("simple", "SimpleDecoder")],
                           outputs=[("booth", "[1–16] → Booth")])
    b["booth"] = Block(c[7], 700, BOOTH, "#34  Booth  (16 ch)",
                       inputs=[("dec", "[1–16] dec_booth"), ("fx", "[1–16] enc_fx"), ("main", "[1–16] enc_main")],
                       processing=[("fader", "fader at −inf")],
                       outputs=[("hw", "hardware out 1–8")])

    # Headphones
    b["osc_ph"] = Block(c[4], 990, MAGENTA, "osc  /master/… , /channel/N/pfl", osc=True, text_colour=WHITE,
                        processing=[("mix", "phones_mix"), ("pfl", "pfl")])
    b["pfl"] = Block(c[4], 1080, GREEN, "N-pfl\n#4 · #5 · #6 · #7  (4 ch)",
                     inputs=[("bus", "[1–4] N-channelbus, pre FX")],
                     processing=[("mute", "mute = not PFL"), ("fader", "fader = 1 − phones_mix")],
                     outputs=[("enc", "[1–4] → enc_phones 4N−3…4N")])
    b["phmix"] = Block(c[4], 1320, GREEN, "#8  ph-mix  (18 ch)",
                       inputs=[("bus", "[1–16] N-channelbus, post"), ("ret", "[17–18] Return")],
                       processing=[("fader", "fader = phones_mix")],
                       outputs=[("enc", "[1–18] → enc_phones")])
    b["enc_ph"] = Block(c[5], 1080, GREEN, "#27  enc_phones  (18 ch)",
                        inputs=[("pfl", "[1–16] N-pfl"), ("mix", "[1–18] ph-mix"), ("fx", "[1–2] enc_fx 1–2")],
                        processing=[("gain", "8 × PurestGain"), ("enc", "MultiEncoder")],
                        outputs=[("amb", "[1–16] Ambisonics")])
    b["osc_phv"] = Block(c[6], 1010, MAGENTA, "osc  /master/…", osc=True, text_colour=WHITE,
                         processing=[("vol", "phones_volume")])
    b["dec_ph"] = Block(c[6], 1080, GREEN, "#3  dec_phones  (16 ch)",
                        inputs=[("enc", "[1–16] enc_phones")],
                        processing=[("bin", "BinauralDecoder"), ("vol", "PurestGain · phones volume")],
                        outputs=[("ph", "[1–2] → Phones")])
    b["phones"] = Block(c[7], 1080, GREEN, "#36  Phones  (2 ch)",
                        inputs=[("dec", "[1–2] dec_phones")], processing=[("gain", "PurestGain")],
                        outputs=[("hw", "hardware out 11–12")])

    # Meters
    b["vu"] = Block(c[7], 1320, TEAL, "#37  VU-Meters  (12 ch)",
                    inputs=[("in", "[1–4] N-input, mono"), ("rec", "[5] dec_rec 1–2, mono"),
                            ("dec", "[6–9] dec_master 2–5")],
                    processing=[("gain", "PurestGain")],
                    outputs=[("hw", "hardware out 21–32")])
    b["auxsend"] = Block(c[7], 1580, GREY, "#35  Aux Send  (2 ch)", processing=[("none", "empty, not routed")])

    # JACK clients behind REAPER (patchbay)
    b["sys_out"] = Block(c[8], 160, TEAL, "system\n(audio interface)",
                         inputs=[("pb", "[playback 1–20] out 1–20")])
    b["j2n"] = Block(c[8], 470, TEAL, "zita-j2n\n(back to the StemDeck machine)",
                     inputs=[("in", "[in 1–2] out 7–8")])
    b["ba"] = Block(c[8], 1320, TEAL, "beat-analyzer",
                    inputs=[("vu", "[vu_1–12] out 21–32"), ("bpm", "[bpm_1] out 7")])
    return b, c


def draw_edges(ctx, b, c):
    gap = lambda col, k: c[col] + BLOCK_W + 10 + 7 * k   # noqa: E731 -- a lane in the gap right of column col

    # patchbay into REAPER
    route(ctx, b["sys_in"], "out:cap", b["analog"], "in:cap", gap(0, 0))
    route(ctx, b["mpd"], "out:lr", b["analog"], "in:mpd", gap(0, 1))
    route(ctx, b["n2j"], "out:out", b["zita"], "in:n2j", gap(0, 2))
    route(ctx, b["stemdeck"], "out:out", b["zita"], "in:stem", gap(0, 3))

    # inputs into channel N
    route(ctx, b["analog"], "out:1", b["input"], "in:analog", gap(1, 0))
    route(ctx, b["adat"], "out:2", b["input"], "in:adat", gap(1, 1))
    route(ctx, b["zita"], "out:1", b["input"], "in:zita", gap(1, 2))
    route_path(ctx, [(b["zita"].right, b["zita"].anchor["out:aux"]), (gap(1, 5), b["zita"].anchor["out:aux"]),
                     (gap(1, 5), 966), (gap(3, 6), 966), (gap(3, 6), b["ret"].anchor["in:zita"]),
                     (b["ret"].left, b["ret"].anchor["in:zita"])])

    # inside channel N
    route(ctx, b["input"], "out:multi", b["multi"], "in:input", gap(2, 0))
    route(ctx, b["input"], "out:stereo", b["stereo"], "in:input", gap(2, 1))
    route(ctx, b["multi"], "out:bus", b["bus"], "in:multi", gap(3, 0))
    ys, yd = b["multi"].anchor["out:inv"], b["stereo"].anchor["in:inv"]
    mid = (b["multi"].bottom + b["stereo"].y) / 2
    route_path(ctx, [(b["multi"].right, ys), (b["multi"].right + 4, ys), (b["multi"].right + 4, mid),
                     (b["stereo"].left - 8, mid), (b["stereo"].left - 8, yd), (b["stereo"].left, yd)])
    route(ctx, b["stereo"], "out:bus", b["bus"], "in:stereo", gap(3, 1))

    # channelbus sends
    route(ctx, b["bus"], "out:main", b["enc_main"], "in:bus", gap(4, 0))
    route(ctx, b["bus"], "out:fx", b["enc_fx"], "in:bus", gap(4, 1))
    route_path(ctx, [(b["bus"].right, b["bus"].anchor["out:pfl"]), (gap(4, 3), b["bus"].anchor["out:pfl"]),
                     (gap(4, 3), 945), (gap(3, 3), 945), (gap(3, 3), b["pfl"].anchor["in:bus"]),
                     (b["pfl"].left, b["pfl"].anchor["in:bus"])])
    route_path(ctx, [(b["bus"].right, b["bus"].anchor["out:ph"]), (gap(4, 4), b["bus"].anchor["out:ph"]),
                     (gap(4, 4), 952), (gap(3, 4), 952), (gap(3, 4), b["phmix"].anchor["in:bus"]),
                     (b["phmix"].left, b["phmix"].anchor["in:bus"])])
    route(ctx, b["ret"], "out:main", b["enc_main"], "in:ret", gap(4, 2))
    route_path(ctx, [(b["ret"].right, b["ret"].anchor["out:ph"]), (gap(4, 5), b["ret"].anchor["out:ph"]),
                     (gap(4, 5), 959), (gap(3, 5), 959), (gap(3, 5), b["phmix"].anchor["in:ret"]),
                     (b["phmix"].left, b["phmix"].anchor["in:ret"])])

    # the room
    route(ctx, b["enc_main"], "out:amb", b["dec_master"], "in:main", gap(5, 0))
    route(ctx, b["enc_fx"], "out:amb", b["dec_master"], "in:fx", gap(5, 1))
    route(ctx, b["enc_main"], "out:amb", b["dec_rec"], "in:main", gap(5, 0))
    route(ctx, b["enc_fx"], "out:amb", b["dec_rec"], "in:fx", gap(5, 1))
    route(ctx, b["dec_master"], "out:main", b["main"], "in:dec", gap(6, 0))
    route(ctx, b["dec_booth"], "out:booth", b["booth"], "in:dec", gap(6, 1))
    route(ctx, b["enc_fx"], "out:amb", b["booth"], "in:fx", gap(6, 2))
    route(ctx, b["enc_main"], "out:amb", b["booth"], "in:main", gap(6, 3))
    route(ctx, b["enc_fx"], "out:ph", b["enc_ph"], "in:fx", gap(4, -1) + 262)

    # headphones
    route(ctx, b["pfl"], "out:enc", b["enc_ph"], "in:pfl", gap(4, 6))
    route(ctx, b["phmix"], "out:enc", b["enc_ph"], "in:mix", gap(4, 7))
    route(ctx, b["enc_ph"], "out:amb", b["dec_ph"], "in:enc", gap(5, 2))
    route(ctx, b["dec_ph"], "out:ph", b["phones"], "in:dec", gap(6, 4))

    # meters
    route_path(ctx, [(b["input"].right, b["input"].anchor["out:vu"]), (gap(2, 3), b["input"].anchor["out:vu"]),
                     (gap(2, 3), 1560), (gap(6, 6), 1560), (gap(6, 6), b["vu"].anchor["in:in"]),
                     (b["vu"].left, b["vu"].anchor["in:in"])])
    route(ctx, b["dec_rec"], "out:vu", b["vu"], "in:rec", gap(6, 7))
    route(ctx, b["dec_master"], "out:vu", b["vu"], "in:dec", gap(6, 8))

    # hardware outs to JACK clients
    route(ctx, b["main"], "out:hw", b["sys_out"], "in:pb", gap(7, 0))
    route(ctx, b["booth"], "out:hw", b["sys_out"], "in:pb", gap(7, 1))
    route(ctx, b["phones"], "out:hw", b["sys_out"], "in:pb", gap(7, 2))
    route(ctx, b["dec_rec"], "out:hw", b["sys_out"], "in:pb", gap(7, 3))
    route(ctx, b["dec_rec"], "out:hw", b["j2n"], "in:in", gap(7, 3))
    route(ctx, b["dec_rec"], "out:hw", b["ba"], "in:bpm", gap(7, 3))
    route(ctx, b["vu"], "out:hw", b["ba"], "in:vu", gap(7, 4))


def draw_osc(ctx, b):
    osc_loop(ctx, b["osc_in"], "fx:gain", b["input"], "fx:gain", 8)
    osc_loop(ctx, b["osc_in"], "fx:eq", b["input"], "fx:eq", 14)
    osc_loop(ctx, b["osc_in"], "fx:fx", b["input"], "fx:hp", 20)
    osc_loop(ctx, b["osc_in"], "fx:fx", b["input"], "fx:lp", 20)
    osc_loop(ctx, b["osc_3d"], "fx:3d", b["multi"], "fx:gain", 8)
    osc_loop(ctx, b["osc_3d"], "fx:3d", b["stereo"], "fx:gain", 8)
    osc_loop(ctx, b["osc_3d"], "fx:pots", b["stereo"], "fx:iso", 16)
    osc_loop(ctx, b["osc_bus"], "fx:vol", b["bus"], "fx:vol", 8)
    osc_loop(ctx, b["osc_bus"], "fx:send", b["bus"], "out:fx", 14)
    osc_loop(ctx, b["osc_ret"], "fx:ret", b["ret"], "fx:gain", 8)
    osc_loop(ctx, b["osc_az"], "fx:az", b["enc_main"], "fx:enc", 8)
    osc_loop(ctx, b["osc_dd"], "fx:bpm", b["enc_fx"], "fx:dd", 8)
    osc_loop(ctx, b["osc_master"], "fx:vol", b["dec_master"], "fx:gain", 8)
    osc_loop(ctx, b["osc_booth"], "fx:booth", b["dec_booth"], "fx:gain", 8)
    osc_loop(ctx, b["osc_ph"], "fx:mix", b["pfl"], "fx:fader", 8)
    osc_loop(ctx, b["osc_ph"], "fx:pfl", b["pfl"], "fx:mute", 14)
    osc_loop(ctx, b["osc_ph"], "fx:mix", b["phmix"], "fx:fader", 8)
    osc_loop(ctx, b["osc_phv"], "fx:vol", b["dec_ph"], "fx:vol", 8)


def draw_frame_and_title(ctx, b):
    ctx.set_source_rgb(*PAPER)
    ctx.paint()
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(1)
    ctx.rectangle(0.5, 0.5, WIDTH - 1, HEIGHT - 1)
    ctx.stroke()

    logo = cairo.ImageSurface.create_from_png(LOGO)
    ctx.save()
    ctx.translate(28, 20)
    ctx.scale(0.5, 0.5)
    ctx.set_source_surface(logo, 0, 0)
    ctx.paint()
    ctx.restore()
    draw_text(ctx, 140, 58, "Audio engine and OSC control", 34)
    draw_text(ctx, 142, 96, "REAPER template a3-reaper.RPP (37 tracks) and the JACK patchbay a3-patchbay.xml",
              14, (0.25, 0.25, 0.25))
    draw_text(ctx, WIDTH - 20, HEIGHT - 16, DATE, 11, align="right")

    # the channel strip is drawn once for all four
    left = b["osc_in"].left - 24
    top = 150
    right = b["bus"].right + 36
    bottom = b["ret"].bottom + 10
    ctx.set_source_rgb(0.45, 0.45, 0.45)
    ctx.set_line_width(1)
    ctx.set_dash([6, 4])
    ctx.rectangle(left, top, right - left, bottom - top)
    ctx.stroke()
    ctx.set_dash([])
    draw_text(ctx, left + 6, top - 10, "channel N — drawn once, there are four (N = 1–4, the A³ channels)", 12,
              (0.3, 0.3, 0.3), bold=True)

    draw_legend(ctx)


def draw_legend(ctx):
    x, y = 30, 1610
    draw_text(ctx, x, y, "Legend", 12, bold=True)
    entries = [(YELLOW, "channel strip"), (ORANGE, "PA: main mix"), (BOOTH, "booth"), (GREEN, "headphones"),
               (VIOLET, "binaural recording mix"), (TEAL, "JACK clients, meters"), (GREY, "input tracks, unused")]
    for i, (colour, label) in enumerate(entries):
        yy = y + 22 + i * 22
        ctx.rectangle(x, yy - 8, 30, 16)
        ctx.set_source_rgb(*colour)
        ctx.fill_preserve()
        ctx.set_source_rgb(0, 0, 0)
        ctx.stroke()
        draw_text(ctx, x + 40, yy, label, 11)
    xx = 330
    polyline(ctx, [(xx, y + 22), (xx + 40, y + 22)], BLACK)
    arrow_head(ctx, xx + 40, y + 22, "right", BLACK)
    draw_text(ctx, xx + 50, y + 22, "audio: a receive, a send or a JACK connection", 11)
    polyline(ctx, [(xx, y + 44), (xx + 40, y + 44)], OSC_LINE)
    arrow_head(ctx, xx + 40, y + 44, "right", OSC_LINE)
    draw_text(ctx, xx + 50, y + 44, "OSC from a3-core.py, the address it arrives on", 11)
    notes = ["[a–b]  the track's channels a signal lands on or leaves from",
             "#n  REAPER's track number, which is also the number in the OSC address /track/n/…",
             "Interpreted: the roles moving / steady, which Isolator3 carries freq and Q, subwoofer and speakers on Main",
             "(see the text below the picture)."]
    for i, note in enumerate(notes):
        draw_text(ctx, xx, y + 80 + i * 20, note, 11)


def render(ctx, b, c):
    draw_frame_and_title(ctx, b)
    draw_edges(ctx, b, c)
    draw_osc(ctx, b)
    for block in b.values():
        block.draw(ctx)


def main():
    blocks, columns = build()
    png_path = os.path.join(OUT_DIR, "reaper_routing.png")
    png = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)
    render(cairo.Context(png), blocks, columns)
    png.write_to_png(png_path)
    # A flat drawing needs no more than a small palette; a third of the size.
    subprocess.run(["magick", png_path, "-colors", "64", "-define", "png:compression-level=9",
                    "PNG8:" + png_path], check=True)
    print(png_path)


if __name__ == "__main__":
    main()
