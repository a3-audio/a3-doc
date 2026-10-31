(audio-engine)=

# Speaker Setup

Before the doors open, once per room: the cables, every speaker checked, a
level the room can never exceed. Then you never touch it during the set.

**a3-core is what you hear**: the program on A³ Core, audio backend included.
A³ Core is the hardware, the box everything plugs into; a3-core is the software
on it. Everything you play on the desk, every stem and every echo goes through
it, and it feeds each speaker exactly its share of the room. For what it does
to the sound, read [How A³ sounds](how-it-sounds.md) first.

## What it does, in short

- It takes the **inputs**: the ST inputs of the audio interface (CDJs,
  turntables, a laptop) and the StemDecks, from the Core itself or over the
  network.
- It runs the **four desk channels**: TRIM, EQ, the FX filter, the fader,
  and for an ST channel the band that moves (3d, FREQ, Q).
- It **places every sound in the room** and adds everything into one room
  mix, plus the beat delay and its FX RETURN.
- It **decodes** that mix for each set of speakers (a **zone**): the PA
  (MAIN) and the BOOTH. It folds it into stereo for the headphones (PHONES)
  and the recording (REC).
- It **measures** every meter the desk and A³ Motion show.

a3-core starts by itself with A³ Core; there is nothing to switch on.

(audio-engine-window)=

## The a3-core window

The settings live in the **a3-core window**: on A³ Core's own screen it is the
workspace **ENGINE** (3); on a laptop, run `a3-core`. Closing the window never
stops the sound.

```{figure} pics_user/a3-signal-flow.svg
:alt: The A³ signal flow: players and StemDecks, the desk, the 3D placement, the room mix with the delay, the four outputs MASTER, BOOTH, REC, PHONES and where each is heard
:width: 70%

What a3-core does, from the inputs to the speakers.
```

```{figure} pics_user/a3-core-window-audio.png
:alt: The a3-core window on the rig's screen, page AUDIO: the page keys AUDIO, SPEAKERS, I/O, CALIBRATION, RIG, STATUS and STEMDECK with its ▾ list at the top; the cards DRIVER (PipeWire, 44100 Hz, 128 frames, 2 periods), STEREO CHANNELS AND STEMDECKS (4 and 4, A-D), MEASURE (digital round trip 7.7 ms) and CLOCK (Scarlett to PTP grandmaster); at the bottom KEYS, MONITOR, CLOCK LOCKED in green and Save
:width: 60%

The a3-core window on A³ Core's screen, page AUDIO, during a set.
```

The keys along the top, one page per job:

| Page | What it is for | Do you need it? |
| :--- | :--- | :--- |
| **AUDIO** | the sound device (rate, block, periods), how many ST channels and StemDecks run, the measured round trip, the clock | rarely; when you add a deck |
| **SPEAKERS** | two sub-pages. **SPEAKERS**: the speakers of one zone, where each stands, a test noise for each, the sub. **ZONES**: which layout MAIN and BOOTH use, and an EQ for your headphones (PHONES) | yes, in a new room |
| **I/O** | three sub-pages. **INPUT**: what feeds each channel and each deck. **OUTPUT**: which interface output each zone uses. **DEPARTMENTS**: the light and video desks that hear everything | yes, once per audio interface |
| **CALIBRATION** | the level of each zone (MAIN, BOOTH, PHONES, REC), and the **FILTER** card: the sound of the desk's FX filter | yes, in a new room |
| **RIG** | every program of the rig, with its state; **Start all**, **Stop all** | when something is missing |
| **STATUS** | two sub-pages. **A³ CORE**: what runs now, the load, the clock, the outputs' meters. **ABOUT**: versions, licences, links | when something is silent |

At the top right, **STEMDECK** takes you to StemDeck, and **▾** lists every
workspace with a window on it. It stands where StemDeck has its MOTION key and
A³ Motion its STEMDECK key, so the key under your finger stays put.

The bar at the bottom: **KEYS** brings up the on-screen keyboard; **MONITOR**
adds a second row of keys with what the devices say to each other
({ref}`A³ Core › The window <core-window>`); the **clock** says in one word
whether the sound card and the network run on one clock (green **CLOCK
LOCKED**; red when not); **Save**.

