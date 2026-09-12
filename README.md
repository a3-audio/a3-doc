# A³ Audio
Interact live with 3D Audio

## System
- A³ Motion: 4-Channel Motion Sampler (OSC Controller)
- A³ Mixer: 4-Channel DJ Mixer (OSC Controller)
- A³ Core: 3D Sound Server

## Homepage
- https://a3-audio.github.io

## Documentation
- https://a3-audio.github.io/a3-doc

## Build

Renders `src/` into `doc/` — the same command CI runs:

```bash
sphinx-build src doc
```

Dependencies, either from the distribution (Debian/Ubuntu):

```bash
sudo apt install python3-sphinx python3-myst-parser python3-sphinx-rtd-theme python3-sphinxcontrib-video
```

or into a virtualenv:

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
```

## Repos
- https://github.com/a3-audio

## Contact
- E-Mail [p5hcu1@systemli.org](mailto:p5hcu1@systemli.org)
## Where this fits

A³ is seven repositories and one system. **The structure, the workflow and the
versioning are described once, in the umbrella:**
[a3-audio/a3-system](https://github.com/a3-audio/a3-system#repositories-and-versioning).

The short of it: work happens on `main`, a version is an annotated tag, and
the same tag name is set in every repository at once — `v03.0` is the first.
