# A³ Motion Development

## A³ Motion Controller UI
The UI is the most complex part of the device: a JUCE / C++17 application
rendering the sphere with OpenGL, in its own repository
[a3-motion-ui](https://github.com/a3-audio/a3-motion-ui), wired into
[a3-motion](https://github.com/a3-audio/a3-motion) as the `ui` submodule.

It owns the motion patterns — recording them from the touchscreen, storing
them as ticks, and playing them back in time with the beat clock — and speaks
OSC to A³ Core.

## Current  Version
![](pics_development/a3motion_ui_new.png)

## Older Version
![](pics_development/a3motion_ui_old.png)

## Before

 ![](pics_development/a3motion-software-mockup.png)

![](pics_development/a3motion-software-mockup_01.png)

## Panel firmware
The buttons, encoders, pots and LEDs are handled by a microcontroller of their
own, which reaches the UI over a binary poll-frame protocol on USB serial.
V02 used a Teensy 4.1; V03 uses an ESP32-S3, built with PlatformIO from
[`firmware/`](https://github.com/a3-audio/a3-motion/tree/main/firmware).