**Nothing changes until you press Save.** The bar says *not saved* while a
change waits. **Save** restarts the audio with the new setting: the sound drops
for a moment and fades back in over a second. So set up before the doors open,
not during the set. If the new setting does not work, the old one comes back
and the window says why. The **FILTER** card is the one exception: it acts at
once.

(audio-engine-setup)=

## Setting up a room: three steps

```{warning}
**Start quiet.** Turn the desk's **MASTER** and **BOOTH** down before you
begin, and bring them up slowly. A wrong cable or a wrong trim can be loud.
```

### 1. The cables: I/O

Open **I/O**.

```{figure} pics_user/a3-core-window-input.png
:alt: The page I/O, sub-page INPUT: a card per channel, CH 1 to CH 4, each with an L and an R dropdown for its interface input, and the DECKS card below
:width: 50%

I/O › INPUT: which interface input feeds each channel's L and R.
```

- **INPUT**: for each desk channel, which interface input is its left and
  its right. Your CDJ on inputs 1 and 2 belongs to channel 1, say. Below that,
  under **DECKS**, where each deck comes from: **Local StemDeck** (on this
  computer) or **AES67 stream** (from another computer on the network).

```{figure} pics_user/a3-core-window-output.png
:alt: The page I/O, sub-page OUTPUT: the cards MAIN (main_sub, main_top_1 to main_top_4), BOOTH (booth_sub, booth_top_1 to 4) and PHONES, each line with a dropdown for the interface output
:width: 50%

I/O › OUTPUT: which interface output each speaker of a zone uses.
```

- **OUTPUT**: for each zone (**MAIN**, **BOOTH**, **PHONES**, **REC**), which
  interface output each of its channels goes to. MAIN has the sub first, then
  the tops. An output that another channel already uses is marked.

Press **Save**. A shipped A³ Core comes with this already done for its own
interface; see {ref}`the I/O map <audio-engine-io>` for what it connects. The
third sub-page, **DEPARTMENTS**, is for light and video desks
({ref}`below <audio-engine-departments>`).

### 2. The speakers: SPEAKERS › ZONES and SPEAKERS

Open **SPEAKERS**, sub-page **ZONES**, and pick the layout of MAIN and of
BOOTH. The shipped one is a square of four tops with one sub (4.1). Below,
the window shows what each zone plays: its decoder, the sub, the crossover and
every speaker's direction. In the bottom bar, **LOAD** applies the chosen
layouts at once; **RENAME** and **DELETE** act on your own variants.

```{figure} pics_user/a3-core-window-zones.png
:alt: The page SPEAKERS, sub-page ZONES: the spatial data card with EDIT SPEAKERS and a dropdown each for MAIN, BOOTH (both Default 4.1) and PHONES (off); below, what MAIN and BOOTH play side by side: decoder, order, weights, sub, crossover and the four speakers with azimuth and elevation
:width: 50%

SPEAKERS › ZONES: the layout of each zone, and what it plays.
```

Then open the sub-page **SPEAKERS** and choose the zone (**MAIN** or
**BOOTH**). The table lists each speaker: its output channel and its direction
(**azimuth**: the angle around you, 0 is straight ahead; **elevation**: the
angle up). Now check them one by one:

```{figure} pics_user/a3-core-window-speakers.png
:alt: The page SPEAKERS, sub-page SPEAKERS for zone MAIN: Sub ch 1, Crossover 150 Hz; the 3D view of the four-speaker layout, the energy map below it, and the loudspeaker table with azimuth, elevation, channel and a Noise button per speaker
:width: 50%

SPEAKERS › SPEAKERS: where each speaker of a zone stands, with a test noise for each.
```

1. Bring **MASTER** (for MAIN) or **BOOTH** up a little: the test noise
   goes through that knob.
2. Press a speaker's **Noise** button: one second of pink noise comes out of
   *that* speaker. Is it the right box, in the right place?
3. To hear the noise *from that speaker's direction* through the whole
   layout, hold **Alt** on a keyboard and press **Noise**. It should sound
   from where the speaker stands. This check needs a keyboard plugged into
   the Core; on the touch screen alone there is no way to do it yet.

If your room is different, change the table (where the speakers stand, which
output is the **Sub**, the **Crossover** to the sub), press **SAVE TO ZONE**,
then **Save**. Your layout is saved as a variant of your own; the shipped files
stay as they are.

