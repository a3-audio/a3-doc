# A³ Mixer Configuration

| Part | V03 (in development) | V02 (shipping) |
| :--- | :--- | :--- |
| Computer | Raspberry Pi Pico with Ethernet (WIZnet W5500-EVB-Pico / -Pico2) | Raspberry Pi 3B and Teensy 4.1 |
| Connector | USB-C | |
| Faders | 45 mm | |
| Front jack | 6.3 mm for headphones | |
| Mainboard PCB | V03 (KiCad, `hardware/mainboard/pcb/`) | V02 |
| OS | | RaspbianOS |

V03 replaces the Pi-and-Teensy pair with a single board: one part that both
speaks Ethernet and reads the panel.
