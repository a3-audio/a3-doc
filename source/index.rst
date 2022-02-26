*******
Welcome
*******

Thanks for your interest. The docs are split in two sections. The first section is the user doc where you will find an overview of basic functions and connections.

The second section is the development doc. You will find all ressources we have. This section is under heavy development and will never be completed.


- `User doc <https://doc.a3-audio.com/user/welcome.html>`_
- `Developer doc <https://doc.a3-audio.com/development/welcome.html>`_

************
Introduction
************
The A³ system is a combination of three devices:

A³ Motion (The Motion Sampler)
##############################
It is a standalone OSC controller which works like a loopstation, but instead of audio it lets you sample and playback motion from a touchscreen.

- `A³ Motion <https://doc.a3-audio.com/user/a3motion.html>`_

A³ Mix (The DJ Mixer)
#####################
It is a standalone OSC controller which behaves like a 4 channel DJ mixer.

- `A³ Mix <https://doc.a3-audio.com/user/a3mix.html>`_

A³ Core (The Sound Server)
##########################
It processes analog audiosignals, calculates 3D sound spheres and is remote controlled by A³ Mix and A³ Motion (or any other OSC controller). A³ Core can handle a wide range of audio hardware to fit environments like Dante, MADI or any class-compliant.

- `A³ Core <https://doc.a3-audio.com/user/a3core.html>`_

Requirements
############
- Soundsystem with at least 4 speakers placed around the venue.
- A venue smaller than 20m diameter. For bigger venues more spheres.

**********
Quickstart
**********
- Plug in your instruments vinyl, cd, daw ..
- Plug in your speakers
- Put speakers in regular circle around center
- Plug CAT cable from A³ Mix and A³ Motion to A³ Core
- Plug in your headphones
- Power on

***********
User Manual
***********

.. toctree::
   :maxdepth: 0
   :caption: A³ Usermanual

   user/welcome
   user/a3motion
   user/a3mix
   user/a3core
   user/advanced

**********************
Developer introduction
**********************

.. toctree::
   :maxdepth: 1
   :caption: A³ Developer

   dev/welcome
   assembly/assembly
   configuration/configuration
   development/development
   development/flashTeensy
   assembly/imaging   
   development/osc
   assembly/parts

.. toctree::
   :maxdepth: 1
   :caption: A³ Mix

   assembly/mic
   configuration/mic
   development/mic
   
.. toctree::
   :maxdepth: 1
   :caption: A³ Motion
   
   assembly/moc
   configuration/moc
   development/moc

.. toctree::
   :maxdepth: 1
   :caption: A³ Core
   
   assembly/core
   configuration/core
   development/core

*******
Contact
*******
- `a3-audio.com <https://a3-audio.com>`_
- `contact@a3-audio.com <mailto:a3-audio.com>`_
- `mattermost <https://talk.lilbits.de/ambisonics>`_
