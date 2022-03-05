# A³ OSC messages
## A³ Core  to REAPER
- ```server.py```

| RECEIVE TYPE | RECEIVE | SEND TYPE | SEND | Description | Interface
| :---| :--- | :--- | :--- | :--- | :---
| OSC | /mic/ch/1-4/gain | OSC | /track/i/fx/i/fxparam/i/value | Channel i gain | potentiometer
| OSC | /mic/ch/1-4/hi  | OSC | /track/i/fxeq/hishelf/gain | Channel i hi | potentiometer
| OSC | /mic/ch/1-4/mid  | OSC | /track/i/fxeq/band/0/gain | Channel i mid | potentiometer
| OSC | /mic/ch/1-4/lo  | OSC | /track/i/fxeq/loshelf/gain | Channel i low | potentiometer
| OSC | /mic/ch/1-4/volume  | OSC | /track/i/volume | Channel i volume | potentiometer
| OSC | /mic/master/volume  | OSC | /track/i/volume | Master volume | potentiometer
| OSC | /mic/master/booth  | OSC | /track/i/volume | Booth volume | potentiometer
| OSC | /mic/master/phMmix | OSC | /track/i/volume | Phones Mix | potentiometer
| OSC | /mic/master/phVol  | OSC | /track/i/volume | Phones volume | potentiometer
| OSC | /mic/ch/1-4/fxparm/fxfreq  | OSC | /track/i/fx/i/fxparam/i/value | FX hipass and lopass frequency |  potentiometer
| OSC | /mic/ch/1-4/fxparm/fxres  | OSC | /track/i/fx/i/fxparam/i/value | FX Resonance | potentiometer
| OSC | /mic/ch/1-4/pfl  | OSC | /track/i/mute | Channel i pfl | buttons
| OSC | /mic/ch/1-4/mode  | OSC | /track/i/mute | Channel i mode (Stereo, 3D) |  buttons
| OSC | /mic/ch/1-4/fxmode  | OSC | /track/i/mute | Channel i mode (hipass, lopass) |  buttons
| OSC | /moc/ch/1-4/side  | OSC | /track/i/fx/i/fxparam/i/value | Channel i reverb send | potentiometer

All parameters are normalized to float [range 0-1] 

## A³ Mix
| RECEIVE TYPE | RECEIVE | SEND TYPE | SEND | Description | Interface
| :---| :--- | :--- | :--- | :--- | :---
| OSC | /vu/rcv/01-04 | serial | "VU"{track},peak,rms | input vu ff (peak/rms) | software
| OSC | /vu/rcv/05-12 | serial | "VU"{track},peak,rms | output vu ff (peak/rms) | software
| OSC | /mic/ch/1-4/pflled | serial | "PFL"{track},bool  | pre fader listen or cue | leds
| serial | FX_MODE:{HIGH_PASS,LO_PASS} | OSC | /mic/channel/fxmode/{hipass,lopass} | FX Mode | buttons
| serial | B{channel},bool | OSC | /mic/channel/{1-4}/pfl/bool | pre fader listen or cue | buttons
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/{1-4}/gain | channel gain | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/{1-4}/hi |eq high | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/{1-4}/mid | eq mid | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/{1-4}/lo | eq low | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/{1-4}/volume | channel volume | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/volume | master volume | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/booth | booth volume | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/phMix | phones mix | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/phVol | phones volume | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/fxres | fx resonance | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/fxfreq | fx frequency | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/1-4/mode | channel 3D mode| button
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/1-4/fxmode | channel FX mode| button

## A³ Motion
| RECEIVE TYPE | RECEIVE | SEND TYPE | SEND | Description | Interface
| :---| :--- | :--- | :--- | :--- | :---
| serial | P:{channel}:P:{potentiometer},float | OSC | /moc/ch/1-4/width/ | stereo width | potentiometer
| serial | P:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/side | reverb send | potentiometer
| serial | Enc:{channel}:P:{potentiometer},float | OSC | | menu navigation | encoder
| serial | EB:{channel}:P:{potentiometer},float | OSC | | menu navigation | encoder buttons
| serial | B:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/fxfreq | fx frequency | potentiometer
| serial | D:{channel}:A:{azimuth} | /StereoEncoder/azimuth | azimuth angle per channel | touchscreen
| serial | D:{channel}:E:{elevation} | /StereoEncoder/elevation | elevation angle | touchscreen

### bpm (receive) <- wip
- /moc/bpm
- /mic/bpm
