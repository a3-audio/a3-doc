# A³ Motion Configuration

(moc-hardware)=

## Hardware

Two parts: the **panel** (buttons, encoders, pots, LEDs on a microcontroller)
and the **touchscreen UI** on a computer, joined by **USB** serial with a
binary poll-frame protocol (`firmware/host.py` in
[a3-motion](https://github.com/a3-audio/a3-motion)).

| Part | V03 (current) | V02 |
| :--- | :--- | :--- |
| UI computer | any Linux machine with a touchscreen; tested on an Intel NUC; on the rig, the Core itself | Raspberry Pi 4B in the housing |
| Panel controller | ESP32-S3 (`esp32-s3-devkitc-1-n16r8`) | Teensy 4.1 |
| Panel power | USB; the firmware dims the LEDs to stay within it | PoE |
| Display | 7" capacitive multi-touch | 7" touchscreen |
| Buttonmatrix PCB | V03 | V02 |
| Mainboard PCB | V03 | V02 |

Power estimate and pictures: {doc}`../assembly/moc`.

(moc-ui)=

## The UI

[a3-motion-ui](https://github.com/a3-audio/a3-motion-ui) (JUCE/C++) runs
**standalone** with the full interface and no panel — the default, not a
fallback. Build: {doc}`../development/build`; finding Core:
{ref}`another Core <motion-howto-network>`. Installed with role Motion it runs
as `a3-motion.service`.

(moc-serial)=

## The panel's serial port

The panel's USB bridge is a **CH343, `1A86:55D3`** (`build.hwids` in
`firmware/boards/esp32-s3-devkitc-1-n16r8.json`). Its tty number varies, so
nothing uses it:

- **Flashing** (`pio run -t upload`, `pio device monitor`,
  `install --flash-firmware`) finds it by USB ID; with several matches set
  `serial_port` in `[motion]` ({ref}`settings <install-settings>`).
- **The UI** takes the port that answers the panel's handshake.
- Group `dialout`; the installer adds the user (from the next login).
