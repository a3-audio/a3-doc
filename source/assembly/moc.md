# A³ Motion Assembly
## A³ Motion v0.2
![](pics_assembly/v02/a3motion.JPG)
![](pics_assembly/v02/a3motion-housing.JPG)

### Hardware
- PoE to USB 5V Adapter
- Raspberry Pi 3 Model B
- Teensy 4.1
- A³ Motion PCB V0.1
- 8 potentimeter
- 16 buttons
- 16 NeoPixel (ws2811)
- 1x Cat extender socket
- Bunch of cables

### PCB's
A³ Motion pcbs are published as kicad projects. You should find all information to assemble peripherals in the circuit-diagram of kicad-projects.

#### Mainboard PCB v0.1
- Kicad project:
```
Ambijockey/hardware/moc/Mainboard-pcb/
```
![](pics_assembly/v01/a3motion-schematic.jpg)
![](pics_assembly/v01/a3motion-pcb-design.jpg)

#### Buttonmatrix PCB v0.1
- Kicad project:
```
Ambijockey/hardware/moc/Buttonmatrix-pcb/
```
![](pics_assembly/v01/a3motion-button-matrix-pcb-front.jpg)
![](pics_assembly/v01/a3motion-button-matrix-pcb-back.jpg)
![](pics_assembly/v01/a3motion-button-matrix-leds.jpg)
![](pics_assembly/v01/a3motion-buttons-schematic.jpg)
![](pics_assembly/v01/a3motion-buttons-pcb-design.jpg)

### Housing v0.2
The housing was build with Blender (*.obj) and is ready to print on a 3d-printer (*.stl).
- Blender project:
```
Ambijockey/hardware/moc/housing
├── moc_housing_bottom.obj
├── moc_housing_bottom.stl
├── moc_housing_top.obj
└── moc_main_pcb.stl
```
![a3motion-housing](pics_assembly/v01/a3motion-housing.png)

### Hardware
- runs on a Raspberry Pi 3 Model B
- powered with PoE -> downstep to 3v on Teensy
- sbc is connected via usb (/dev/ttyACM0) to
- teensy 4.1, it has
    - 1 multiplexer hc4051 (8ch)
        function: width and 3d-boost per channel
    - 2 hc4051
        function: Buttonmatrix
    - 1 NeoPixel-strip (ws2811 led-controller)
        - 16 x status leds buttonmatrix
  
### Estimated power consumption
Device | Watts
---|---
Raspberry Pi 4b | 15W
Teensy 4.1 | 2.5W
40 NeoPixel | 11W
SunFounder Raspberry Pi 4 Display Touchscreen 7 Inch | 3W
---|---
Sum | 31.5W

- raspberry pi 4b: 15W
- teensy4.1: 2.5W
- ws2811 40 LEDs: 11W
- 

## Early versions
### 2020-2021
#### A³ Motion v0.1
![](pics_assembly/v01/a3motion-prototype.jpg)
![](pics_assembly/v01/a3motion-wires.jpg)
![](pics_assembly/v01/a3motion-wires-01.jpg)
![a3motion-v01.jpg](pics_assembly/v00/a3motion-v01.jpg)
#### Buttonmatrix v0.1
![/a3motion-buttonmatrix-v01.jpg](pics_assembly/v00/a3motion-buttonmatrix-v01.jpg)
#### Buttonmatrix v0.0
![a3motion-buttonmatrix-pcb-v01.jpg](pics_assembly/v00/a3motion-buttonmatrix-pcb-v01.jpg)
![a3system-early.jpg](pics_assembly/v00/a3system-early.jpg)