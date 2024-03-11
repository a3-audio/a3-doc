# A³ Motion
## Features:
- Standalone OSC controller
- 7" full-color capacitive multi-touch display
- USB-A 2.0 slot for storage with presets (WIP)
## Part Names and functions
![A³ Motion numbered](pics_user/a3-motion-icon_light_numbered.png)

### [1] STEREO WIDTH SEPARATION
- Adjust Stereo Width separation of the two audio input channels. The current state will be displayed on top of touchdisplay (0° : 90°)

### [2] REVERB SEND
- Adjust send level to Reverb. The current state will be displayed on top of touchdisplay (-inf dB to 0 dB)

### [3] DISPLAY
- This full-color multi-touch display shows information relevant to A³Motion’s current operation. Touch the display (and use the hardware controls) to control the A3Motion interface. See Operating Instrucions to learn how to use some basic functions

### [4] FUNCTION ENCODER
- Use these touch-sensitive knobs to adjust various parameters and settings. The knobs can control one column of parameters at a time. The Highlight section on bottom of screen indicates the currently selected column. Press the Encoder button to change which column of parameters they currently control

### [5] MOTION SAMPLE PADS
- Each channel has a column of four iluminated sample pads. See Operaton to use basic functions

## BACK
### ETHERNET SOCKET
- Connect ethernet cable to PoE switch here

## Operating Instructions
- Set looplength with Function Encoder [4]
- Press and hold down one pad [5] to record motion from touchscreen 
	- The pad will flash green / red to indicate record mode
	- Tap on the screen and hold to grab channel soundsource
	- Release the pad and move the soundsource on touchscreen until record length is reached. Longer motion will overwrite previously recorded data
	- Release the touchscreen to end record
	- The pad will stay green to indicate play mode
- Pads without stored motion are dark
- Pads with stored motion are white
- Press white buttons to switch motion on the next beat (related to 120bpm)
- Width [2] and Reverb [3] will not be recorded

## A³ Motion Specification
- PoE to USB 5V Adapter
- PoE cost 31.5W max
- Raspberry Pi 3 Model B
- Teensy 4.1
- A³ Buttonmatrix PCB v0.1
- A³ Motion PCB V0.1

## NETWORK AND PoE
- When a plan calls for multiple devices to be connected to one PoE/PoE+ switch, it’s necessary to ensure the total wattage required by the devices do not exceed the maximum wattage of the switch
- This device powers up as soon as the PoE powersupply is connected

## Box Contents
- A³ Motion
- Network cable
- Quickstart Guide
- Safety & Warranty Manual

## Misc
- Items not listed under Box Contents are sold separately