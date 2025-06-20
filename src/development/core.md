# A³ Core Development
## Python script core.py
- Receive OSC from
	- A³ Mixer
	- A³ Motion
- Send OSC to
	- Reaper
	- A³ Mixer
	- A³ Motion

## Supercollider vu-meter.scd
- Receive audio from reaper and system via jack audio server
- Sends Peak and RMS VU-Meter as OSC messages to
	- A³ Mixer
	- A³ Motion
	- external