# A³ Core v0.2 Assembly

mix | config
---|---
![](pics_assembly/v02/a3core_v02_mix.jpg) | ![](pics_assembly/v02/a3core_v02_config.jpg)

## Specifications
- A powerful linux pc (could be headless)
	- based on debian, linux realtimekernel and jack audioserver
- Different class compliant audio hardware could be installed
	- Tested: Focusrite, RME, Digigram
- We provide a reaper session for a3mix but a3core can run different audio backends
	- Tested: Reaper, Panoramix, IEM-Pluginsuite, puredata, supercollider, Bitwig Studio
- IO roundtrip latency are measured from 1.3ms to 2.8ms, depends on audio and pc hardware components 