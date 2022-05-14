# A³ Core Development
- Archlinux realtime kernel must be well configured to assure  low latency and stable audio processing
- jack2 audio engine and alsa
- Qjackctl may be used to patch virtual audio cables from your hardware to Reaper and back out

## Python script OSC-Router
 - Routes OSC between audioengine and controller
 - ```server.py```

## Supercollider script VU-Meter
- 12-Channel Jack client
- sends vu-meter (peak and rms) via OSC
- ```VU-Meter.scd```

## FOH Setup Page
Reach it via vnc player ```vncviewer QualityLevel 2 192.168.43.50```
- Screen 8: Qjackctl (Patching)
- Screen 9: Reaper (Sequencer)
- Screen 10: Reaper (Mixer)

## IEM Pluginsuite
- [IEM-Pluginsuite](https://plugins.iem.at/) VST plugins for 3D audio processing
- StereoEncoder
- AllraDecoder
- BinauralDecoder
- FDN Reverb
- AllraDecoder must be configured to fit your speaker setup

## Plasticity filter FX
- [Plasticity Filter](https://bomshankamachin.es/plugins/plasticityFilter) VST plugin for hipass lopass resonance filter

## Jmess (jack audio wiring)
- [Jmess](https://github.com/jacktrip/jmess-jack) is used to store and restore jack connections
- [aj-snapshot](https://man.archlinux.org/man/aj-snapshot.1.en) can be used to store and restore alsa connections

## Audiobackend Signalflow
![](pics_development/audio_signalflow.drawio.png)
```
