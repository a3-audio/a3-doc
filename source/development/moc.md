# A³ Motion Developement
## Backend
A³ Motion backend runs Arch Linux ARM. To configure your own see the [A³ Motion Configuration](https://doc.a3-audio.com/configuration/moc.html) section

## A³ Motion Controller UI
A³ Motion Controller UI is the most complex part to develop. It is in [A³Motion - Motion Controller UI repository](https://github.com/ambisonic-audio-adventures/MotionControllerUI)

### Input adapter
The user interface is able to run in different modes:
- dev mode:
```
python moc_ui.py --develop
```
- device mode:
```
moc_ui.py --serial_device /dev/ttyACM0 --server_ip "192.168.43.50" --server_port 9000 --encoder_base_port 1337
```

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
