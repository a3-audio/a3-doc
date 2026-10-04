# A³ Mixer Configuration

(mic-hardware)=

## Hardware

The desk is two computers today: a **Raspberry Pi 3B** runs `a3-mixer.py`
(see {doc}`../development/mic`), and a **Teensy 4.1** drives the panel — it
reads the faders, pots, encoders and keys, and lights the LEDs and the VU
meters. The two talk over USB serial.

| Part | Today | Planned |
| :--- | :--- | :--- |
| Computer | Raspberry Pi 3B, Raspberry Pi OS | one small, cheap microcontroller board with Ethernet (Olimex-style, e.g. an ESP32 board with LAN), replacing both the Pi and the Teensy |
| Panel controller | Teensy 4.1 (`hardware/mainboard/firmware/`, PlatformIO) | |
| Mainboard PCB | V02 | V03 (KiCad, `hardware/mainboard/pcb/`) |
| Power | PoE | |
| Connector | | USB-C |
| Faders | | 45 mm |
| Front jack | 6.3 mm, headphones | |

The planned board is not chosen yet. The V03 schematic draft in
`hardware/mainboard/pcb/` still carries an earlier candidate, a WIZnet
W5500-EVB-Pico.

The parts, the multiplexer pins and the power estimate of the shipped panel
are on {doc}`../assembly/mic`.

(mic-run)=

## Running the desk

The {doc}`installer <install>` does not set up the desk yet; it is set up by
hand on the Pi:

- The repository is checked out at **`/home/aaa/a3-mixer`**.
- A Python venv at **`/home/aaa/.venv`**, with
  `software/scripts/requirements.txt` installed into it.
- The system unit **`a3-mixer.service`**, from
  `platform-config/raspianos/etc/systemd/system/`, runs
  `software/scripts/a3-mixer.py` on that venv's Python and restarts it when
  it fails. `a3-mixer-set-display.service` beside it runs the display
  script. Copy both to `/etc/systemd/system/`, then
  `sudo systemctl enable --now a3-mixer a3-mixer-set-display`.

No addresses or ports are configured on the desk: it fetches them from Core
(see {ref}`Addresses, ports and where the desk gets them <mic-truth>`). How to
run its tests: {ref}`Build and test <build-commands>`.
