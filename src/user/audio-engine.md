(audio-engine)=

# The Engine: setting up a room

Before the doors open, once per room: the cables, every speaker checked, a
level the room can never exceed. Then you never touch it during the set.

**The Engine is what you hear**: A³ Core's audio backend. A³ Core is the
hardware, the box everything plugs into; the Engine is the software on it.
Everything you play on the desk, every stem and every echo goes through it, and it feeds each speaker exactly its share of
the room. For what it does to the sound, read [How A³ sounds](how-it-sounds.md) first.

## What it does, in short

- It takes the **inputs**: the stereo inputs of the audio interface (CDJs,
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

The Engine is part of the program `a3-core` on A³ Core. It starts by itself
with the Core; there is nothing to switch on.

(audio-engine-window)=

## The Core window

The engine's settings live in the **Core window**: on A³ Core's own screen
it is the workspace **ENGINE** (3); on a laptop, run `a3-core`. Closing the
window never stops the sound.

```{figure} pics_user/a3-signal-flow.svg
:alt: The A³ signal flow: players and StemDecks, the desk, the 3D placement, the room mix with the delay, the four outputs MASTER, BOOTH, REC, PHONES and where each is heard
:width: 70%

What the engine does, from the inputs to the speakers.
```

The pages along the top, one per job:

| Page | What it is for | Do you need it? |
| :--- | :--- | :--- |
| **AUDIO** | the sound device: its sample rate and buffer, and the estimated delay from input to output | rarely. On the rig the audio server decides; the page only shows it |
| **CHANNELS** | how many desk channels and how many StemDecks (A, B, C, D, …) the engine runs | only when you add a deck |
| **ZONES** | which speaker layout the PA (MAIN) and the BOOTH use, and an optional EQ for your headphone model (PHONES) | yes, in a new room |
| **SPEAKERS** | the speakers of one zone: where each one stands, a test noise for each, and which output is the sub | yes, in a new room |
| **I/O** | the cables: what feeds each channel (INPUT), and which interface output each zone uses (OUTPUT) | yes, once per audio interface |
| **CALIBRATION** | the level of each zone: MAIN, BOOTH, PHONES | yes, in a new room |
| **FILTER** | the sound of the desk's FX filter: SVF (clean) or Ladder (warmer, it bites) | when you like |
| **STATUS** | what runs now: the engine, the connection to the rest of the system, the load, what is missing | when something is silent |

Below them, **OSC MONITOR** shows what the devices say to each other
({ref}`A³ Core › The window <core-window>`).

**Nothing changes until you press Save.** The bar at the bottom says
*not saved* while you have a change waiting. **Save** restarts the engine with
the new setting: the sound drops for a moment and fades back in over a
second. So set up before the doors open, not during the set. If the new
setting does not work, the old one comes back and the window says why. The
**FILTER** page is the one exception: it acts at once.

(audio-engine-setup)=

## Setting up a room: three steps

```{warning}
**Start quiet.** Turn the desk's **MASTER** and **BOOTH** down before you
begin, and bring them up slowly. A wrong cable or a wrong trim can be loud.
```

### 1. The cables: I/O

Open **I/O**.

- **INPUT**: for each desk channel, which interface input is its left and
  its right. Your CDJ on inputs 1 and 2 belongs to channel 1, say. Below that,
  for each deck, where it comes from: **Local StemDeck** (on this computer)
  or **AES67 stream** (from another computer on the network).
- **OUTPUT**: for each zone (**MAIN**, **BOOTH**, **PHONES**, **REC**), which
  interface output each of its channels goes to. MAIN has the sub first, then
  the tops. An output that another channel already uses is marked.

Press **Save**. A shipped A³ Core comes with this already done for its own
interface; see {ref}`the I/O map <audio-engine-io>` for what it connects.

### 2. The speakers: ZONES and SPEAKERS

Open **ZONES** and pick the layout of MAIN and of BOOTH. The shipped one is a
square of four tops with one sub (4.1). Pick a layout in the list to see its
speakers.

Then open **SPEAKERS** and choose the zone. The table lists each speaker:
its output channel and its direction (**azimuth**: the angle around you, 0 is
straight ahead; **elevation**: the angle up). Now check them one by one:

1. Bring **MASTER** (for MAIN) or **BOOTH** up a little: the test noise
   goes through that knob.
2. Press a speaker's **NOISE** button: one second of pink noise comes out of
   *that* speaker. Is it the right box, in the right place?
3. To hear the noise *from that speaker's direction* through the whole
   layout, hold **Alt** on a keyboard and press **NOISE**. It should sound
   from where the speaker stands. This check needs a keyboard plugged into
   the Core; on the touch screen alone there is no way to do it yet.

If your room is different, change the table (where the speakers stand, which
output is the sub, the crossover to the sub), press **SAVE TO ZONE**, then
**Save**. Your layout is saved as a variant of your own; the shipped files
stay as they are.

### 3. The level: CALIBRATION

Open **CALIBRATION**. Each zone has a trim, from −90 to +6 dB: the level
the zone has with its desk knob fully open. Moving a slider only *proposes* a
value; a question names the old and the new value before anything changes.

- Play a track, desk knobs fully open, and raise the trim until the room is
  as loud as it may ever get. Then the desk can never go louder than that.
- The shipped MAIN and BOOTH trims are low on purpose (−30.88 dB).
- A zone without a trim stays silent.

That is it. From now on the engine starts with these settings every time.

## In depth

The signal path, the shipped I/O map, how decks arrive and how to start the
Engine by hand are in the configuration section:
{doc}`The audio engine in depth <../configuration/core-engine>`.
