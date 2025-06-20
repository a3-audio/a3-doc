# A³ Mixer Development
## Python script mic.py
- Receives messages from teensy via USB-Serial
	- Buttons
	- Fader
	- Encoder

- sends OSC messages to A³ Core
	- Buttons
	- Fader
	- Encoder

- receives OSC messages from Core
	- Input vu meters per channel
	- Output vu meters for mastersection
	- Status (3d, fx, cue)

- Sends messages to teensy via USB-Serial
	- LEDs
	- Displays
## Teensy firmware main.cpp
Teensy 4.1 firmware is written in c++
