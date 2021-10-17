# A³ Motion Assembly
## PCB
### Mainboard
![a3motion-schematic](https://doc.orbitalwaves.net/static/v01/a3motion-schematic.jpg)
![a3motion-pcb-design](https://doc.orbitalwaves.net/static/v01/a3motion-pcb-design.jpg)

### Buttonmatrix
![a3motion-buttons-schematic](https://doc.orbitalwaves.net/static/v01/a3motion-buttons-schematic.jpg)
![a3motion-buttons-pcb-design](https://doc.orbitalwaves.net/static/v01/a3motion-buttons-pcb-design.jpg)

### Housing
![a3motion-housing](https://doc.orbitalwaves.net/static/v01/a3motion-housing.png)

The housing was build with Blender (*.obj) and is ready to print on a 3d-printer (*.stl).

```
Ambijockey/hardware/moc/housing
├── moc_housing_bottom.obj
├── moc_housing_bottom.stl
├── moc_housing_top.obj
└── moc_main_pcb.stl
```

## Hardware
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
  