### 3. The level: CALIBRATION

Open **CALIBRATION**. Each zone has a trim, from −90 to +6 dB: the level
the zone has with its desk knob fully open. Moving a slider only *proposes* a
value; **Set…** asks, naming the old and the new value, before anything changes.

```{figure} pics_user/a3-core-window-calibration.png
:alt: The page CALIBRATION: a slider, a value and a Set… key each for Main, Booth, Phones and Rec; below, the FILTER card with the keys SVF and LADDER
:width: 50%

CALIBRATION: the level of each zone, and the FILTER card.
```

- Play a track, desk knobs fully open, and raise the trim until the room is
  as loud as it may ever get. Then the desk can never go louder than that.
- The shipped MAIN and BOOTH trims are low on purpose (−30.88 dB).
- A zone without a trim stays silent.

The **FILTER** card below sets the sound of the desk's FX filter: **SVF**
(clean) or **LADDER** (warmer, it bites). It acts at once; try it during a
sound check.

That is it. From now on a3-core starts with these settings every time.

## The other pages

### AUDIO

The page in the first picture. **DRIVER**: the sound device. On the rig
PipeWire runs it at 44.1 kHz; **Block** and **Periods** set the latency, and
**REVERT** goes back to the last working pair. **STEREO CHANNELS AND
STEMDECKS**: how many desk channels and how many StemDecks (A, B, C, D) run;
change it only when you add a deck. **MEASURE**: the round trip from input to
output, measured over a loop you choose on I/O (digital), or once over a test
cable (analog). **CLOCK**: who keeps the time; on the rig the Scarlett, with
the network's PTP clock locked to it, so the decks over the network play on
the same clock as the sound card.

### RIG

```{figure} pics_user/a3-core-window-rig.png
:alt: The page RIG: the MAIN card with the machine's name and the keys Start all and Stop all; the ENTITIES card with a row each for a3-core, Deck A to Deck D, A³ Mixer and A³ Motion, each with a light, its state and its software and firmware versions
:width: 50%

RIG: every program of the rig, its state and its version.
```

One row per program of the rig: a3-core itself, each deck, A³ Mixer and
A³ Motion, each with a light, its state, where it runs and its version. Grey
means it should run and does not. **Start all** and **Stop all** start or stop
the whole rig in its order; **Stop all** asks first.

### STATUS

```{figure} pics_user/a3-core-window-status.png
:alt: The page STATUS, sub-page A³ CORE: the lines Mode, Core, Gate, Audio, Rate from, Bit depth, DSP load, Xruns, Estimated, Measured digital, Measured analog and AES67 latency; the CLOCK card, here red NOT RUNNING; the output meters below
:width: 50%

STATUS › A³ CORE: what runs now. Here on a test machine, where the clock does not run.
```

**A³ CORE** is the first place to look when something is silent: the audio
mode, whether Core is heard, whether the outputs are open (**Gate**), the
load, the xruns, the estimated and measured latency, and the **CLOCK** card
(green when locked, red when not). The meters below show the outputs as they
leave.

```{figure} pics_user/a3-core-window-about.png
:alt: The page STATUS, sub-page ABOUT: A³ Spatial DJ setup with the links Documentation, Website and Source and the copyright line; the card PUBLISHED with the versions; the licences
:width: 50%

STATUS › ABOUT: versions, licences and links.
```

**ABOUT** says which version every part of the system runs, under which
licence, and links to these docs, the website and the source.

(audio-engine-departments)=

### I/O › DEPARTMENTS

```{figure} pics_user/a3-core-window-departments.png
:alt: The page I/O, sub-page DEPARTMENTS: an empty list with the columns NAME, HOST, PORT, ON and STATUS, and the keys ADD and SAVE LIST
:width: 50%

I/O › DEPARTMENTS: the light and video desks that hear every A³ message.
```

A light or video desk can hear every move you make: **ADD**, then its name,
host and port, **SAVE LIST**. It applies at once, and each row says whether
messages go out. Details: {ref}`Adding a department <core-subscriber>`.

## In depth

The signal path, the shipped I/O map, how decks arrive and how to start
a3-core by hand are in the configuration section:
{doc}`a3-core in depth <../configuration/core-engine>`.
