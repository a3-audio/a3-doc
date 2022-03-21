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

## Jack
### System Input Ports
```
[1/2] Stereo 1
[3/4] Stereo 2
[5/6] Stereo 3
[7/8] Stereo 4
```

### Reaper Output Ports
```
[1/2]    Phones
[3]      Subwoofer booth
[4-12]   Speaker booth
[13-20]  8x mono for output VU-Meter (osc)
[21]     Subwoofer pa
[22-inf] speaker pa
```

## Reaper (Mixer and Pluginhost) Node mapping
- See project for newest information:
 ```a3-audio.RPP```

### Reaper Master
```
receives    name                
--------------------------------
[3]        subbus booth
[4-inf]    stereobus 
[4-inf]    decoderbus
[21]   	   subbus FOH
[22-inf]   speaker FOH
```

#### DJ Master
```
receives    name                
--------------------------------
[3]        subbus
[4-inf]    stereobus
[4-inf]    decoderbus
```

##### Stereo
```
receives    name                
--------------------------------
[1,2]       dj(1-4)-channelbus
```

##### Subwoofer
```
receives    name                
--------------------------------
[3]        dj(1-4)-channelbus
```

##### Decoder
```
receives    name                
--------------------------------
[4-19]        dj(1-4)-channelbus
```

#### Booth Master
```
[3]        subbus_booth
[4-inf]    stereobus_booth
[4-inf]    decoderbus_booth
```

##### Stereo booth
```
receives    name                
--------------------------------
[1,2]       dj(1-4)-channelbus
```

##### Subwoofer booth
```
receives    name                
--------------------------------
[3]        dj(1-4)-channelbus
```

##### Decoder booth
```
receives    name                
--------------------------------
[4-19]        dj(1-4)-channelbus
```

### Phones Master
```
receives    name                
--------------------------------
[1,2]       stereobus_phones
[1,2]       binauralbus_phones
```

#### dj(1-4)-stereo phones
```
receives    name
--------------------------------
[1,2]       dj(1-4)-pfl
[1,2]       mainmix-pfl
```

#### dj(1-4)-binaural phones (3D)
```
receives    name
--------------------------------
[3-18]      dj(1-4)-pfl
[3-18]      mainmix-pfl
```

#### dj(1-4)-pfl (pre fader listen)
```
receives    name
--------------------------------
[1,2]       dj(1-4)-channelbus[stereo]
[4-19]      dj(1-4)-channelbus[b-format]
```

#### Mainmix Phones
```
receives    name
--------------------------------
[1,2]       dj(1-4)-stereo
[4-19]      dj(1-4)-channelbus
[3-18]      reverb
```

### Input section
#### dj(1-4)-channelbus
```
receives    name                
--------------------------------
[1,2]       stereo
[3]			subwoofer
[4-19]      b-format
---
[20,21]     stereo (pfl)
[22-37]     b-format (pfl)
```

##### dj(1-4)-bformat
```
receives    from                        
---------------------
[1,2]		dj(1-4)-input
```

##### dj(1-4)-stereo
```
receives    from      
---------------------
[1,2]		dj(1-4)-input 
```

##### dj(1-4)-Input
```
receives    from      
--------------------
[1,2]		hardware  
[3,4]		hardware  
[5,6]		hardware  
[7,8]		hardware  
```

## FX section
### Reverb Bus
```
receives    name    
------------------
[1-16]      reverb  
```

#### Reverb
```
receives    name  
------------------------
[4-19]      dj(1-4)-b-format
```