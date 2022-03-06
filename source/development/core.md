# A³ Core Development
## Backend
- Archlinux realtime kernel must be well configured to assure  low latency and stable audio processing
- jack2 audio engine and alsa
- Qjackctl may be used to patch virtual audio cables from your hardware to Reaper and back out

### OSC-Router (python)
 - Routes OSC between audioengine and controller
 - ```server.py```

### VU-Meter (Supercollider)
- 12-Channel Jack client
- sends vu-meter (peak and rms) via OSC
- ```VU-Meter.scd```

### FOH Setup Page <- wip
- VST plugins can do good speakermanagement

### IEM Pluginsuite
- [IEM-Pluginsuite](https://plugins.iem.at/) VST plugins for 3D audio processing
- 4x StereoEncoder
- 2x AllraDecoder
- 1x BinauralDecoder
- 2x FDN Reverb
- The Decoder must be configured to fit your speaker setup

### Jmess (digital audio wiring)
- [Jmess](https://github.com/jacktrip/jmess-jack) is used to store and restore jack connections
- [aj-snapshot](https://man.archlinux.org/man/aj-snapshot.1.en) can be used to store and restore alsa connections

### Reaper project (mixer and pluginhost)
- VST plugins must be linux and reaper compatible
 ```a3-audio.RPP```

### Reaper jack connections
Input
```
[1/2] Stereo 1
[3/4] Stereo 2
[5/6] Stereo 3
[7/8] Stereo 4
```
Output
```
[1/2]    Phones
[3]      Subwoofer booth
[4-8]    Speaker booth
[9-12]   4x mono for input vu
[13-20]  8x mono for output vu
[21]     Subwoofer pa
[22-inf] speaker pa
```

### Reaper bus-mapping
Masterbus (reaper master)
```
receives    name                
--------------------------------
[1,2]      phonesbus
[3]        subbus
[4-inf]    stereobus
[4-inf]    decoderbus
```
DJ masterbus
```
receives    name                
--------------------------------
[3]        subbus
[4-inf]    stereobus
[4-inf]    decoderbus
```
Booth bus
```
[3]        subbus
[4-inf]    stereobus
[4-inf]    decoderbus
```
Phones masterbus
```
receives    name                
--------------------------------
[1,2]       stereobus(ph)       
[1,2]       binauralbus(ph)     
-           dj1-pfl
-           dj2-pfl
-           dj3-pfl
-           dj4-pfl
-           mainmixbus
```
Reverbbus
```
receives    name                
--------------------------------
[1-16]      reverb              
[17-32]     reverb(ph)          
```
DJ input bus
```
receives    name                
--------------------------------
[1,2]       stereo
[3-18]      b-format            
[19,20]     stereo (pfl)
[21-36]     b-format (pfl)      
```
Basechannels
```
receives	from			name                
-----------------------------------------
[1,2]		hardware     	dj1-input
[1,2]		dj1-input     	dj1-stereo
[1,2]		dj1-input      	dj1-b-format
[3,4]		hardware     	dj2-input
[1,2]		dj2-input     	dj2-stereo
[1,2]		dj2-input      	dj2-b-format
[5,6]		hardware     	dj3-input
[1,2]		dj3-input     	dj3-stereo
[1,2]		dj3-input      	dj3-b-format
[7,8]		hardware     	dj4-input
[1,2]		dj4-input     	dj4-stereo
[1,2]		dj4-input      	dj4-b-format
```