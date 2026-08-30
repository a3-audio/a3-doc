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
	- Input vu meters per channel
	- Output vu meters for the master section
	- Status (3d, fx, cue)

- Sends messages back to the microcontroller via USB serial
	- LEDs
	- Displays

A second script, `a3-mixer-set-display/`, drives the channel displays.

## Panel firmware
Written in C++ as a PlatformIO project,
[`hardware/mainboard/firmware/`](https://github.com/a3-audio/a3-mixer/tree/main/hardware/mainboard/firmware).
V02 runs on a Teensy 4.1; V03 moves to a Raspberry Pi Pico with Ethernet.
