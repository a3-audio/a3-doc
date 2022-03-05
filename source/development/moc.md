# A³ Motion Developement
A³ Motion backend runs on Arch Linux ARM on a Raspberry Pi 3 Model B. As Microcontroller we're using Teensy 4.1. 

## UI
A³ Motion UI is the most potential and complex part to develop. It is in a different repository (see [A³Motion - configuration](https://doc.a3-audio.com/configuration/moc.html).

[Ambijockey/doc/configuration/moc](https://doc.a3-audio.com/Ambijockey/doc/configuration/moc.html) 

## OSC <> serial router (python)
Connected to:
- A³ Core (LAN)
- Display (hdmi & usb)
- Teensy (serial usb)

OSC-communication:
- Send stereowidth
- Send stereosides boost
- Send azimuth/elevation
- Receive bpm

Python- script:
- ```Controller_Motion/software/MotionControllerUI/moc_ui.py```

## pcb <> teensy <> serial (c++)
Connected to:
- Mainboard
	- Encoder (gpio)
	- potis (ic: hc4051)
	- neoPixel (gpio)
	- Buttonmatrix (ic: SN74HCT245N)

Firmware:
- ```Controller_Motion/software/teensy/src/main.cpp```
