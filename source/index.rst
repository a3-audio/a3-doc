.. test documentation master file, created by
   sphinx-quickstart on Sat Oct  2 23:20:02 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

***************************
Interact Live with 3d-Audio
***************************
A³ Pandemic is a 3d-audio processor controlled by a 4-channel dj-mixer and a 
16-pad motion-sampler. It is designed to modulate positions of audio-events
live, in a 3d sound-sphere.

A³ Motion (The Motion-Sampler)
##############################
Works like a sampler, but instead audio it samples motion from 
it's touchscreen. 

- adjust loop-length
- store livemotion on sample-pads
- play/pause recorded motionpattern in different modes like loop or one-shot
- sync to bpm
- spread width of a stereo signal
- boost sides from mid/side processing

A³ Mix (The DJ-Mixer)
#####################
A³ Mix is a DJ-Mixer with 3-band-kill-eq, fx-section for hi- and lopass, 3d-toggle, multichannel vu-meter and 3d-prelisten on headphones.
It has a „tape-in“ section for multichannel or stereo direct to mix bus.

A³ Core (The Sound-server)
##########################
A³ Core processes analog audio-signals, calculates 3d-sound-spheres and is remote-controlled by A³ Mix and A³ Motion (or any other osc-controller). A³ Core can handle a wide range of audio-hardware to fit environments like Dante, MADI or any class-compliant.

Requirements
############
- Soundsystem with at least 4 speakers placed around the venue.
- A venue smaller than 20m diameter. For bigger venues more spheres.


with 4 stereo input-channels and a tape-in for multichannel input. 

It is scalable and capable to feed up to 128 speakers in multiple 3d-sound-spheres.

It consists of three 

*********
Usecases:
*********
- A³ Core encodes and decodes: You can preset your show with stereotracks and control-data. You can use [osccontrol-light](https://github.com/drlight-code/osccontrol-light) vst-plugin to send osc-data from inside daw.
- A³ Core decodes: You can pre-encode your show and just send 3rd order b-format (acn, sn3d)
- A³ Core just routes: You get discrete channels for each speaker
- A³ Core simulates speaker-setup: You can play direct out from Dolby or Auro-3D decoder
- A³ Triple: You use A³ Mix and A³ Motion with dj-players to scratch your tracks while moving them.

**********
Quickstart
**********
- Plug in your instruments vinyl, cd, daw ..
- Plug in your speaker
- Put speakers in regular circle around center
- Plug CAT-cable from A³ Mix and A³ Motion to A³ Core
- Plug-In your headphones
- Power on

*********************
Goal for this project
*********************
- 3d-sound everywhere
- Community
- Compatibility
- Easy to use
- Flexibility
- Open-Source
- Quality
- Rock-Solid-Stable in runtime and housing
- Scalable

*****
Media
*****
We put Media-files to [Seafile](https://tinycloud.lilbits.de/Media)

***
Buy
***
- Get a custom-build set: 6410€ (without audio-hardware)
- Get it on Kickstarter: depends on community
- Build your own: ~1720€ (without audio-hardware)
- Buy audio-hardware: starts from 750€ (see [parts](https://doc.orbitalwaves.net/assembly/parts.html))
- Maintenance and Service Subscriptions: 100€ / Month

****
Rent
****
- Rent A³ Pandemic set 320-640€ per day (without speakers)
- Rent A³ Speakers set  320-60000€ per Event (without show)
- Rent A³ Show 20000-350000€

***
Git
***
- A³ Pandemic Mainrepo: https://github.com/ambisonics-audio-association/Ambijockey
- A³ Motion UI-repo: https://github.com/ambisonics-audio-association/MotionControllerUI

*******
Support
*******
- Help-desk
- Community

*******
Contact
*******
- [contact@orbitalwaves.net](mailto:contact@orbitalwaves.net)
- [mattermost](https://talk.lilbits.de/ambisonics)

********
In depth
********

.. toctree::
   :maxdepth: 1
   :caption: Usermanual:

   user/core
   user/mic
   user/moc

.. toctree::
   :maxdepth: 1
   :caption: Configuration:

   configuration/configuration
   configuration/core
   configuration/mic
   configuration/moc
   
.. toctree::
   :maxdepth: 1
   :caption: Development
   
   development/development
   development/core
   development/mic
   development/moc
   development/osc
   development/flashTeensy

.. toctree::
   :maxdepth: 1
   :caption: Assembly
   
   assembly/assembly
   assembly/core
   assembly/mic
   assembly/moc
   assembly/parts
   assembly/imaging   
