# A³ Motion Configuration

## V03
- Raspberry Pi 4B running the touchscreen UI
- ESP32-S3 (`esp32-s3-devkitc-1-n16r8`) for buttons, encoders, pots and LEDs
- A³ Motion Buttonmatrix PCB V03
- A³ Motion Mainboard PCB V03

The panel talks to the UI over a binary poll-frame protocol on USB serial; the
firmware is a PlatformIO/Arduino project in
[`firmware/`](https://github.com/a3-audio/a3-motion/tree/main/firmware).

## V02
- RaspbianOS
- Raspberry pi 4b
- teensy 4.1
- A³ Motion Buttonmatrix PCB V02
- A³ Motion Mainboard PCB V02
