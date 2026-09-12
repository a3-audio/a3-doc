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

- Receives OSC messages from A³ Core
	- Input vu meters per channel (`/vu/*`)
	- Output vu meters for the master section
	- The lamps (`/channel/*/led/*`, `/fx/led`)

- Sends messages back to the microcontroller via USB serial
	- LEDs
	- Displays

A second script, `a3-mixer-set-display/`, drives the channel displays.

### What it is sent and does not listen for

Three `dispatcher.map` calls, and that is the whole list: `/vu/*`,
`/channel/*/led/*`, `/fx/led`. A³ Core sends it a great deal more — every
channel's gain, EQ, volume and FX send, the whole master section, the shared
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

### The pfl lamp was inverted twice

`send_button_leds_data` had a branch of its own for `led_mode == 0` — pfl's —
that wrote `0 if led_on else 255` while every other lamp wrote
`255 if led_on else 0`. A³ Core inverted pfl on the way out as well. The two
cancelled: the desk was right, and `/channel/n/led/pfl` carried the opposite
of what its name said.

That cost nothing while the desk was the only thing listening. It stopped
being nobody's problem when the lamps became something **every** device is
told, so both inversions came out on the same day. What reaches the pixel is
unchanged and this function is now one branch.

## Panel firmware
Written in C++ as a PlatformIO project,
[`hardware/mainboard/firmware/`](https://github.com/a3-audio/a3-mixer/tree/main/hardware/mainboard/firmware).
V02 runs on a Teensy 4.1; V03 moves to a Raspberry Pi Pico with Ethernet.
