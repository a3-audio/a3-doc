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
- **The stems line up with the channels.** A set made by StemDeck's
  [stem creator](#stemdeck-stem-creator) puts drums on bus 1, bass on 2,
  other on 3 and vocals on 4 — and bus N arrives on A³ channel N. Every
  track you split lands the same way round, so a clip on channel 4 is
  *always* moving the vocal.
- **One clock, from the music itself.** With StemDeck as master, the beat
  A³ Motion follows is the beat of the deck that is playing, tempo fader
  included. Nudge the tempo on StemDeck and the room speeds up with it.
- **Both decks, one channel per stem.** Each bus carries stem N of **deck A
  and deck B** together, so channel 1 is "the drums" whichever deck they come
  from. Blend from one track into the next and the movements carry on: the
  channel is the part, not the deck.

(stemdeck-with-motion-map)=

## Which stem goes where

StemDeck's ten outputs travel to A³ Core over the network as ten audio
channels (zita-j2n on the StemDeck side, zita-n2j on the Core). A³ Core's
patchbay wires the ten network channels into REAPER's inputs 11–20, and the
REAPER project spreads them over the four channels:

| StemDeck output | Network channels | REAPER inputs | Arrives on | In a set made by StemDeck |
| :--- | :---: | :---: | :--- | :--- |
| `deck1_L`, `deck1_R` (bus 1) | 1–2 | 11–12 | **channel 1** | drums |
| `deck2_L`, `deck2_R` (bus 2) | 3–4 | 13–14 | **channel 2** | bass |
| `deck3_L`, `deck3_R` (bus 3) | 5–6 | 15–16 | **channel 3** | other |
| `deck4_L`, `deck4_R` (bus 4) | 7–8 | 17–18 | **channel 4** | vocals |
| `aux_L`, `aux_R` | 9–10 | 19–20 | the **Return** track, set by the **RET** pot | every stem switched to **AUX** |

From there a stem is just another source on its channel: it goes through
that channel's strip — gain, EQ and fader on the A³ Mixer, 3d, freq and Q on
A³ Motion — exactly like a deck plugged into the desk.

A few things follow from that:

- **A stem shares its channel with the analog input.** The network stems
  arrive *beside* that channel's analog input, not instead of it. A CDJ on
  channel 1 and StemDeck's drums play through the same strip and move
  together. Mix accordingly, or keep the analog deck quiet.
- **A set with its own stem names** (`DUB`, `KICK`, `PADS`, `PERC`, …) goes
  on the buses in the order its endings sort — see
  [Stem sets](#stemdeck-stem-sets). Which part lands on which channel is
  whatever that order says.
- **AUX takes a stem off its channel.** Switch a stem to AUX in StemDeck's
  mixer and it leaves its bus — and so its A³ channel and its movement — and
  goes to the Return track instead, whose level is the RET pot (on A³
  Motion's MIXER, and the desk's FX return).

(stemdeck-with-motion-setup)=

## Setting it up

You need StemDeck, A³ Core with the Beat Analyzer, and A³ Motion — the A³
Mixer is welcome but optional, since A³ Motion's MIXER page has the same
controls.

### 1. The audio: StemDeck into A³ Core

**On A³ Core** there is nothing to do: the a3-core package runs zita-n2j for
ten channels and its patchbay wires them into REAPER inputs 11–20.

**On the StemDeck machine**, send the ten outputs to the Core over the
network:

1. Run `zita-j2n` for 10 channels, pointed at the Core's address and the port
   zita-n2j listens on (65100 in the a3-core package).
2. Patch StemDeck's outputs into `zita-j2n`'s inputs **in order**:
   `deck1_L` → 1, `deck1_R` → 2, … `aux_R` → 10. StemDeck
   [never connects anything by itself](#stemdeck-audio), so this is on you —
   once, in qjackctl or any patchbay, and saved.
3. Settle the StemDeck machine's sample rate **before** StemDeck and
   zita-j2n start. StemDeck takes the rate it finds and asks for nothing, on
   purpose: changing a running graph throws zita-j2n out.

**StemDeck on the Core machine itself?** Then skip the network: patch its ten
outputs straight to REAPER's `in11` … `in20`, in the same order.

<!-- QUESTION (maintainer): the page describes the Core side as the a3-core package ships it (zita-n2j, --chan 1-10; patchbay out_1..10 -> REAPER in11..in20; REAPER template: pairs 1-2/3-4/5-6/7-8 to 1-input..4-input, 9-10 to Return). The sender side — how zita-j2n is started on the StemDeck machine and whether its inputs are patched deck1_L..aux_R in order — is not in any repository. Is that how the rig runs it, and should StemDeck ship a j2n helper? -->

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

1. **Load a track in StemDeck.** Pick one you know well, split by StemDeck
   (drums, bass, other, vocals). Check the meters in StemDeck's mixer: all
   four buses move. On A³ Motion the four channel meters move with them.
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
7. **Mix the next track in** on StemDeck's other deck. Its drums join
   channel 1, its vocal channel 4 — already on the move. When you hand
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
| A³ Motion's channel meters stay still while StemDeck plays | The stems don't reach the Core. Check StemDeck's outputs are patched into zita-j2n, and that zita-j2n reaches the Core |
| Drums show up on the vocal channel | The outputs are patched out of order on the StemDeck side. `deck1_L` goes to input 1, `aux_R` to input 10 |
| A stem plays but doesn't move | Its channel's **3d** is down, or its clip isn't playing. Or the stem is on **AUX**: then it is on the Return track, not on a channel |
| A³ Motion doesn't follow StemDeck's tempo | Wait for the deck's BPM; is the deck playing and the top bar saying `PIO master`? Is A³ Motion on **PIO**? Is the Core in the same network as StemDeck? |
| The movements start one beat off the bar | StemDeck counts the bar from the first beat of the track's beat grid. Set the downbeat with the jog |
| The stems stop after a change in the audio settings | Changing the sample rate or buffer of a running graph throws zita-j2n out. Restart it, and set the rate before starting next time |
