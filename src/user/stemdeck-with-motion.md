# StemDeck × A³ Motion

(stemdeck-with-motion-at-a-glance)=

## At a glance

A normal DJ set reaches the room as one stereo mix. Move it, and the whole
track moves — kick, bassline, vocal and all, like a speaker on a trolley.

[StemDeck](stemdeck.md) plays each track as **four stems** — drums, bass,
other, vocals — and sends each stem on its own output. In the A³ setup those
four outputs land on **A³ Core's four channels**, the same four channels
[A³ Motion](a3motion.md) moves. So each part of the track gets its own place
and its own path through the room:

- the **drums** can hold the floor while
- the **vocal** circles overhead,
- the **pads and synths** breathe from wall to wall, and
- the **bass** stays put, where bass is happiest.

And it all runs **in time with the track**. StemDeck can be the tempo master
of the whole system: its playing deck's beat goes out on Pro DJ Link, the
[Beat Analyzer](beat-analyzer.md) follows it, and A³ Motion follows the Beat
Analyzer. The movements are counted in bars off that beat, so a shape that
takes four bars lands on the one of the track StemDeck is playing — no
tapping, no CDJs needed.

Nothing here is a special mode. It is StemDeck, the Beat Analyzer and A³
Motion doing what each already does, wired together. This page is the wiring,
and a first set to try it with.

<!-- GIF: the room view on A³ Motion with a StemDeck track playing: four blobs on four different clips, and StemDeck's four stem meters beside it (split screen or two recordings side by side) -->

(stemdeck-with-motion-why)=

## Why it works so well

- **One part at a time, not the whole track.** A moving full mix smears; a
  moving vocal over a drum kit that stays put is a *gesture*. The ear can
  follow one thing flying about while the rest keeps its footing.
- **A stem gets a channel of its own.** Bus N arrives on A³ channel N, and
  you choose which stem is on which bus — on the desk, or with the bus
  switches in StemDeck's mixer. A set made by StemDeck's
  [stem creator](#stemdeck-stem-creator) is always drums, bass, other, vocals
  as stems 1–4, so the same choice fits every track you split.
- **One clock, from the music itself.** With StemDeck as master, the beat
  A³ Motion follows is the beat of the deck that is playing, tempo fader
  included. Nudge the tempo on StemDeck and the room speeds up with it.
- **The channel is the part, not the deck.** A channel plays one stem at a
  time, from either deck. Keep the drums on channel 1 and channel 1 is "the
  drums" whichever deck they come from: push deck 2's drums onto channel 1
  and its movement carries on with the next track.

(stemdeck-with-motion-map)=

## Which stem goes where

StemDeck plays into A³ Core either on the Core itself — the usual case,
where it fills the Core's workspace STEMDECK (number 2) — or from another
machine over the network. The ports, the network channels and the REAPER
inputs they arrive on are all on the
{doc}`Patchbay page <../ressources/patchbay>`. Either way the REAPER project
spreads them over the four channels the same way:

| StemDeck output | Arrives on | What is on it |
| :--- | :--- | :--- |
| `deck1_L`, `deck1_R` (bus 1) | **channel 1** | every stem switched to **1** |
| `deck2_L`, `deck2_R` (bus 2) | **channel 2** | every stem switched to **2** |
| `deck3_L`, `deck3_R` (bus 3) | **channel 3** | every stem switched to **3** |
| `deck4_L`, `deck4_R` (bus 4) | **channel 4** | every stem switched to **4** |
| `aux_L`, `aux_R` | the **Return** track, set by the **RET** pot | every stem switched to **A** (AUX) |
| `phones_L`, `phones_R` | StemDeck's own headphone bus (REAPER inputs 23–24), heard on the cue side | every stem on **C**, every deck on CUE |

From there a stem is just another source on its channel: it goes through
that channel's strip — gain, EQ and fader on the A³ Mixer, 3d, freq and Q on
A³ Motion — exactly like a deck plugged into the desk.

A few things follow from that:

- **A stem replaces the analog input.** While a stem is on a channel, Core
  shuts that channel's analog input (REAPER's `analog` track send to
  `N-input`); with no stem there, the analog input plays. A CDJ on channel 1
  is silent while a stem is on channel 1, and the stem moves through the same
  strip. You choose it on the desk: turn the channel's encoder to the stem
  and push (see {ref}`the desk's input selectors <a3mix-displays>`).
