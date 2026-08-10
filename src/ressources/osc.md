# OSC communication
## A³ Core

| RECEIVE | SEND | DATA TYPE | DATA | DESCRIPTION
| :---| :--- | :--- | :--- | :---
| - | /vu/[0-11] | float (peak), float (rms) | [0-1], [0-1] | Peak and rms vu meter
| - | /channel/pfl/led/[0-3] | bool | [0 or 1] | pfl status
| - | /channel/fx/led/[0-3] | bool | [0 or 1] | fx status
| - | /channel/3d/led/[0-3] | bool | [0 or 1] | 3d status
| - | /fx/led | string | [high_pass, low_pass] | fx mode status
| /channel/[0-3]/gain | - | float | [0-1] | Channel gain
| /channel/[0-3]/eq/high | - | float | [0-1] | Channel eq high
| /channel/[0-3]/eq/mid | - | float | [0-1] | Channel eq mid
| /channel/[0-3]/eq/low | - | float | [0-1] | Channel eq low
| /channel/[0-3]/volume | - | float | [0-1] | Channel volume
| /channel/[0-3]/reverb | - | float | [0-1] | Channel reverb
| /channel/[0-3]/pfl | - | bool | [0 or 1] | Channel pfl
| /channel/[0-3]/fx | - | bool | [0 or 1] | Channel fx
| /channel/[0-3]/3d | - | bool | [0 or 1] | Channel 3d
| /channel/[0-3]/azimuth | - | float | [-180-180] | ambisonic azimuth
| /channel/[0-3]/elevation | - | float | [0-1] | ambisonic elevation
| /channel/[0-3]/width | - | float | [0-1] | ambisonic stereo width
| /channel/[0-3]/order | - | float | [0-1] | ambisonic order
| /master/volume | - | float | [0-1] | Master volume
| /master/booth | - | float | [0-1] | Booth volume
| /master/phones_mix | - | float | [0-1] | Phones mix
| /master/phones_volume | - | float | [0-1] | Phones volume
| /fx/mode | - | string | [high_pass, low_pass] | Global fx mode
| /fx/frequency | - | float | [0-1] | fx filter frequency
| /fx/resonance | - | float | [0-1] | fx filter resonance

## A³ Motion

A³ Motion listens on two UDP ports (configurable in the UI's `config/config.json`,
`oscReceiver`): the main port (default 7771) and a separate VU port (default 7772), so the
high-rate VU stream does not share a socket with the beat clock. Both ports are served by the
same handler, so the split is a convention, not a restriction.

| RECEIVE | SEND | DATA TYPE | DATA | DESCRIPTION
| :---| :--- | :--- | :--- | :---
| /vu/[0-3] | - | float (peak), float (rms) | [0-1], [0-1] | Audio channels 1-4 — drives the corona around each channel blob
| /vu/4 | - | float (peak), float (rms) | [0-1], [0-1] | Subwoofer — drives the sphere glow
| /vu/[5-8] | - | float (peak), float (rms) | [0-1], [0-1] | Speakers 1-4 — drives the speaker spotlights
| /vu/[9-11] | - | float (peak), float (rms) | [0-1], [0-1] | Received but unused — silently discarded
| /beat | - | int (beat), int (bar), int (bpm) | [1-4], [-], [-] | External beat clock. Always updates the status bar readout; in EXT/PIO clock mode it also syncs playback tempo and phase. Float arguments are accepted and truncated to int.

The index ranges above exist only in A³ Motion — senders do not carry that meaning. The
`beat-analyzer`, for instance, simply emits `NUM_VU_CHANNELS` (default 12) meters, one per JACK
input, so which physical signal ends up on which index is decided by the JACK patching alone.
Changing that wiring changes what the UI shows, with nothing to warn you.

## IP and Port
- A³ Core 192.168.43.50:9000
- A³ Mixer 192.168.43.51:7771
- A³ Motion 192.168.43.52:8700