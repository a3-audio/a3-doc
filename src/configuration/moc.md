# A³ Motion Configuration

(moc-hardware)=

## Hardware

A³ Motion is two parts: the **panel** — buttons, encoders, pots and LEDs on
their own microcontroller — and the **touchscreen UI**, a program on a
computer. The panel PCB connects over **USB** to any PC, laptop or
single-board computer, and the two talk a binary poll-frame protocol over USB
serial (described in `firmware/host.py` in
[a3-motion](https://github.com/a3-audio/a3-motion)).

| Part | V03 (current) | V02 |
| :--- | :--- | :--- |
| UI computer | any Linux machine with a touchscreen; tested on an Intel NUC — on the rig it is the Core machine itself. Initially planned for a Raspberry Pi 5 | Raspberry Pi 4B in the housing, Raspberry Pi OS |
| Panel controller | ESP32-S3 (`esp32-s3-devkitc-1-n16r8`) | Teensy 4.1 |
| Panel power | from the computer's USB port; the firmware dims the key LEDs to stay within it | PoE, for the whole box |
| Display | 7" capacitive multi-touch | 7" touchscreen |
| Buttonmatrix PCB | V03 | V02 |
| Mainboard PCB | V03 | V02 |

The power estimate and the pictures of each revision are on
{doc}`../assembly/moc`.

(moc-ui)=

## The UI

The UI is [a3-motion-ui](https://github.com/a3-audio/a3-motion-ui), a JUCE/C++
application. It builds and runs **standalone**, with the full interface and
no panel attached — that is the default, not a degraded mode, and it is how
the interface can be tried without the hardware in the room. How to build it:
{doc}`../development/build`. Its settings and how it finds Core are on
{ref}`How to point the device at another Core <motion-howto-network>`.

On a Core machine set up with the {doc}`installer <install>` (role Motion),
the UI runs as the user service `a3-motion.service`.

(moc-serial)=

## The panel's serial port

The panel's USB serial bridge is a **CH343, USB ID `1A86:55D3`**, written as
`build.hwids` in the firmware's board file
(`firmware/boards/esp32-s3-devkitc-1-n16r8.json`). The tty number it gets
differs from machine to machine, so nothing names it:

- **Flashing** — `pio run -t upload`, `pio device monitor` and
  `install --flash-firmware` find the panel by that USB ID. If more than one
  device matches, set `serial_port` under `[motion]` in the
  {ref}`installer's settings <install-settings>`.
- **The UI** probes the serial ports and takes the one that answers the
  panel's handshake.
- The port belongs to the group `dialout`; the installer adds the user to it
  (it applies from the next login).
