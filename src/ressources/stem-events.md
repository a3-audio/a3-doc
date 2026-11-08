(stem-events-file)=

# Stem events file

The file in which StemDeck keeps a set's [events](#stemdeck-events): planned
movements of the stems, placed on the beat grid. A person can edit it, a program
can write it (`stemdeck-prepare-events` does). This page is format **version 1**.

## Where it lives

Beside the set's **first stem file**, in the same folder:

```text
<first stem file name without its extension>.a3events.json
```

- `Song/drums.wav`, `Song/bass.wav`, ... gives `Song/drums.a3events.json`.
- An NI Stems file drops the whole `.stem.mp4`: `Song.stem.mp4` gives
  `Song.a3events.json`.
- One file per set; all four stems are in it. It travels with the library, to
  any deck host. There is no file when a set has no events (StemDeck deletes it
  when the last event goes).

## Layout

UTF-8 JSON, one object:

```json
{
  "version": 1,
  "events": [
    {
      "stem": 1,
      "beat": 64.0,
      "shape": "orbit",
      "bars": 4,
      "reversed": true,
      "seed": "1311768467463790320",
      "active": true,
      "origin": "prepared"
    }
  ]
}
```

| Field | Type | Meaning |
| :--- | :--- | :--- |
| `version` | integer | the format version, here `1` |
| `events` | array | at most 512 events (see [Limits](#stem-events-limits)) |

Per event, **all eight fields are required**:

| Field | Type | Meaning |
| :--- | :--- | :--- |
| `stem` | integer, 0 to 3 | the stem, in the set's order (the first stem file is 0) |
| `beat` | number | where the event starts, in beats of the deck's grid counted from the grid's first beat (the track's *one*); a decimal, negative before the one. There is **no time in the file**: a grid corrected by hand moves the events with the music |
| `shape` | string | `orbit`, `ping`, `rise` or `scat` |
| `bars` | number | how long the movement runs, in bars: `0.5`, `1`, `2`, `4` or `8`. Another value is played as the nearest of these |
| `reversed` | boolean | `true`: ORBIT runs the other way round. `ping`, `rise` and `scat` ignore it in this version |
| `seed` | **string** of decimal digits | decides the random course of `scat`, so a prepared track scatters the same way every time. Other shapes keep it but do not use it |
| `active` | boolean | `false`: the event is kept but does not fire (shown dimmed) |
| `origin` | string | `hand` (placed or recorded by the DJ) or `prepared` (written by a preparation tool) |

### The seed is a string

A seed is an unsigned 64-bit number. JSON numbers are read as 64-bit floats by
most tools, which lose digits above 2^53, so the seed is written as a **string**
(`"seed": "42"`, not `"seed": 42`). A reader accepts only digits, at most
2^64 - 1; anything else makes that event invalid.

### One event per slot

A **slot** is one stem at one beat. Two events on the same slot (within a
millionth of a beat) cannot exist: the second one in the file is dropped when
the file is read. Events are kept sorted by beat, then stem.

(stem-events-limits)=

## Limits

- At most **512 events** per set. Further events in a file are dropped.
- A set **without a beat grid has no events**: the app neither records nor
  fires any.

## Versions

`version` is `1`. A reader that knows version *n* treats a file as follows:

| File | What StemDeck does |
| :--- | :--- |
| missing | the track has no events |
| valid, version 1 | loads it; an event with an unknown `shape` or `origin`, a missing field or a bad `seed` is skipped, the rest are kept |
| not valid JSON, no `version` or `events`, wrong types | **damaged**: plays the track plain, writes nothing |
| `version` higher than the app knows | **newer**: plays the track plain, writes nothing |

A damaged or newer file is **never overwritten**, not even after the DJ places
or records something: that change then lives in memory only, and the strip says
`FILE DAMAGED` or `NEWER FILE` (and `NOT SAVED`). Move the file away to start a
new one. A valid file is written whole, atomically, so a power cut leaves the
old file or the new one.

## `origin`: hand and prepared

`hand` marks what the DJ made. `prepared` marks what a tool wrote.
`stemdeck-prepare-events` replaces its own `prepared` events when it runs again,
keeps every `hand` event as it is and does not put a prepared event on a slot a
hand event holds. StemDeck itself writes `hand`.
