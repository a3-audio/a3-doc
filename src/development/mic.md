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

- Sends messages back to the microcontroller via USB serial
	- LEDs
	- Displays

A second script, `a3-mixer-set-display/`, drives the channel displays.

(mic-truth)=

### Addresses, ports and where the desk gets them

The script has no address, port or IP of its own. It reads them from
`a3-osc.json`, the system's one truth (see
{ref}`Where addresses and ports live <osc-truth>`) — and it gets that file
**from Core**, not by hand.

- **The cache.** The desk keeps the last truth it fetched in
  `~/.cache/a3/a3-osc.json`. The service runs as root, so that is root's home
  on the desk.
- **The announcement.** The desk listens on UDP port 7790. Every 2 seconds
  Core broadcasts OSC `/core/here` there, with two strings: the URL of its
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

A handful of `dispatcher.map` calls, and that is the whole list: the meters,
the lamps (`/channel/{ch}/cue/led`, `/channel/{ch}/filter/led`,
`/filter/led`) and `/beat`. A³ Core sends it a great deal more — every
channel's gain, EQ, volume and aux send, the whole master section, the shared
filter, every flag — and all of it is dropped without a word, because
pythonosc passes a message with no matching pattern straight into nothing.

That has been true for as long as the reverse path has existed. It stopped
being invisible on 2026-09-12, when A³ Motion's software mixer began showing
the same values: the desk is now the only device in the system that does not
know its own state beyond its lamps.

Wiring it up is not the hard part. The pots here are **analog** — a returned
value cannot move a knob, only be displayed — so the question is what a
channel display should show when the knob under it and the value in REAPER
disagree, and they will, the moment somebody touches the same channel on the
other mixer. A display showing a number the knob below it does not have is
worse than one showing nothing. Tracked in
`issues/a3-mixer-hoert-nur-leds-und-vu.md`.

### Three addresses that went out and were never answered

Found on 2026-09-12 by holding the OSC reference against A³ Core's generated
register:

- **`/channel/n/enc` and `/channel/n/encbtn`** — the channel's rotary encoder
  and its push switch. No handler anywhere, and no decision behind them. The
  script even remembered which encoder was used last, so something was
  planned; nobody could say what. Removed.
- **`/tap`** — went to A³ Core, on an address Core never subscribed to. The
  handler was there, its `dispatcher.map` line was commented out, and so was
  the `rtmidi` import it needed. The key kept sending and UDP had no way of
  saying that nobody listened. It now goes **straight at the beat-analyzer**,
  the same port and the same message A³ Motion's TAP key sends — press only,
  and `int 1`, which the analyzer reads as the beat within the bar. A tap is
  timing, and timing does not want a relay in the middle.

The **3D key** went in the same round, for a different reason: it is not on
the panel in hardware v3.2, so its entry described a key nobody has and its
lamp a light that is not there. A³ Core's side of it (`/channel/n/4d`) went
the same day.

### The pfl lamp was inverted twice

`send_button_leds_data` had a branch of its own for `led_mode == 0` — pfl's —
that wrote `0 if led_on else 255` while every other lamp wrote
`255 if led_on else 0`. A³ Core inverted pfl on the way out as well. The two
cancelled: the desk was right, and the pfl lamp's address
(`/channel/n/led/pfl` then, `/channel/{ch}/pfl/led` from 2026-09-30, `/channel/{ch}/cue/led` since 2026-10-01) carried
the opposite of what its name said.

That cost nothing while the desk was the only thing listening. It stopped
being nobody's problem when the lamps became something **every** device is
told, so both inversions came out on the same day. What reaches the pixel is
unchanged and this function is now one branch.

## Panel firmware
Written in C++ as a PlatformIO project,
[`hardware/mainboard/firmware/`](https://github.com/a3-audio/a3-mixer/tree/main/hardware/mainboard/firmware),
for the panel controller named on {ref}`A³ Mixer hardware <mic-hardware>`.
How to build it: {doc}`build`.
