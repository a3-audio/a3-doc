# A³ Mixer Development

## Python script a3-mixer.py

`software/scripts/a3-mixer.py` in [a3-mixer](https://github.com/a3-audio/a3-mixer).

| Direction | What |
| :--- | :--- |
| panel → script (USB serial) | buttons, faders, encoders |
| script → Core (OSC) | the same, as A³ addresses |
| Core, beat-analyzer → script | input meters `in1_pre_L` … `in4_pre_R` (`/vu/51`–`/vu/58`, louder side); analog inputs `analog1_L` … `analog4_R` (`/vu/1`–`/vu/8`); outputs `main_sub`, `main_top1`–`7` (`/vu/11`–`/vu/18`); lamps (`/channel/{ch}/cue/led`, `/channel/{ch}/filter/led`, `/filter/led`); `/beat`; selector state (`/channel/{ch}/stem…`, `/aux-return/stem…`); display meters `stem_a1` … `stem_b4` (`/vu/41`–`/vu/48`), `stem_aux_L/R` (`/vu/49`–`/vu/50`), `aux_L/R` |
| script → panel (USB serial) | LEDs and VU meters |
| script → displays (I2C) | five OLEDs, below |

Input meters feed the LED VUs and the channel display's A (`Displays.note_input`).

(mic-displays)=

### The displays

What they show: {ref}`the desk's input selectors <a3mix-displays>`. Two parts:

- **`a3-mixer-set-display/display_panel.py`**, pure and tested without a Pi:
  display ↔ multiplexer channel (`PANELS`), reading Core's announcements,
  meter movement, layout. `channel_picture()` turns a cursor, nine levels and
  the stem mask into headings D1 | D2 | A, nine bars, dividers, the arrow and
  the bracket (playing stem = lowest mask bit, else A = `ANALOG_INPUT`, 8). The
  ninth slot is `LAST_SLOT_METERS` (2) wide, so bars keep 10 of 11 pixels on
  128 px; A's bar is centred in it, and the return's CUE field uses the same
  slot. `return_picture()` draws STEM and ANALOG bars, bracket, CUE field and
  arrow. `_bands()` gives three row bands: headings, arrow (`ARROW_ROWS` 5,
  dark row above and below), meters to the bottom (rows 19–63 of 64). Any
  display size.
- **`a3_mixer_displays.py`** draws it with PIL onto the SSD1306s via the
  TCA9548A; imports the Pi libraries only when opening. Without them the desk
  runs without displays.

| Element | Drawing |
| :--- | :--- |
| cursor | solid down-arrow, `ARROW_WIDTH` 10 px, `ARROW_ROWS` 5, over the selected meter or CUE field; meters look the same selected or not |
| bracket | "]" turned 90° CCW, `BRACKET_ROWS` 4: top line in the dark row, legs in the gaps, so the bar stays whole |
| A's bar | the channel's input meter, only while analog plays (`_analog_peak()`); dark while a stem plays |
| CUE field | filled with dark letters when cued, outline otherwise; letters stacked `FRAME` 1 px inside; field `TOGGLE_INSET` 3 px inside its slot |

How:

- **Own thread**: the OSC thread notes, the display thread draws the latest
  state; turns and announcements before meter redraws.
- **Meters on a clock**: `METER_STEPS_PER_SECOND` (10) steps with the peak
  since the last step; silent after 0.5 s unheard; stereo shows the louder
  side.
- **`Ballistics`**: instant rise, `METER_FALL_DB_PER_SECOND` (20) over 48 dB,
  time-based; no peak marks.
- **STEM** uses `stem_aux_L/R` once heard, else the loudest stem on the return.
- **Redraw only on pixel change** (`pixel_key()`: bars, cursor, CUE state,
  bracket, headings). `show_channel()` posts only when the playing stem
  changes. About 17 draws/s instead of 50.
- **Partial updates**: `a3_mixer_oled.py` sends only changed windows.
- **A failed display**: one journal line, retried after 2 s, drawn whole.

`a3-mixer-set-display.py` writes each display's name once at boot; the main
script draws over it.

(mic-truth)=

### Addresses, ports and where the desk gets them

No address of its own: it fetches `a3-osc.json` **from Core**
({ref}`truth <osc-truth>`).

- **Cache** `~/.cache/a3/a3-osc.json` (root's home: the service runs as root).
- **Announcement**: listens on `devices.announce` for Core's `/core/here`
  (every 2 s, truth URL + fingerprint; no router crossing).
- **Update**: on a new fingerprint it fetches `/api/truth`, checks body sha256,
  `X-A3-Truth` and announcement agree, writes the file whole and **exits**;
  systemd restarts it. A refusal is logged; it runs on.
- **At start**: `$A3_OSC_TRUTH`, the cache, the old `software/scripts/a3-osc.json`
  (one more release), else it waits. It never loops on a missing truth.

**Deploying needs no copy step**; address changes happen on Core
({ref}`how <osc-truth>`). Meters are found by name. With every state request it
sends `/device/hello` (name, sha256) for Core's comparison.

### What it is sent and does not listen for

Core sends gain, EQ, volume, sends, master, filter and flags too; pythonosc
drops them silently. The pots are analog, so a returned value could only be
shown, and how to show a disagreement is undecided
({ref}`The way back <osc-way-back>`).

## Panel firmware

PlatformIO, [`hardware/mainboard/firmware/`](https://github.com/a3-audio/a3-mixer/tree/main/hardware/mainboard/firmware),
for the controller on {ref}`A³ Mixer hardware <mic-hardware>`; build: {doc}`build`.

- **Input VUs**: 8 LEDs (1–4 green, 5–6 yellow, 7–8 red). The script sends the
  top lit index (`channel_leds()` in `a3_mixer_meters.py`) at
  `CHANNEL_LED_THRESHOLDS_DB` −36, −24, −18, −12, −9, −6, −3, 0 dBFS; no peak
  dot. Older firmware: green bar, red top.
- **Main VU**: eight columns across four modules, 32 rows.
- **Encoder switches**: all eight `EB` channels reported; unused ones ignored.

A Teensy with older firmware needs reflashing for these.
