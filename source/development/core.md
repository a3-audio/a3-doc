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

### Reaper bus-mapping
Masterbus
```
receives    name                
--------------------------------
[1,2]       phonesbus           
[3]         monobus (single)    
[4]         subbus              
[5-20]      spare               
[21-inf]    monobus (multi)     
[21-inf]    stereobus           
[21-inf]    decoderbus          
```
Phonesbus
```
receives    name                
--------------------------------
[1,2]       monobus(ph)         
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
Channelbus
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