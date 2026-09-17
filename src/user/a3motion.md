# A³ Motion

- [A³ Motion Repository](https://github.com/a3-audio/a3-motion)
- Standalone OSC controller
- 7" full-color capacitive multi-touch display

A³ Motion records and plays back **movement trajectories**: where each of the
four channels sits in the room, and how it travels through it. It makes no
sound of its own — it sends positions to A³ Core over OSC, and Core moves the
sound. A clip is one figure together with every value it is played with, and a
set is which clip sits in which slot.

Playback follows a beat clock, so a figure that takes four bars keeps taking
four bars when the tempo changes.

![A³ Motion](pics_user/a3-motion-icon_light.png)

## The panel

Every control has one job and keeps it whatever is on screen. A knob that
means something different depending on the page is a knob you have to look at.

| Control | What it does |
| :--- | :--- |
| Upper encoder, per channel | **freq** — that channel's filter frequency |
| Lower encoder, per channel | **Q** — that channel's filter resonance |
| Potentiometer, per channel | **3d** — crossfades the channel between its stereo and its multichannel encoder in A³ Core |
| Pads, four per channel | Play\|Pause, Stop, Action, Settings for that channel's slot |
| Function keys, six | TAP, clock, REC, recmode, MENU, SHIFT |
| Touchscreen | everything else |

Pressing an encoder does nothing. The six function keys sit as a **vertical
column at each end of the panel**, mirrored so either hand reaches them; a key
is down while either side is down.

**The touchscreen is not optional.** Since the touch rework the encoders no
longer navigate anything, so with the screen out the device cannot be driven.
That trade was made knowingly.

## [3] DISPLAY
- This full-color multi-touch display shows information relevant to A³Motion’s current operation. Touch the display (and use the hardware controls) to control the A3Motion interface. See Operating Instrucions to learn how to use some basic functions

![The A³ Motion display in operation](pics_user/a3-motion-ui-display-v03.png)

The screen has three bands. Along the top sits the status bar, and it is
deliberately almost empty: the current tempo on the left, the beat grid in the
middle — it fills as the bar runs — and the MIX key on the right. It carried
nine level meters for two days and they made the one band that is always in
view the busiest thing on the screen.

The middle band is the room seen from straight above, with you — the listener —
in the middle at ear height. Each channel is a coloured blob sitting where its
sound is; it swells and throws sparks with that channel's input level, and
dragging it moves the sound. A playing clip draws its trajectory as a braid of
three strands of plasma with the blob travelling inside it. What runs behind
the sphere is drawn darker than what runs in front of it.

At the four corners stand the speakers, each a tower of three tops over four
subs, on a dark floor below your feet. Lightning comes out of the tops and
flickers across the floor towards the middle: thicker, and more of it, on the
speaker that is playing loudest, and none at all when the room is silent. The
subs throw ball lightning with the bass. The field around the sphere shows
where the energy in the room is coming from.

The small ball in the top right corner is the view. Drag on it to tilt and
turn the room; a double tap on it takes the view back to straight above.

The four coloured cells at the left of the tab row are the channels. Each
carries a **signal dot** in its top right corner: the channel's input level,
in the same green / yellow / red the meters use, brighter the louder it is —
and **gone entirely when the channel is silent.**

![The four channel keys, three with signal and one without](pics_user/a3-motion-signal-dots.png)

That is the question you actually have mid-set — *is this channel making
sound, and roughly how hot* — asked where the answer belongs, on the channel
itself. For reading a level properly, the MIX page has the full meters.

The bottom band holds the settings of the selected clip, framed in that
channel's colour: its shape, how it is mapped in elevation, how it moves in
time — speed, direction, what happens at the end, and the fade that closes the
loop — and its filter. The narrow strip on the right is global rather than
per-channel and carries the recording mode.
## The tab row

The tabs pick what the bottom band shows. The four coloured cells to their
left are the channels; tapping one selects the clip the settings describe.

| Tab | What it is |
| :--- | :--- |
| **CLIP** | the selected clip's settings — shape, elevation, motion |
| **REC** | the same three sections, with the Shape card turned over to record a take |
| **ACTION** | what the Action pad fires besides playing |
| **PADS** | the panel's pads on screen, reachable without the hardware |
| **MIX** | a full channel strip for all four channels |
| **FILES** | the library: clips, shapes, actions and sets |

Beside the tabs sit the two **slot keys**. They are keys rather than a
heading: a heading saying which clip you are looking at and a control changing
it want the same place.

## CLIP — the settings of one clip

Three cards, each with a **lock** at the right end of its title row. A locked
section is one nothing writes over — step through clips with Elevation held
and every figure arrives in the room you are already in. The lock belongs to
the device, not to the clip: it is a stance you take while playing and drop
again, so it travels in neither the clip file nor the set.

A **double tap on a knob** puts it back to the middle of its range. Only
knobs — a list has no middle.

### Shape — which figure, and how fast

| Control | What it does |
| :--- | :--- |
| picture | the figure the sound traces. Scroll it with a thumb to step through the shapes; **swapping the figure keeps the values** |
| clip field | which settings preset is loaded. Its own list, scrolled separately — one scroller over both could quietly apply somebody's preset while you were choosing a shape |
| drift dot | warning-coloured, in the clip field: the values have been turned since they were loaded and something is waiting to be written |
| four speed keys | tap to play at that speed. **Drag a key to give that key another speed**, out of the whole range, applied straight away. The key keeps it, so a speed the four do not yet name is reached once and found again next time |
| `dir` | **Fwd** or **Rev** — which way the figure is travelled |
| `end` | what happens when a pass runs out: **Loop**, **Stop**, **Paus**, **Bnce**, **Rnd** |

**Stop and Paus are two different things.** Stop returns to the beginning of
the take, whichever way it was running, so the next start is visibly a start.
Paus stands still wherever the playhead landed.

### Elevation — how the flat figure is wrapped onto the sphere

The recorded figure is a flat disc. Elevation decides how that disc is laid
over the room: the radius becomes the angular distance from a base direction,
and the disc's angle becomes the bearing around it. The figure is a cap
centred on the base and grows out of it in every direction.

| Control | What it does |
| :--- | :--- |
| the graphic | drag the chord to set the **base** — the direction the figure is centred on |
| `reach` | how far down the sphere the figure's outer edge lands |
| `sway` | sweeps the base up and down, in bars off the tempo clock. The stretch it covers is filled in on the graphic |
| `clip-top` | a ceiling: a point pushed past it keeps its bearing and gives up only its height, so a figure reaching into the ceiling travels *around* it rather than heaping on one spot |
| `clip-bot` | the same for the floor |
| `pole` | mirrors the figure to the southern hemisphere |
| `flat` | ignores elevation and holds the figure at one height |

### Motion — what is done to the figure while it plays

Five rows, and each is a standing value next to the movement that works on
it. Everything that moves on its own is counted in **bars off the tempo
clock**, never in seconds, so a cycle comes back to where it started on a bar
line instead of drifting through the loop underneath it.

| Pair | Standing value | Its movement |
| :--- | :--- | :--- |
| 1 | `rot` — turn the whole figure around the vertical axis | `spin` — keep turning, signed for direction |
| 2 | `reach` — see Elevation | `swell` — sweep the reach out and back |
| 3 | `sqzX` — squeeze front-to-back | `strX` — sweep that squeeze |
| 4 | `sqzY` — squeeze left-to-right | `strY` — sweep that squeeze |
| 5 | `fade` — how long the take's closing move lasts | `bias` — what happens to what a take never wrote |

**`rot` is a closed ring**, the only control in the bar that is: a rotation
comes round to itself, so a scale with two ends and a dead zone between them
would read as an amount rather than as a position. Its pointer says where your
hand left it; the blue says where the spin is holding it now.

**A spin that is not running turns nothing.** Turned off, it stands still at
whatever angle it stopped at rather than counting on invisibly.

The two squeezes are bipolar with their middle at zero and multiply their axis
by 2^value — half at one end, double at the other, and the middle of the
travel is the take as recorded. **The squeeze happens before the turn**, so
the ellipse belongs to the figure and travels with it.

### The accent

Not a movement: it rises while the **ACT pad is held**, stays up as long as it
is held, and falls when you let go. The hold is the finger, which is why there
is no sustain control — on a pad, how long a thing lasts is a gesture.

| Control | What it does |
| :--- | :--- |
| `atk` | how long it takes to rise, in bars |
| `dec` | how long it takes to fall |
| `max` | the ceiling it rises towards. A ceiling set *under* the floor leaves the floor alone |
| `act` | **1shot** or **Hold** — what the Action key does |

What it drives is the channel's **3d**, and only upwards: the knob shows the
floor you set, and the arc from there to where the accent has taken it is
filled in. When the decay runs out, the clip does what its `end` says — and
only on that edge, once.

## REC — making a take

Record is a **toggle wherever it is pressed**: the panel key, the bar's key,
the tab.

1. Choose a length — eight keys, from a quarter bar to 32.
2. Press REC, or hold the panel's REC and press a slot's Play\|Pause pad.
3. Drag the blob across the sphere. The trajectory appears as you play it in.
4. The pass ends when the length is reached.

Only the Shape card turns over for this — you are still looking at the
elevation and the motion the take will get. `fade` closes the join where the
take meets itself.

The **rec mode** says how much of an old take a pass destroys, and it carries
that on its own colour:

| Mode | What it destroys |
| :--- | :--- |
| **Touch** | mends the corner you touch and leaves the rest |
| **Latch** | holds on after the finger goes |
| **Write** | clears the pass whether you touched it or not |

## PADS

The panel's pads on screen, because a plain build has no panel and without
pads such a build cannot start a single clip. Channels across, slots down, and
where they meet one clip with its four pads: **play beside stop on top, action
beside settings below**.

Nothing is decided here: a press goes out as the same `(channel, pad)` the
hardware sends, and a pad's colour comes in already worked out by the one loop
that also writes the panel's LEDs — so empty, idle, armed and running look on
screen exactly as they look on the hardware.

**When a pad takes effect:**

| Pad | When |
| :--- | :--- |
| Play\|Pause | the **next beat**, starting and stopping alike |
| Stop | **now** |
| Action | **now** |
| Shift + Action | now, in preview, for as long as it is held |

The bar is the take's unit, but it is the wrong unit for a press: a bar is up
to a metre's worth of beats away, and a clip that starts that long after the
finger reads as a button that did not work. Stop is the way out of something
going wrong, and a way out that waits for the music is not one.

### MIX

A software mixer for the four channels, sending the same messages the A³
Mixer sends. Anything you turn here, the desk sees too — and the other way
round.

![The MIX page](pics_user/a3-motion-ui-mix.png)

The knobs show what is actually set, not what this device last did: A³ Core
passes on whatever REAPER reports, so a hand on the desk or in REAPER moves
them here too, and a restart mid-evening brings them back as they stand. That
holds for the whole mixer — the channel strips, the master column and the
filter — and for the PFL and FX keys, which light to match what A³ Core has
rather than what was last pressed here.

Tapping **MIX** in the status bar opens the whole thing at once:

![The mixer, showing the room as it actually stands](pics_user/a3-motion-ui-mixer-overlay.png)

Per channel: **GAIN**, the three EQ bands **HIGH / MID / LOW**, **VOL**, and
**SEND** — how much of that channel goes to the FX bus, where the delay that
follows the beat sits. Below them the **PFL** and **FX** buttons. A second
page holds the master, booth and headphone levels and the one filter shared by
all four channels.

**SEND comes up shut, and a double tap takes it back there.** It is the one
control on the page you may want to get rid of in a single gesture,
mid-transition, without looking — and the one whose starting position can be
right rather than guessed.
Nothing else on the MIX page responds to a double tap: a gain that snaps to a
default in the middle of a set is a channel that jumps in the room.

On the narrow strip to the right — `3d`, `freq` and `Q` per channel — a double
tap works too: `3d` and `freq` go back to twelve o'clock, `Q` goes back to
closed.

## When the device comes up

A³ Motion asks A³ Core where each sound already is, and adopts the answer
before it says anything itself. So switching the device on, or restarting it
mid-evening, does not move the room: the blobs appear where the sound
actually is, and the pots stand where they stood.

Loading a **set** is the other way round — that is an explicit act, and the
set wins.

## FILES — the library

Two tabs, **CLIPS** and **SVG**, and they are two different things: choosing a
clip fills the slot with a figure *and* its values; choosing a shape swaps only
the figure and leaves the values where your hand put them.

A **clip file is the SVG**. There is no separate settings file — the trajectory
and every value the clip settings hold live in one file, which is why the
browser's library list *is* the list of clips. A **set** is the layer above:
which clip sits in which of the eight slots, plus what belongs to the device
rather than to a clip.

Five keys, the same words on every tab:

| Key | What it does |
| :--- | :--- |
| **Filter** | steps `All → User → System` and wears the state it is in, not the one the next press would bring |
| **Rename** | typed into the row itself. Enter or "Keep" settles it, Escape drops it |
| **Save** | writes what is on show back over the file it came from |
| **Save as** | writes it to a new one, and opens that row for typing |
| **Delete** | asks twice — the key says "Delete", then "Sure?" |

**Save and Save as are two keys rather than one and a modifier**: which of the
two you meant is the whole question, and a modifier makes it something you find
out afterwards.

**Deleting deliberately does less.** A set's file goes and what is loaded stays
loaded; a clip's files go and the sets that named it are left alone. Everything
playing goes on playing — the pattern is in memory, and a file going is not a
reason to stop the room.

## The global strip

To the right of the clip settings, on every page, because these belong to the
device rather than to the clip.

| Control | What it does |
| :--- | :--- |
| the 4×3 grid | **3d**, **freq**, **Q** per channel, in the channel's colour. Drag a cell |
| **recmode** | steps Touch → Latch → Write, coloured by how much it destroys |
| **clock** | steps INT → EXT → PIO, and writes the mode in that mode's colour |
| **MENU** | opens the settings, one level at a time |
| **REC** | starts a take on the clip the bar is showing, and ends a running one |
| **TAP** | tap the tempo. Breathes with the beat |
| **SHIFT** | held, not latched — Shift+Action previews for as long as it is down |

The rec mode and clock keys **never light**: they carry a value, the value is
written on them, and a wash that comes and goes says the same thing again in
grey.

**The status bar shows the tempo and nothing else**, in the clock's colour.
Which clock it is comes from the clock key, under your hand; a third place
saying it was a third place to keep in step.

### Clock modes

| Mode | Where the tempo comes from |
| :--- | :--- |
| **INT** | this device. The tap key sets it, and `/beat` goes out |
| **EXT** | an incoming `/beat` over OSC — the beat-analyzer |
| **PIO** | Pioneer Pro DJ Link |

Clock mode is deliberately **not** in the menu: a setting in two places is a
setting whose location you have to remember. It is also not saved in a set —
it depends on what is plugged into the switch at the venue.

## The menu

Opened with MENU. The strips left and right of the panel are drag zones, not
margins: dragging in the **left** one walks the list, dragging in the **right**
one arms a row and changes its value. That is the encoder's two levels laid out
as two *places* rather than as a press that switches between them.

The list scrolls the way it does on a phone — a drag moves the page in your
finger's direction — and a row is chosen by touching it.

| Page | What it holds |
| :--- | :--- |
| **Skin** | which skin is loaded |
| **Skin Editor** | every value a skin holds, grouped by what it is |
| **Network** | the OSC hosts, ports and addresses |
| **Button LEDs** | the panel's key colours |
| **Pattern Folder** | where clips and sets are read from |
| **Sphere in Menu** | whether the sphere keeps drawing behind the menu |

**A double tap on any row calls up the keyboard**, so a value finer than a
drag can reach is typed. Two-finger scrolling and the arrow keys both walk the
list.

Getting out: **back** closes one level, **close** gets you out of all of it at
once, however deep. Escape does not quit — on a device standing in a booth
with a keyboard plugged into it, that is one stray key from ending the set.

## When the device comes up

A³ Motion asks A³ Core where each sound already is, and adopts the answer
before it says anything itself. So switching the device on, or restarting it
mid-evening, does not move the room: the blobs appear where the sound actually
is, and the pots stand where they stood.

Loading a **set** is the other way round — that is an explicit act, and the set
wins. What was running runs again, from the top, on the next **downbeat**:
eight clips starting together is the whole point of a set, and together is what
a downbeat gives you.

## Specs

Current revision, V03:

- PoE, 31.5 W max
- Raspberry Pi 4B running the touchscreen UI
- ESP32-S3 (`esp32-s3-devkitc-1-n16r8`) for the panel's buttons, encoders,
  pots and LEDs, over a binary poll-frame protocol on USB serial
- 7" capacitive multi-touch display
- A³ Motion Buttonmatrix PCB V03, A³ Motion Mainboard PCB V03

Earlier revisions are listed under
[Configuration](https://a3-audio.github.io/a3-doc/configuration/moc.html).
