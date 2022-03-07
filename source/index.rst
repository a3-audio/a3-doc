************
Introduction
************

Thanks for your interest in the A³ system.

These docs are split in two sections:

- The first section is the `User <https://doc.a3-audio.com/user/user.html>`_ section, where you will find an overview of basic functions and connections.

- The second section is the developer section wich is under heavy development and will probably never be completed. The developer section is splitted in three subsections: `Developer <https://doc.a3-audio.com/development/developer.html>`_ (about code), `Assembly <https://doc.a3-audio.com/development/assembly.html>`_ (about hardware), and `Configuration <https://doc.a3-audio.com/development/configuration.html>`_ (setup operation system).

**********
What it is
**********
The A³ system is made for 3D Audio live interaction. It is a combination of three devices:

A³ Motion (The Motion Sampler)
##############################

`A³ Motion <https://doc.a3-audio.com/user/a3motion.html>`_ is a standalone OSC controller which works like a loopstation, but instead of audio it lets you sample and playback motion from a touchscreen.

.. image:: pics_landing/a3_system_symbol_moc.png
   :height: 500px
   :width: 500 px
   :scale: 50 %

A³ Mix (The DJ Mixer)
#####################
`A³ Mix <https://doc.a3-audio.com/user/a3mix.html>`_ is a standalone OSC controller which behaves like a 4 channel DJ mixer.

.. image:: pics_landing/a3_system_symbol_mix.png
   :height: 500px
   :width: 500 px
   :scale: 50 %

A³ Core (The Sound Server)
##########################
`A³ Core <https://doc.a3-audio.com/user/a3core.html>`_  processes analog audiosignals, calculates 3D sound spheres and is remote controlled by A³ Mix and A³ Motion (or any other OSC controller). A³ Core can handle a wide range of audio hardware to fit environments like Dante, MADI or any class-compliant.

.. image:: pics_landing/a3_system_symbol_core.png
   :height: 500px
   :width: 500 px
   :scale: 50 %

************
Requirements
************
- PA soundsystem with at least 4 speakers
- All speaker must be placed in a most chubbiest spherical installation around listening area. Electronic corrections are possible for closer speakers.
- A venue smaller than 18m diameter. For bigger venues more speaker spheres are required

********
Optional
********
- Booth soundsystem with at least 4 speakers placed around the DJ desk

**********
Quickstart
**********
- Plug in your instruments vinyl, cd, daw ..
- Plug in your speakers
- Put speakers in regular circle around center
- Plug CAT cable from A³ Mix and A³ Motion to A³ Core
- Plug in your headphones
- Power on

*******
Contact
*******
- Website: `a3-audio.com <https://a3-audio.com>`_
- E-Mail: `contact@a3-audio.com <mailto:contact@a3-audio.com>`_
- Forum: `3d-audio.io <https://d3-audio.io>`_
- Mattermost: `mattermost <https://talk.lilbits.de/ambisonics>`_

**********
Quicklinks
**********

.. toctree::
   :maxdepth: 1
   :caption: A³ User

   user/user
   user/a3motion
   user/a3mix
   user/a3core
   user/advanced-user

.. toctree::
   :maxdepth: 1
   :caption: A³ Developer

   assembly/assembly
   configuration/configuration
   development/developer

.. toctree::
   :maxdepth: 1

   assembly/moc
   configuration/moc
   development/moc

.. toctree::
   :maxdepth: 1

   assembly/mic
   configuration/mic
   development/mic
   
.. toctree::
   :maxdepth: 1

   assembly/core
   configuration/core
   development/core

.. toctree::
   :maxdepth: 1
   :caption: A³ Ressources

   development/flashTeensy
   development/imaging   
   development/osc
   assembly/parts

