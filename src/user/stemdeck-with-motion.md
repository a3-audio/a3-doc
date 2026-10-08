# StemDeck × A³ Motion

(stemdeck-with-motion-at-a-glance)=

## At a glance

Move a stereo mix and the whole track moves, like a speaker on a trolley.
[StemDeck](stemdeck.md) sends **four stems** — drums, bass, other, vocals — to
**A³ Core's four channels**, the ones [A³ Motion](a3motion.md) moves. So each
part gets its own path: drums hold the floor, the vocal circles overhead, the
pads breathe wall to wall, the bass stays put.

And it runs **in time with the track**: StemDeck is the tempo master on Pro DJ
Link, the [Beat Analyzer](beat-analyzer.md) follows, A³ Motion follows the
analyzer. No special mode: three programs, wired together.

<!-- GIF: the room view on A³ Motion with a StemDeck track playing: four blobs on four different clips, and StemDeck's four stem meters beside it (split screen or two recordings side by side) -->

(stemdeck-with-motion-why)=

## Why it works so well

- **One moving part over a steady rest** reads as a gesture; a moving full mix
  smears.
- **A stem per channel.** Bus N arrives on channel N. The stem creator always
  makes drums, bass, other, vocals as stems 1–4, so one choice fits every track.
- **One clock from the music.** The master deck's beat, tempo fader included,
  drives the room.
- **The channel is the part, not the deck.** Keep the drums on channel 1 and
  channel 1 stays "the drums" across decks and tracks.

(stemdeck-with-motion-map)=

## Which stem goes where

StemDeck plays on the Core (workspace STEMDECK) or from another machine; the
REAPER project spreads it the same way (ports: {doc}`Patchbay <../ressources/patchbay>`):

| StemDeck output | Arrives on | What is on it |
| :--- | :--- | :--- |
| `deck1_L/R` … `deck4_L/R` (buses 1–4) | **channels 1–4** | stems switched to that number |
| `aux_L/R` | the **Return**, at the **RET** pot, in STEM mode (ANALOG mode plays analog 11/12) | stems switched to **A** |

A stem then runs through its channel's strip like any deck: gain, EQ and fader
on the desk; 3d, freq and Q on A³ Motion.

