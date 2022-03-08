# A³ OSC and serial communication
## IP-Addresses
- A³ Core 192.168.43.50
- A³ Mix 192.168.43.51
- A³ Motion 192.168.43.52

## A³ Core
All parameters are normalized to float [range 0-1] 
- ```server.py```
- ```vu-meter.scd```
- ```bpm.scd``` <- wip 

| RECEIVE TYPE | RECEIVE DATA | SEND TYPE | SEND DATA | Destination | Description | Interface
| :---| :--- | :--- | :--- | :--- | :--- | :---
| OSC | /mic/ch/{channel}/gain | OSC | /track/i/fx/i/fxparam/i/value | reaper | Channel i gain | potentiometer
| OSC | /mic/ch/{channel}/hi  | OSC | /track/i/fxeq/hishelf/gain | reaper | Channel i hi | potentiometer
| OSC | /mic/ch/{channel}/mid  | OSC | /track/i/fxeq/band/0/gain | reaper | Channel i mid | potentiometer
| OSC | /mic/ch/{channel}/lo  | OSC | /track/i/fxeq/loshelf/gain | reaper | Channel i low | potentiometer
| OSC | /mic/ch/{channel}/volume  | OSC | /track/i/volume | reaper | Channel i volume | potentiometer
| OSC | /mic/master/volume  | OSC | /track/i/volume | reaper | Master volume | potentiometer
| OSC | /mic/master/booth  | OSC | /track/i/volume | reaper | Booth volume | potentiometer
| OSC | /mic/master/phMmix | OSC | /track/i/volume | reaper | Phones Mix | potentiometer
| OSC | /mic/master/phVol  | OSC | /track/i/volume | reaper | Phones volume | potentiometer
| OSC | /mic/ch/{channel}/fxparm/fxfreq  | OSC | /track/i/fx/i/fxparam/i/value | reaper | FX hipass and lopass frequency |  potentiometer
| OSC | /mic/ch/{channel}/fxparm/fxres  | OSC | /track/i/fx/i/fxparam/i/value | reaper | FX Resonance | potentiometer
| OSC | /mic/ch/{channel}/fxmode  | OSC | /track/i/fx/i/fxparam/i/value | reaper | Channel i mode (hipass, lopass) | button
| OSC | /mic/ch/{channel}/pfl  | OSC | /track/i/mute | reaper | Channel i pfl | button
| OSC | /mic/ch/{channel}/mode  | OSC | /track/i/mute | reaper | Channel i mode (Stereo, 3D) |  button
| OSC | /moc/ch/{channel}/side  | OSC | /track/i/fx/i/fxparam/i/value | StereoEncoder | Channel i reverb send | potentiometer
| audio | channel and master | OSC | /track/i/vu/value ff | A³ mix, A³ Motion | VU meter | supercollider

## A³ Mix
All parameters are normalized to float [range 0-1] 
- ```mic.py```
- ```main.cpp```

| RECEIVE TYPE | RECEIVE DATA | SEND TYPE | SEND DATA | destination | Description | Interface
| :---| :--- | :--- | :--- | :--- | :--- | :---
| OSC | /vu/rcv/01-04 | serial | "VU"{track},peak,rms | teensy | input vu ff (peak/rms) | software
| OSC | /vu/rcv/05-12 | serial | "VU"{track},peak,rms | teensy | output vu ff (peak/rms) | software
| OSC | /mic/ch/{channel}/pflled | serial | "PFL"{track},bool | teensy | pre fader listen or cue | leds
| serial | FX_MODE:{HIGH_PASS,LO_PASS} | OSC | /mic/channel/fxmode/{hipass,lopass} | A³ Core | FX Mode | buttons
| serial | B{channel},bool | OSC | /mic/channel/{{channel}}/pfl/bool | A³ Core | pre fader listen or cue | buttons
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/{{channel}}/gain | A³ Core | channel gain | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/{{channel}}/hi | A³ Core | eq high | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/{{channel}}/mid | A³ Core | eq mid | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/{{channel}}/lo | A³ Core | eq low | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/{{channel}}/volume | A³ Core | channel volume | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/volume | A³ Core | master volume | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/booth | A³ Core | booth volume | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/phMix | A³ Core | phones mix | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/phVol | A³ Core | phones volume | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/fxres | A³ Core | fx resonance | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/fxfreq | A³ Core | fx frequency | potentiometer
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/{channel}/mode | A³ Core | channel 3D mode| button
| serial | T:{channel}:P:{potentiometer},float | OSC | /mic/ch/{channel}/fxmode | A³ Core | channel FX mode| button

## A³ Motion
- ```moc.py```
- ```main.cpp```

| RECEIVE TYPE | RECEIVE DATA | SEND TYPE | SEND DATA | destination | Description | Interface
| :---| :--- | :--- | :--- | :--- | :--- | :---
| serial | P:{channel}:P:{potentiometer},float | OSC | /moc/ch/{channel}/width [f 0:1] | StereoEncoder OSC | stereo width | potentiometer
| serial | P:{channel}:P:{potentiometer},float | OSC | /mic/ch/master/side [f 0:1] | A³ Core OSC | reverb send | potentiometer
| serial | D:{channel}:A:{azimuth} | OSC | /StereoEncoder/azimuth [i -180:180] | StereoEncoder OSC | azimuth angle | touchscreen
| serial | D:{channel}:E:{elevation} | OSC | /StereoEncoder/elevation [i -180:180] | StereoEncoder OSC | elevation angle | touchscreen
| serial | Enc:{channel}:P:{potentiometer},float | python | [f 0:1] | menu navigation | A³ Motion UI | encoder
| serial | EB:{channel}:P:{potentiometer},float | python | [f 0:1] | menu navigation | A³ Motion UI | encoder buttons