- **Nothing is on a channel at first.** StemDeck starts with every stem on
  AUX only (see [Where the stems start](#stemdeck-start-buses)); a stem
  reaches a channel when you push it there. A set with its own stem names
  (`DUB`, `KICK`, `PADS`, `PERC`, …) numbers its stems in the order its
  endings sort — see [Stem sets](#stemdeck-stem-sets).
- **A stem plays on every bus that is lit.** Each stem in StemDeck's mixer
  has six switches, **1 2 3 / 4 A C**. A stem on a number is on that A³
  channel and moves with it; a stem on **A** (AUX) only is on the Return
  track, whose level is the RET pot (on A³ Motion's MIXER, and the desk's aux
  return), and does not move. Pushing a stem onto a channel from the desk puts
  it on that number and takes its AUX away; what the desk enforces is on
  {ref}`StemDeck's remote control <stemdeck-remote>`.

(stemdeck-with-motion-setup)=

## Setting it up

You need StemDeck, A³ Core with the Beat Analyzer, and A³ Motion — the A³
Mixer is welcome but optional, since A³ Motion's MIXER page has the same
controls.

### 1. The audio: StemDeck into A³ Core

**StemDeck on the Core machine itself?** Then there is nothing to wire: the
a3-core package's patchbay connects its outputs to REAPER (see the
{doc}`Patchbay page <../ressources/patchbay>`), and the user service keeps it
running on workspace 2 (see
[Always running on the Core](#stemdeck-on-the-core)). Go on with the clock.

**On A³ Core**, for a StemDeck on another machine, there is nothing to do
either: the a3-core package runs zita-n2j and its patchbay wires it into
REAPER (channels and inputs: see the Patchbay page). The Core's zita units take their address
and port from `~/.config/a3/osc.env`, which the package writes from
`a3-osc.json` (`a3-osc-render user`).

**On the StemDeck machine**, send the ten outputs to the Core over the
network. StemDeck's repository ships two systemd user services for this,
under `.config/systemd/user/`:

- `zita-j2n.service` sends StemDeck's 10 channels to the Core, to the
  listener `zita-n2j.audio` of the a3-core package's zita-n2j;
- `zita-n2j.service` receives 2 channels back from the Core on
  `radla.zita-n2j`, where the a3-core package's zita-j2n sends REAPER's
  recording bus.

The ports are on {doc}`../ressources/ports`. Both units start zita through
StemDeck's `tools/zita-from-truth.py`, which reads the Core's address and both
ports from the truth StemDeck fetched from Core — see
{ref}`StemDeck on radla <osc-radla>`. Only the channel counts are written in
the units.

Both come back by themselves 2 s after they drop out: zita ends on some
changes to the audio graph, and the units restart it with no limit on how
often.

1. On a StemDeck machine other than the Core, tell StemDeck where Core is
   (`~/.config/a3/core`, see {ref}`StemDeck on radla <osc-radla>`). On the
   Core machine there is nothing to do.
2. Install and start both units, from the StemDeck checkout — or let the
   {doc}`installer <../configuration/install>` do it (role StemDeck on a
   machine without the Core):

   ```sh
   cp .config/systemd/user/zita-*.service ~/.config/systemd/user/
   systemctl --user daemon-reload
   systemctl --user enable --now zita-j2n zita-n2j
   ```

   Run the same lines again to update them after a StemDeck update.
3. Patch StemDeck's outputs into `zita-j2n`'s inputs **in order**:
   `deck1_L` → 1, `deck1_R` → 2, … `aux_R` → 10. StemDeck
   [never connects anything by itself](#stemdeck-audio), and neither do the
   zita units, so this is on you — once, in qjackctl or any patchbay, and
   saved. The two channels arriving at `zita-n2j` are patched by hand the
   same way, wherever you want them.
4. Settle the StemDeck machine's sample rate **before** StemDeck starts.
   StemDeck takes the rate it finds and asks for nothing, on purpose: changing
   a running graph throws zita out — it comes back after 2 s, but the stems
   drop out meanwhile.


### 2. The clock: StemDeck as master

1. In StemDeck, load a set on a deck and **wait for the BPM readout**. A deck
   whose tempo is still being analysed sends no beats.
2. Press **MASTER** on that deck — or just press **PLAY**: with no master
   chosen, the only playing deck becomes master by itself. The top bar reads
   `PIO master: A` (or B).
3. The Beat Analyzer has to be in **clock mode 2** (pioneer). The normal way
   to get there is the next step.
4. On A³ Motion, tap the clock key (top left) until it reads **PIO**. The BPM
   beside it now follows StemDeck's master deck.

StemDeck sends its beat as a **broadcast** into the network of its own
network interface. The Beat Analyzer on A³ Core only hears it if the Core is
in that same network. On one machine it always is; the whole clock chain is
described on the Beat Analyzer page under
{ref}`Playing without CDJs <beat-analyzer-without-cdjs>`.

<!-- IMAGE: StemDeck's top bar with "PIO master: A" next to A³ Motion's clock key reading PIO and the same BPM -->

### 3. The room: 3d up

On A³ Motion, turn **3d** up on the channels you want to move — the pot above
each channel's pads, or **3D** in its field in the channel row. At 3d = 0 a
channel is plain stereo, however busy its blob looks on the screen.

(stemdeck-with-motion-first-set)=

## Your first set

Ten minutes, one track, four stems in four places.

When both run on the Core, they share its one screen. The key at the far
right of each top bar goes to the other — **MOTION** in StemDeck,
**STEMDECK** in A³ Motion, at the same spot in both, so one finger goes back
and forth without moving (see [Over to A³ Motion](#stemdeck-workspaces)).

1. **Load a track in StemDeck.** Pick one you know well, split by StemDeck
   (drums, bass, other, vocals). **Put its four stems on channels 1–4**: on
   the desk, push each channel's stem; without the desk, light bus 1 on the
   drums, 2 on the bass, 3 on other and 4 on the vocals in StemDeck's mixer.
   Check the meters in StemDeck's mixer: all four buses move. On A³ Motion
   the four channel meters move with them.
2. **Make StemDeck the clock** as above: press PLAY, check `PIO master: A`,
   set A³ Motion to **PIO**. The BPM on A³ Motion matches StemDeck's deck.
3. **Load a set on A³ Motion.** FILES › SETS › *Warmup* › **Load**, then close
   FILES. Four calm clips, one per channel — so one per stem.
4. **Bring up the room one part at a time.** Turn 3d up on **channel 4**
   first: the vocal leaves the speakers' stereo image and starts to travel.
   Press channel 4's **Play\|Pause**; the clip starts on the next downbeat.
   Add **channel 3** (the other parts) next, then **channel 1** (drums).
5. **Leave the bass alone** — or at least low and slow. Low frequencies are
   hard to place anyway, and a bassline on a roller coaster mostly makes the
   room feel seasick.
6. **Play the stems with the actions.** Hold **A1** on the vocal channel for
   a gentle lift, let go, and it comes back. In every shipped set the left
   pads push the energy up, the right pads take it down.
7. **Mix the next track in** on StemDeck's other deck, its stems loaded on
   the same channels. Its drums join channel 1, its vocal channel 4 —
   already on the move. When you hand
   MASTER to the new deck, A³ Motion follows its tempo.
8. **Walk the night on.** A6 on a channel cues that channel into the next
   phase (*Groove* after *Warmup*); load the next set in FILES when you want
   all four at once.

<!-- GIF: first set, step 4: channel 4's 3d going up and its Play|Pause starting the clip on the downbeat, the blob leaving the centre -->

<!-- GIF: first set, step 6: holding A1 on channel 4 while channel 1 keeps its own clip, then letting go -->

**Something to try once it runs:** mute a stem in StemDeck (**M**, or keys
`1`–`4` for deck A) and watch its channel meter drop on A³ Motion while the
clip keeps going. Bring it back on the one and it re-enters already in
motion. It's a small thing; the room will think you rehearsed it.

(stemdeck-with-motion-troubleshooting)=

## Troubleshooting

| Symptom | What to do |
| :--- | :--- |
| A³ Motion's channel meters stay still while StemDeck plays | The stems don't reach REAPER. On the Core: are StemDeck's outputs connected to REAPER (see the {doc}`Patchbay page <../ressources/patchbay>`; qjackctl's patchbay). On another machine: are they patched into zita-j2n, and does zita-j2n reach the Core? |
| Drums show up on the vocal channel | The outputs are patched out of order on the StemDeck side. `deck1_L` goes to input 1, `aux_R` to input 10 |
| A stem plays but doesn't move | Its channel's **3d** is down, or its clip isn't playing. Or the stem is only on **A** (AUX): then it is on the Return track, not on a channel |
| A³ Motion doesn't follow StemDeck's tempo | Wait for the deck's BPM; is the deck playing and the top bar saying `PIO master`? Is A³ Motion on **PIO**? Is the Core in the same network as StemDeck? |
| The movements start one beat off the bar | StemDeck counts the bar from the first beat of the track's beat grid. Set CUE on the real first beat of a bar and press **GRID**, then **SNAP** |
| The stems stop after a change in the audio settings | Changing the sample rate or buffer of a running graph throws zita-j2n out; its unit restarts it within about 2 s. If the stems stay away, check `systemctl --user status zita-j2n` on the StemDeck machine, and set the rate before starting next time |
