# A³ Mixer Configuration

(mic-hardware)=

## Hardware

Today: a **Raspberry Pi 3B** runs `a3-mixer.py` ({doc}`../development/mic`); a
**Teensy 4.1** reads the controls and drives LEDs and VUs; USB serial between.

| Part | Today | Planned |
| :--- | :--- | :--- |
| Computer | Raspberry Pi 3B, Raspberry Pi OS | one small, cheap microcontroller board with Ethernet (Olimex-style, e.g. an ESP32 board with LAN), replacing both the Pi and the Teensy |
| Panel controller | Teensy 4.1 (`hardware/mainboard/firmware/`, PlatformIO) | |
| Mainboard PCB | V02 | V03 (KiCad, `hardware/mainboard/pcb/`) |
| Power | PoE | |
| Connector | | USB-C |
| Faders | | 45 mm |
| Front jack | 6.3 mm, headphones | |

The planned board is not chosen (the V03 draft still shows a WIZnet
W5500-EVB-Pico). Parts, multiplexer pins, power: {doc}`../assembly/mic`.

(mic-run)=

## Running the desk

Not yet in the {doc}`installer <install>`; by hand on the Pi:

- The repository is checked out at **`/home/aaa/a3-mixer`**.
- A Python venv at **`/home/aaa/.venv`**, with
  `software/scripts/requirements.txt` installed into it.
- **`a3-mixer.service`** and **`a3-mixer-set-display.service`** from
  `platform-config/raspianos/etc/systemd/system/` (the first runs
  `a3-mixer.py` on the venv, restarting on failure): copy to
  `/etc/systemd/system/`, then
  `sudo systemctl enable --now a3-mixer a3-mixer-set-display`.

No addresses on the desk: it fetches them from Core ({ref}`how <mic-truth>`).
Tests: {ref}`Build and test <build-commands>`.