- **A stem replaces the analog input.** Core shuts the channel's analog input
  (REAPER's `analog` send to `N-input`) while a stem is on it. Choose on the
  desk: turn the channel's encoder to the stem and push; push **A** to go back
  to analog ({ref}`input selectors <a3mix-displays>`).
- **Nothing is on a channel at first**: stems start on AUX only
  ([Where the stems start](#stemdeck-start-buses)). Custom stem names sort
  into 1–4 by ending ([Stem sets](#stemdeck-stem-sets)).
- **A stem plays on every lit bus** (**1 2 3 / 4 A**). On a number it moves
  with that channel; on **A** only it is on the Return and does not move.
  Pushing it onto a channel from the desk takes its AUX away
  ({ref}`remote control <stemdeck-remote>`).

(stemdeck-with-motion-setup)=

## Setting it up

You need StemDeck, A³ Core with the Beat Analyzer, and A³ Motion; the A³ Mixer
is optional (A³ Motion's MIXER has the same controls).

### 1. The audio: StemDeck into A³ Core

On the Core itself, nothing to wire: the package's patchbay connects StemDeck
to REAPER and a user service keeps it running
([Always running on the Core](#stemdeck-on-the-core)). On another machine:
[StemDeck on another machine](#stemdeck-with-motion-remote-machine).

### 2. The clock: StemDeck as master

1. Load a set and **wait for the BPM** (no beats before the analysis is done).
2. Press **MASTER**, or just **PLAY**: the only playing deck becomes master.
   The top bar reads `PIO master: A`.
3. On A³ Motion, tap the clock key to **PIO** (sets the analyzer to mode 2).
   The BPM follows StemDeck.

StemDeck **broadcasts** on its own network; the Core must be in it (always,
on one machine). Chain: {ref}`Playing without CDJs <beat-analyzer-without-cdjs>`.
Ask before joining a venue's Pro DJ Link ({doc}`../ressources/trademarks`).

<!-- IMAGE: StemDeck's top bar with "PIO master: A" next to A³ Motion's clock key reading PIO and the same BPM -->

### 3. The room: 3d up

Turn **3d** up on the channels to move (pot above the pads, or **3D** in the
channel row). At 0 a channel is plain stereo.

(stemdeck-with-motion-first-set)=

## Your first set

The **MOTION** / **STEMDECK** key at the far right of each top bar switches
between the two ([workspaces](#stemdeck-workspaces)).

1. **Load a track you know** and put its stems on channels 1–4: push each on
   the desk, or light bus 1 on drums, 2 bass, 3 other, 4 vocals. A³ Motion's
   channel meters move.
2. **StemDeck as clock**: PLAY, `PIO master: A`, A³ Motion on **PIO**.
3. **Load a set** on A³ Motion: FILES › SETS › *Warmup* › **Load**.
4. **One part at a time**: 3d up on **channel 4** (vocal), press its
   **Play\|Pause**; then channel 3, then channel 1.
5. **Leave the bass** low and slow: low end is hard to place and a moving
   bassline makes the room seasick.
6. **Hold A1** on the vocal for a lift; let go and it returns.
7. **Mix the next track** on the other deck onto the same channels; hand over
   MASTER and A³ Motion follows the new tempo.
8. **Walk the night on**: A6 cues a channel into the next phase; load the next
   set for all four.

<!-- GIF: first set, step 4: channel 4's 3d going up and its Play|Pause starting the clip on the downbeat, the blob leaving the centre -->

<!-- GIF: first set, step 6: holding A1 on channel 4 while channel 1 keeps its own clip, then letting go -->

**Try:** mute a stem (**M**, or `1`–`4` for deck A) while its clip runs, and
bring it back on the one: it re-enters already in motion.

(stemdeck-with-motion-remote-machine)=

## StemDeck on another machine

Ten outputs travel to the Core as zita audio. The Core needs nothing: its
package runs zita-n2j, patched into REAPER, with addresses from
`~/.config/a3/osc.env`.

StemDeck's repository ships two user units (`.config/systemd/user/`):
`zita-j2n` sends the 10 channels to the Core's `zita-n2j.audio`; `zita-n2j`
receives REAPER's 2-channel rec bus on `radla.zita-n2j`. Both run
`tools/zita-from-truth.py`, which takes address and ports from the truth
StemDeck fetched ({ref}`StemDeck on radla <osc-radla>`; ports:
{doc}`../ressources/ports`), and restart 2 s after any drop-out.

1. Tell StemDeck where Core is: `~/.config/a3/core`
   ({ref}`StemDeck on radla <osc-radla>`).
2. Install the units (or let the {doc}`installer <../configuration/install>`,
   role StemDeck, do it); repeat after a StemDeck update:

   ```sh
   cp .config/systemd/user/zita-*.service ~/.config/systemd/user/
   systemctl --user daemon-reload
   systemctl --user enable --now zita-j2n zita-n2j
   ```

3. Patch StemDeck's outputs into `zita-j2n` **in order** (`deck1_L` → 1 …
   `aux_R` → 10) and `zita-n2j` where you want it — once, saved; or load the
   StemDeck package's `stemdeck-without-core.xml`
   ({ref}`patchbay <patchbay-zita>`). Nothing connects itself.
4. Set the sample rate **before** StemDeck starts: a change on a running graph
   throws zita out for 2 s.

(stemdeck-with-motion-troubleshooting)=

## Troubleshooting

| Symptom | What to do |
| :--- | :--- |
| A³ Motion's meters stay still | Stems don't reach REAPER. On the Core: StemDeck → REAPER in qjackctl's patchbay ({doc}`Patchbay <../ressources/patchbay>`). Elsewhere: patched into zita-j2n, reaching the Core? |
| Drums on the vocal channel | Outputs patched out of order: `deck1_L` → 1, `aux_R` → 10 |
| A stem plays but doesn't move | **3d** down, clip not playing, or the stem is only on **A** (Return) |
| No tempo follow | BPM shown? Deck playing, `PIO master`? A³ Motion on **PIO**? Core on StemDeck's network? |
| Movements a beat off the bar | CUE on the real first beat of a bar, **GRID**, **SNAP** |
| Stems stop after an audio-settings change | zita restarts within ~2 s; else `systemctl --user status zita-j2n`. Set the rate before starting |
