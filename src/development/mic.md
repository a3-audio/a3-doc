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
	- Input vu meters per channel: `in1_pre` … `in4_pre` (`/vu/1`–`/vu/4`)
	- Output vu meters for the master section: `main_sub` and
	  `main_top1` … `main_top7` (`/vu/11`–`/vu/18`)
	- The lamps (`/channel/{ch}/cue/led`, `/channel/{ch}/filter/led`, `/filter/led`)
	- The beat (`/beat`)
	- The state of its input selectors (`/channel/{ch}/stem…`, `/aux-return/stem…`)
	- StemDeck's stem meters (`/vu/41`–`/vu/48`)

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
  Core's announcements are read, and the layout. `channel_picture()` and
  `return_picture()` turn a cursor, what plays and the meter levels into
  headings, meters and a cursor box for a display of any size. It is tested
  without a Pi.
- **`a3_mixer_displays.py`** draws that layout with PIL and sends it to the
  SSD1306s through the TCA9548A multiplexer. It needs the Pi's libraries and
  imports them only when the displays are opened. Without them the desk runs
  on without displays.

How it draws:

- **A thread of its own.** The OSC thread only notes what a display should
  show; the display thread always draws the latest state, so a fast turn does
  not queue one draw per click.
- **Meters on a clock.** Peaks are held, and the meters step
  `METER_STEPS_PER_SECOND` (5) times a second, with the loudest peak since
  the last step. A meter not heard for 0.5 s falls to silence. A turn or an
  announcement is drawn before waiting meter redraws.
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
