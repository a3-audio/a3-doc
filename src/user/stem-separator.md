<!-- SPDX-FileCopyrightText: 2026 Raphael Eismann and contributors -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
(stem-separator)=

# A³ Stem Separator

StemDeck plays every track as four stems, so each part of a track can move through the room on its
own path. The stems come from **A³ Stem Separator**, a command-line tool you run on your own
computer, not on the rig: it sends a track to a rented cloud GPU, splits it into four stems and
writes them as a stem set StemDeck plays. Source:
[a3-stem-separator](https://github.com/a3-audio/a3-stem-separator), a submodule of a3-stemdeck.

## What you get

- **In:** FLAC, WAV or AIFF — single tracks or whole folders. Finished tracks are skipped, and an
  interrupted run continues where it stopped.
- **Out:** one stem set per track, 44.1 kHz / 24-bit FLAC (or WAV), plus the untouched original
  under `originals/`. By default the four stems are split by their job in the room:
  `1 - low` (bass and kick), `2 - tops` (the rest of the kit), `3 - music`, `4 - vocals`. The four
  always add up to the original mix.
- **Names:** the file name becomes the title, so a tempo prefix like `a098 ` survives into the
  stem names.
- **Cost:** the tool shows an estimate before it uploads anything (`--dry-run`); you pay the GPU
  time per track to the cloud provider ([Modal](https://modal.com)).

## Setup, once

Python 3.12 or newer and a Modal account:

```
python3 -m venv .venv
.venv/bin/pip install -e .
.venv/bin/modal token new
.venv/bin/modal deploy modal_app.py
```

## Use

```
stemseparator ~/Music/new/                    # every track in the folder and below
stemseparator track.flac --title "a098 Name"  # one track, with its own title
stemseparator --dry-run ~/Music/new/          # names and cost, nothing uploaded
```

Then copy the library to the machines that play it. The other model sets (`--models`) and every
option are in the tool's
[README](https://github.com/a3-audio/a3-stem-separator#readme).
