# A³ Motion Assembly

## V03

Drawn, printed, populated, and running — in that order.

### The housing, as drawn

Four views of the enclosure and two of the display bezel. The four round
openings in the front wall are the per-channel potentiometers; the perforated
band beside them is the vent.

housing | | | |
---|---|---|---
![](pics_assembly/v03/a3motion_v03_cad_housing_01.png) | ![](pics_assembly/v03/a3motion_v03_cad_housing_02.png) | ![](pics_assembly/v03/a3motion_v03_cad_housing_03.png) | ![](pics_assembly/v03/a3motion_v03_cad_housing_04.png)

bezel | | assembled
---|---|---
![](pics_assembly/v03/a3motion_v03_cad_bezel_01.png) | ![](pics_assembly/v03/a3motion_v03_cad_bezel_02.png) | ![](pics_assembly/v03/a3motion_v03_cad_assembled.png)

The bezel carries the display's mounting plate inside its frame, so the screen
and the surround are one printed part rather than two to align.

### Printed

on the bed | the housing | the bezel | the display mount
---|---|---|---
![](pics_assembly/v03/a3motion_v03_printing.jpg) | ![](pics_assembly/v03/a3motion_v03_housing_01.jpg) | ![](pics_assembly/v03/a3motion_v03_bezel.jpg) | ![](pics_assembly/v03/a3motion_v03_display_mount.jpg)

### The panel

Four rows of illuminated pads with a column at each end — those two columns
are the six function keys, mirrored so either hand reaches them — plus the
channel encoders above and the potentiometers along the front.

front | from inside | the button matrix, with the ESP32-S3
---|---|---
![](pics_assembly/v03/a3motion_v03_panel_front.jpg) | ![](pics_assembly/v03/a3motion_v03_panel_back.jpg) | ![](pics_assembly/v03/a3motion_v03_buttonmatrix_esp32.jpg)

**V03 moves from a Teensy 4.1 to an ESP32-S3** (`esp32-s3-devkitc-1-n16r8`),
the board sitting at the top of the matrix PCB. It talks to the UI over a
binary poll-frame protocol on USB serial — see
[A³ Motion Development](https://a3-audio.github.io/a3-doc/development/moc.html).

### Running

![The device assembled and running](pics_assembly/v03/a3motion_v03_assembled_01.jpg)

![The screen and the pads lit](pics_assembly/v03/a3motion_v03_assembled_02.jpg)

## V02
![](pics_assembly/v02/a3motion_v02_newSoftware.jpg)

## PCB's
### Mainboard PCB V01
| front                                             | back                                             |
| ------------------------------------------------- | ------------------------------------------------ |
| ![](pics_assembly/v01/a3motion-pcb-v01-front.jpg) | ![](pics_assembly/v01/a3motion-pcb-v01-back.jpg) |

![](pics_assembly/v01/a3motion-schematic.jpg)

![](pics_assembly/v01/a3motion-pcb-design.jpg)

### Buttonmatrix PCB V02 
front | back | action
---|---|---
![](pics_assembly/v01/a3motion-button-matrix-pcb-front.jpg) | ![](pics_assembly/v01/a3motion-button-matrix-pcb-back.jpg) | ![](pics_assembly/v01/a3motion-button-matrix-leds.jpg)

![](pics_assembly/v01/a3motion-buttons-schematic.jpg)

![](pics_assembly/v01/a3motion-buttons-pcb-design.jpg)

## Housing V02
The housing was build with Blender (*.obj) and is ready to print on a 3d-printer (*.stl).

draft | print
---|---
![a3motion-housing](pics_assembly/v02/a3motion_v02_housing_01.jpg) | ![](pics_assembly/v02/a3motion_v02_housing_02.jpg)


## Estimated power consumption
Device | Watts
---|---
Raspberry Pi 4b | 15W
Teensy 4.1 | 2.5W
40 NeoPixel | 11W
SunFounder Raspberry Pi 4 Display Touchscreen 7 Inch | 3W
---|---
Sum | 31.5W

## V01

![](pics_assembly/history/re_202109-v01-a3motion.jpg)

## V00
![](pics_assembly/v00/a3motion-buttonmatrix-pcb-v01.jpg)

![](pics_assembly/v00/a3motion-buttonmatrix-v01.jpg)