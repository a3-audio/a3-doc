# A³ Motion Developement
## Backend
A³ Motion backend runs Arch Linux ARM. To configure your own
- [A³ Motion Configuration](https://doc.a3-audio.com/Ambijockey/doc/configuration/moc.html) 
- [A³ Motion Configuration](https://doc.a3-audio.com/Ambijockey/doc/assembly/moc.html) 

## A³ Motion Controller UI
A³ Motion Controller UI is the most complex part to develop. It is in a different repository
- [A³Motion - configuration](https://doc.a3-audio.com/configuration/moc.html)

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
