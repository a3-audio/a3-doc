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

## IP and Port
- A³ Core 192.168.43.50:9000
- A³ Mixer 192.168.43.51:7771
- A³ Motion 192.168.43.52:8700