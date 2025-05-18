# A³ Mixer Assembly
## V02
![](pics_assembly/v02/a3mix_v02_displays.jpg)

## PCB V02
![a3mix-pcb-v02](pics_assembly/v01/a3mix-pcb-v02.jpg)

![a3mix-schematic](pics_assembly/v01/a3mix-schematic.jpg)

![a3mix-pcb-design](pics_assembly/v01/a3mix-pcb-design.jpg)

## Housing V02
draft | print
---|---
![](pics_assembly/v02/a3mix_v02_housing_01.jpg) | ![](pics_assembly/v02/a3mix_v02_housing_02.jpg)

## Headphones
2 XLR sockets on the back are connected to a 6.3mm jack socket on the front. An external headphones amp is needed

## Assembly
1 | 2
---|---
![](pics_assembly/v02/a3mix_v02_desk_02.jpg) | ![](pics_assembly/v02/a3mix_v02_desk_03.jpg)
![](pics_assembly/v02/a3mix_v02_desk_01.jpg) | 
![](pics_assembly/v02/a3mix_v02_wires_01.jpg) | ![](pics_assembly/v02/a3mix_v02_wires_02.jpg)

## Specifications
### Multiplexer pin configuration
#### Multiplexer 1-4 (hc4051)
Function (potentiometer)| Pin
---|---
GAIN | 0 
EQ HIGH | 1 
EQ MID | 2 
EQ LOW | 3 
VOLUME | 4
FX SEND | 5

#### Multiplexer 5 (hc4051)
Function (potentiometer) | Pin
---|---
MASTER | 0 
BOOTH | 1
PHONES MIX | 2
PHONES VOLUME | 3
TAP BUTTON | 4
FX FREQUENCY | 7
FX RESONANCE | 8

#### Multiplexer 6 (hc4051)
Function (buttons) | Pin
---|---
FX TOGGLE | 0-3
3D TOGGLE | 4-7

### Leds
- 4 led-buttons for heapdphones prelisten function (pfl)
- 4x9 NeoPixel for input vu (ws2811)
- 10 NeoPixel for fx and 3d-section (ws2811)
- 1x 8x32 LED-Matrix max7219
### Displays
- 5x 0.96 inch OLED SSD1306 Display I2C 128 x 64
- TCA9548A I2C IIC Multiplexer

### Estimated power consumption
Device | Watts
---|---
Raspberry Pi 3 Model B | 5W
Teensy 4.1 | 2.5W
46 NeoPixel | 13W
8x32 Leds max7219 | 4.5W
5x 0.96 inch OLED Display | 0.2W
---|---
Sum | 25.2W

## V01
![](pics_assembly/v01/a3mix-prototype.jpg)

![](pics_assembly/v00/a3mix-prototype-v01.jpg)

### Wrapped

![](pics_assembly/history/re_202112-v01-a3mix-green.jpg)

### V00 
![](pics_assembly/v00/a3mix-pcb-v01.jpg)

## V00

| Back | Front
--- | ---
![](pics_assembly/v00/a3mix-pcb-back-v0.jpg) | ![](pics_assembly/v00/a3mix-pcb-front-v0.jpg)
