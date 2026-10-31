# A³ System

A³ is a live-performance sound system for DJs and live acts: three networked
devices and a set of programs that play and move music in the room. **A³ Core**
is the computer that does the audio and the 3D sound field, **A³ Mixer** is the
four-channel desk, **A³ Motion** steers where each channel sits in the room,
and **StemDeck** plays each track as four stems. They talk to each other over
OSC on one network. The pages below describe the system as a whole; each device
has its own page in the sidebar.

## What A³ is made of

One version is one tag across every repository, so a system is always assembled from parts of
the same version. Each hardware part carries its revision; the boards of every revision sit side
by side in `hardware/pcb/`, one folder each. Repository, what it is, version, licence:

```
A³ System                   the umbrella: installer, CI, pins  v03.2      GPL-3.0
├─ a3-core                  A³ Core and its window             v03.2      GPL-3.0
│  └─ a3-beat-analyzer      the beat clock                     v03.2      GPL-3.0
├─ a3-doc                   the documentation                  v03.2      CC-BY-SA-4.0
├─ a3-kicad-lib             the shared KiCad parts library     37df6cf    CERN-OHL-S
├─ a3-mixer                 A³ Mixer                           v03.2      GPL-3.0
│  ├─ pcb                   the boards
│  │  ├─ v0_2               the built board                    rev v0.2   CERN-OHL-S
│  │  └─ v3_1               the V03 draft                      rev v3.1   CERN-OHL-S
│  ├─ housing               the housing                        rev v03.2  CERN-OHL-S
│  ├─ firmware              the board's firmware               rev v03.2  GPL-3.0
│  └─ a3-mixer-ui           the virtual desk                   v03.2      GPL-3.0
├─ a3-motion                A³ Motion                          v03.2      GPL-3.0
│  ├─ pcb                   the boards
│  │  ├─ v1                 the first boards                   rev v1     CERN-OHL-S
│  │  └─ v3_1               the current board                  rev v3.1   CERN-OHL-S
│  ├─ housing               the housing                        rev v03.2  CERN-OHL-S
│  ├─ firmware              the board's firmware               rev v03.2  GPL-3.0
│  └─ a3-motion-ui          the Motion UI                      v03.2      GPL-3.0
├─ a3-pro-dj                DJ knowledge, the autopilot        v03.2      GPL-3.0
├─ a3-stemdeck              the stem decks                     v03.2      GPL-3.0
│  └─ a3-stem-separator     the stems, made off the rig        v03.2      GPL-3.0
└─ third-party              what A³ is built on
   ├─ Airwindows            PurestGain, SmoothEQ3, Isolator3   2026-10    MIT
   ├─ BTrack                beat tracking                      1.0.7      GPL-3.0
   ├─ IEMPluginSuite        ambisonics encoder and decoders    v1.16.0    GPL-3.0
   ├─ JUCE                  the application framework          9.0.3      AGPL-3.0 OR JUCE-9
   ├─ kiss_fft              FFT inside BTrack                  1.3.0      BSD-3-Clause
   ├─ Neumann KU 100 HRIR   the binaural head                  2013       CC-BY-3.0
   ├─ platform-espressif32  the Motion board definition        2026-05    Apache-2.0
   └─ Roboto                the window's font                  1.100141   Apache-2.0
```

Boards and 3D-print files are CERN-OHL-S-2.0, code GPL-3.0-or-later, the documentation
CC-BY-SA-4.0; third-party works keep the licence their authors set. The same tree is in the
[a3-system README](https://github.com/a3-audio/a3-system#whats-in-a-system) and, live from the
installed checkout, on the a3-core window's ABOUT page.

```{toctree}
:titlesonly:

how-it-sounds
what-you-need
stemdeck-with-motion
audio-engine
first-set
```
