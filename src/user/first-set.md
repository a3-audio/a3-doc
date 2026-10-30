(first-set)=

# First set

Twenty minutes, three moments you hear. First the hi-hats of a CDJ track
start to circle the floor while its kick stays put. Then the vocal of a
StemDeck track rises over the crowd on the drop and comes back on the one.
Then both run on one beat. After that you know the instrument; the rest is
taste.

What has to be there: A³ Core with its engine running
([What you need](what-you-need.md)), a desk (the A³ Mixer, or the
{ref}`virtual desk <a3mix-virtual>`), A³ Motion (the hardware, or its screen
alone, by touch or mouse) and StemDeck deck A, which always runs on the Core. No
speakers yet? Read [Without speakers or panels](#first-set-no-hardware) first.

```{warning}
**Start quiet.** The desk's **MASTER** and **BOOTH** down, then bring them up
slowly. A room that was never set up plays at the shipped low level; set it
up first: [The audio engine](audio-engine.md).
```

(first-set-stereo)=

## 1. A CDJ on ST: one band moves

1. **Plug the CDJ in.** Its L/R outputs go into the interface inputs of
   channel 1 (on a shipped Core: inputs 1 and 2).
2. **Put channel 1 on ST.** Turn its **INPUT** knob to **ST** and push: the
   bracket sits over ST. Fader up, MASTER up. You hear the track spread
   around the room, standing still.
3. **Pick a clock** ([Who is the clock](#first-set-clock)): with a CDJ on Pro
   DJ Link, tap A³ Motion's clock key to **PIO**. The BPM on A³ Motion
   matches the CDJ.
4. **Load a set** on A³ Motion: **FILES** › **SETS** › *Warmup* › **Load**.
   Loading sets 3d, FREQ and Q of all four channels, so load first and turn
   afterwards.
5. **Choose the band.** In channel 1's field of A³ Motion's channel row: turn
   **FREQ** high and **Q** narrow. That band is where the hi-hats are.
6. **Turn 3d up** on channel 1 and press its **Play\|Pause**. It blinks and
   starts on the downbeat.

**What you hear:** the hats leave the track and circle the room on the
clip's path. The kick and the bass stay on the floor. Turn 3d down and the
hats sink back into the track. Turn FREQ down and Q wide, and much more of
the track moves: you hear why A³ moves one band and not the whole channel.

More: [A³ Motion's first ten minutes](#motion-get-started) (actions on the
pads, pausing on the downbeat).

(first-set-stem)=

## 2. A deck's vocal rises

1. **Load a track on StemDeck deck A** (the **STEMDECK** key at the far right
   of A³ Motion's top bar takes you there) and wait for its BPM.
2. **Put it on channel 2.** Turn channel 2's **INPUT** to **A** and push.
   Press **PLAY** on the deck and bring channel 2's fader up. A³ Motion's
   channel 2 now says **DECK A**: the deck moves its own stems.
3. **Mix it in** against the CDJ as you would on any mixer: EQ, fader, the
   filter's FX key. They act on the whole deck.
4. **Before the drop**, choose the length under the vocal stem's pads
   (**‹ ›**: ½ to 8 bars), then tap **RISE** on the vocal.

**What you hear:** on the next bar the vocal lifts out of the track and rises
over the crowd; after the bars you chose it comes back down and sinks into
the track again. The drums, the bass and the rest never moved. Try **ORBIT**
on the drums in a break, **PING** on a stab, **SCAT** on a fill.

Pre-listen to a stem with its **CUE** key: it is in your headphones whether
the deck is on a channel or not. A stem's **AUX** knob sends only that stem
to the beat delay, the vocal echoing from where it is.

(first-set-clock)=

## 3. Who is the clock

Everything that moves counts in bars, so everything needs the same beat. Pick
**one** source for the evening on A³ Motion's clock key; it sets the Beat
Analyzer's mode for the whole system.

```{admonition} Who is the clock tonight?
:class: tip

| Your booth | Clock key | Where the beat comes from |
| :--- | :---: | :--- |
| CDJs on Pro DJ Link | **PIO** | the CDJ that is tempo master |
| StemDeck, no CDJs | **PIO** | the deck with **MASTER** on; see {ref}`StemDeck as the tempo master <stemdeck-master>` |
| CDJs and StemDeck | **PIO** | the CDJ that is tempo master; the StemDecks follow it with **SYNC** |
| vinyl, or players without Pro DJ Link | **EXT** | the Beat Analyzer, listening to the music; tap **TAP** on the desk to set the one |
| nothing to listen to, or you want to play the tempo | **INT** | A³ Motion itself: tap the tempo there |

The clock is never saved in a set: check it at soundcheck. Details:
{ref}`Beat Analyzer › Clock modes <beat-analyzer-modes>`.
```

With one clock, A³ Motion's clips and StemDeck's actions start on the same
bar line. Hand the master over from deck to deck, or from CDJ to CDJ, and A³
Motion follows the new tempo.

(first-set-no-hardware)=

## Without speakers or panels

You can play all of this before you own a speaker ring or the hardware
panels:

| Instead of | Use |
| :--- | :--- |
| the speakers | **headphones** on the PHONES output. Turn **CUE/MIX** fully to MIX: you hear the whole room folded to two ears (binaural), every movement included |
| the A³ Mixer | the {ref}`virtual desk <a3mix-virtual>`, on any machine with a screen on the A³ network |
| the A³ Motion panel | the A³ Motion screen alone (the Motion UI, installer role Motion) on a machine with a screen, by touch or mouse; 3d, FREQ and Q are in its channel row |
| a CDJ | any stereo player into an ST input, or only StemDeck: then step 1 has nothing to move, and steps 2 and 3 work as written |

The REC output is the same binaural mix: StemDeck's **REC** key records
what the room would hear.

## Where next

- [On stage](a3motion-on-stage.md) before your first gig.
- [StemDeck × A³ Motion](stemdeck-with-motion.md): how the two share a set.
- [A³ Motion](a3motion.md) and [StemDeck](stemdeck.md), control by control.
