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