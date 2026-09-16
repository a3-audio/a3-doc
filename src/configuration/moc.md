# A³ Motion Configuration

Two computers in one box: a Pi runs the touchscreen UI, and a microcontroller
reads the panel. They talk over a binary poll-frame protocol on USB serial; the
firmware is a PlatformIO/Arduino project in
[`firmware/`](https://github.com/a3-audio/a3-motion/tree/main/firmware).

| Part | V03 (current) | V02 |
| :--- | :--- | :--- |
| UI computer | Raspberry Pi 4B | Raspberry Pi 4B, RaspbianOS |
| Panel controller | ESP32-S3 (`esp32-s3-devkitc-1-n16r8`) | Teensy 4.1 |
| Buttonmatrix PCB | V03 | V02 |
| Mainboard PCB | V03 | V02 |

The UI itself is [a3-motion-ui](https://github.com/a3-audio/a3-motion-ui), a
JUCE/C++ application. It builds and runs **standalone**, with the full
interface and no panel attached — that is the default, not a degraded mode, and
it is how the interface can be tried without the hardware in the room.
