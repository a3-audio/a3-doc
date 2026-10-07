# A³ Mixer Development

## Python script a3-mixer.py
`software/scripts/a3-mixer.py` in the
[a3-mixer](https://github.com/a3-audio/a3-mixer) repository.

- Receives messages from the panel microcontroller via USB serial
	- Buttons
	- Fader
	- Encoder

- Sends OSC messages to A³ Core
	- Buttons
	- Fader
	- Encoder

- Receives OSC messages from A³ Core and the beat-analyzer
	- Input vu meters per channel, in stereo: `in1_pre_L` … `in4_pre_R`
	  (`/vu/51`–`/vu/58`), the louder side shown
	- The analog inputs, in stereo: `analog1_L` … `analog4_R`
	  (`/vu/1`–`/vu/8`), the level at each channel's analog input
	  whatever the channel plays
	- Output vu meters for the master section: `main_sub` and
	  `main_top1` … `main_top7` (`/vu/11`–`/vu/18`)
	- The lamps (`/channel/{ch}/cue/led`, `/channel/{ch}/filter/led`, `/filter/led`)
	- The beat (`/beat`)
	- The state of its input selectors (`/channel/{ch}/stem…`, `/aux-return/stem…`)
	- The meters on its displays: StemDeck's stem meters `stem_a1` … `stem_b4`
	  (`/vu/41`–`/vu/48`) on the channels; StemDeck's AUX bus
	  `stem_aux_L`/`stem_aux_R` (`/vu/49`–`/vu/50`) and the analog return
	  `aux_L`/`aux_R` on the return. The input meters go to the LED VUs and
	  to the channel display's A (`Displays.note_input`)

- Sends messages back to the microcontroller via USB serial
	- LEDs and VU meters

- Draws the five OLED displays itself, over I2C (see *The displays* below)

(mic-displays)=

### The displays

What the displays show and how the encoders work is on
{ref}`the desk's input selectors <a3mix-displays>`. Inside `a3-mixer.py` it is
split in two:

- **`a3-mixer-set-display/display_panel.py`** is the pure part, with no
  hardware: which display sits on which multiplexer channel (`PANELS`), how
  Core's announcements are read, the meters' movement and the layout.
  `channel_picture()` turns a cursor, nine levels (eight stems, then the
  analog input) and the channel's stem mask into the D1 | D2 | A headings,
  nine plain bars, the dividers, the cursor's arrow box and the active
  bracket over what plays: the playing stem (the mask's lowest bit), or A
  (`ANALOG_INPUT`, position 8) when none plays. The ninth slot is
  `LAST_SLOT_METERS` (2) meters wide, so on a 128-pixel display the bars
  keep 10 of their 11 pixels; A's bar is a stem's width, centred in it. The
  return's CUE field takes the same slot. `return_picture()` turns
  the cursor, the mode and two levels (STEM, ANALOG) into two mono bars
  under their headings, the active bracket over the playing mode's meter,
  the CUE field and the arrow box; nothing stands between the two (the AUX title is gone). `_bands()`
  returns three row bands: the headings, the arrow (`ARROW_ROWS`, 5 rows,
  with a dark row above and below) and the meters, which run to the bottom
  row (rows 19–63 on a 64-row display). Both work for a display of any
  size. It is tested without a Pi.
- **`a3_mixer_displays.py`** draws that layout with PIL and sends it to the
  SSD1306s through the TCA9548A multiplexer. It needs the Pi's libraries and
  imports them only when the displays are opened. Without them the desk runs
  on without displays.

What it draws:

- **The cursor is an arrow**: a solid triangle pointing down,
  `ARROW_WIDTH` (10) pixels wide and `ARROW_ROWS` (5) rows tall, each row a
  pixel narrower on either side. It sits in the arrow band, centred over the
  selected meter or the return's CUE field. Meters are drawn the same
  whether selected or not.
- **The active bracket** is a "]" turned 90 degrees counter-clockwise,
  `BRACKET_ROWS` (4) rows tall: its top line in the dark row over the
  meter, a leg down either side in the gaps, so the bar stays whole. It
  marks what plays, on a channel and on the return.
- **A's bar** is the channel's input meter, the louder side, and only while
  the analog input plays (`_analog_peak()`). That meter carries whatever
  plays on the channel, so while a stem plays A stays dark rather than show
  the stem under its letter.
- **The return's CUE field** is a filled field with dark letters while the
  return is cued, an outline with light letters while it is not; the
  letters stand one over the other, `FRAME` (1) pixel inside the field. The field sits
  `TOGGLE_INSET` (3) pixels inside its slot, apart from the divider beside
  it.

How it draws:

- **A thread of its own.** The OSC thread only notes what a display should
  show; the display thread always draws the latest state, so a fast turn does
  not queue one draw per click. A turn or an announcement is drawn before
  waiting meter redraws.
- **Meters on a clock.** Peaks are held, and the meters step
  `METER_STEPS_PER_SECOND` (10) times a second, with the loudest peak since
  the last step. A meter not heard for 0.5 s falls to silence. A stereo
  source on the return shows the louder of its two sides.
- **Ballistics.** Each meter goes through a `Ballistics` unit: it rises at
  once and falls `METER_FALL_DB_PER_SECOND` (20 dB/s) over the 48 dB range.
  No display draws a peak. The fall runs on the clock, so a late step falls
  as far as the time that passed.
- **STEM's source.** The return's STEM meter takes `stem_aux_L`/`stem_aux_R`
  once the desk has heard them. A truth without these names never sends
  them, and STEM falls back to the loudest stem playing on the return.
- **Redrawn only when the pixels change.** After each step, a display is
  redrawn only if what it paints in pixels (`pixel_key()`: the bars, the
  cursor, the CUE field's on/off, the bracket and the headings, so a mode
  change counts) differs from what was last drawn. `show_channel()` posts a
  redraw only when the stem that plays changes, or between A and a stem: a
  stem added above the playing one moves no pixel. The bus carries about 17 draws a second; ten steps on
  five displays would be 50.
- **Partial updates.** `a3_mixer_oled.py` sends only the windows of the
  picture that changed, not the whole 1 KB frame.
- **A failed display** is one line in the journal; it is tried again two
  seconds later with its latest picture, drawn whole.

`a3-mixer-set-display.py` is a separate one-shot script, run by its own unit
at boot. It writes each display's name; `a3-mixer.py` draws over it when it
starts.

(mic-truth)=

### Addresses, ports and where the desk gets them

The script has no address, port or IP of its own. It reads them from
`a3-osc.json`, the system's one truth (see
{ref}`Where addresses and ports live <osc-truth>`) — and it gets that file
**from Core**, not by hand.

- **The cache.** The desk keeps the last truth it fetched in
  `~/.cache/a3/a3-osc.json`. The service runs as root, so that is root's home
  on the desk.
- **The announcement.** The desk listens on `devices.announce`. Every 2
  seconds Core broadcasts OSC `/core/here` there, with two strings: the URL of its
  truth and the truth's fingerprint. A broadcast does not cross a router.
- **The update.** When Core announces a fingerprint other than the cached
  file's, the desk fetches `/api/truth` from that URL and checks that the
  body's sha256, the `X-A3-Truth` header and the announcement all agree. If
  they do, it stores the file (written whole, so a cut-off write leaves the old
  one) and **exits**; systemd restarts it on the new truth. If the fetch is
  refused, the desk logs why and keeps running on what it has.
- **At start** it takes the first of these: `$A3_OSC_TRUTH` if set; the cache;
  the old copy beside the script, `software/scripts/a3-osc.json` (kept for one
  release, then it goes); otherwise it waits for Core's announcement. A desk
  without a truth, or with one that lacks a word, no longer exits into a
  restart loop.

**Deploying the desk therefore needs no copy step.** Start the service with
Core on the same network and the first announcement brings the truth. Changing
an address is done on Core — see
{ref}`When a port or an address has to change <osc-truth>`.

Its meters are looked up by name in the truth's `vu_meters`, not by number.
And with every state request — at start, too — the desk sends
`/device/hello` with its name and the sha256 of its truth, which Core's window
compares against Core's fingerprint.

### What it is sent and does not listen for

Core sends the desk much more than it listens for — every channel's gain, EQ,
volume and aux send, the master section, the shared filter, every flag — and
pythonosc drops a message with no matching pattern without a word. The pots
are analog: a returned value could only be displayed, not set, and what a
display should show while the knob under it and REAPER disagree is not
decided. See {ref}`The way back <osc-way-back>`.

## Panel firmware
Written in C++ as a PlatformIO project,
[`hardware/mainboard/firmware/`](https://github.com/a3-audio/a3-mixer/tree/main/hardware/mainboard/firmware),
for the panel controller named on {ref}`A³ Mixer hardware <mic-hardware>`.
How to build it: {doc}`build`.

- **Input VUs:** 8 LEDs a channel, coloured by position: 1–4 green, 5–6
  yellow, 7–8 red. `a3-mixer.py` sends the top lit LED's index
  (`channel_leds()` in `a3_mixer_meters.py`): LED *n* lights when the peak
  reaches `CHANNEL_LED_THRESHOLDS_DB`, −36, −24, −18, −12, −9, −6, −3 and
  0 dBFS. There is no separate peak dot. An older firmware draws the same
  bar, green with its top LED red.
- **Main VU:** eight columns over all four LED modules, 32 rows; the stem
  columns on the top module are gone.
- **Encoder switches:** it reports all eight channels of the encoder-switch
  multiplexer (`EB` lines); `a3-mixer.py` ignores a channel it has no target
  for.

A Teensy flashed with older firmware needs flashing again for these.
