# A³ Core Development

## Python script a3-core.py
`home/aaa/.local/bin/a3-core.py` in the
[a3-core](https://github.com/a3-audio/a3-core) repository is the runtime: it
turns incoming OSC into DSP settings.

- Receives OSC on port 9000 from
	- A³ Mixer
	- A³ Motion
- Sends OSC to
	- REAPER (`127.0.0.1:9001`)
	- the IEM ambisonics plugins (`127.0.0.1:1337+n`, one port per instance)
	- A³ Mixer
	- A³ Motion

The parameter curves — the functions that map a controller value to a DSP
setting — are pure functions of one number and live in the same file.

## SuperCollider vu-meter.scd
- Receives audio from REAPER and the system via the JACK audio server
- Sends peak and RMS VU meters as OSC messages to
	- A³ Mixer
	- A³ Motion
	- external

## Beat-Analyzer
[beat-analyzer](https://github.com/rafjagger/beat-analyzer) is a separate
C++/CMake service on the same JACK graph. It produces the beat clock every
device follows, and the VU meters that drive the A³ Motion visuals. Its clock
source is selectable at runtime with `/clockmode`: its own onset/tempo
analysis, an external `/beat` from A³ Motion, or a Pioneer Pro DJ Link master.
