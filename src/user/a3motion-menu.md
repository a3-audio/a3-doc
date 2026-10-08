# Menu, skins and keyboard

(motion-menu)=

## The menu

Opened with **MENU** in the status bar, left of STEMDECK, or MENU on the panel.
It opens on top of the sphere. **Nothing in the menu is needed to play.**

| Page | What it holds |
| :--- | :--- |
| **Skin** | which skin is loaded, as a list; the skin previews as you browse it with the arrow keys |
| **Skin Editor** | every value the loaded skin holds, grouped by what it is |
| **Button LEDs** | the colours of the panel's keys |
| **Pattern Folder** | where clips, shapes, actions and sets are read from |
| **Sphere in Menu** | **on**: the sphere keeps drawing behind the menu; **off**: it rests while the menu is open |
| **Developer Mode** | **on** lets Save write over shipped files |

```{warning}
**Developer Mode: leave it off on a gig.** With it on, Save in FILES writes
over the shipped sets, clips, shapes and actions.
```

**In the menu, a value only changes in its edit box**, never by brushing past
it:

| Gesture | What it does |
| :--- | :--- |
| drag the list, or the empty strips left and right of it | scrolls, the way a phone does |
| tap a row that leads to a page (Skin Editor, Button LEDs, Pattern Folder) | opens that page, at once |
| tap any other row | selects it |
| double tap a row, or ENTER | opens it: a list of its values (Skin, Sphere in Menu, Developer Mode), an edit box, or the colour picker |
| in a list of values | tap or ENTER chooses, and a tap chooses at once; Escape or back leaves without choosing |
| in an edit box | type with the keyboard; ENTER keeps; Escape, back or ✕ undo. A skin number also has **− / +** keys that step it while you watch |

Two fingers scroll as one. Inside a page — the Skin Editor and the
others — a tap selects a row and a double tap opens it, as above. **Mind the
double tap on the main menu's page rows:** the first tap has already opened
the page, and the second lands on whatever row is under your finger there.

**Getting out:** the **‹** (back) and **✕** (close) keys in the top right, and
MENU itself. Back and MENU close **one level**; ✕ closes all of it at once,
however deep. **Escape never quits the app.** In a booth, one elbow on a
keyboard shouldn't end your set.

<!-- GIF: howto-menu-navigate.gif | region: 0,0,768,660 | recorded 2026-09-30 (after the Network page left the menu), quiet-indigo-2, --fuzz 1% | steps: Tap MENU, tap Skin Editor, tap All values, drag the list, tap back, tap ✕. | "MENU opens it over the sphere" / "Tap a row: its page" / "Drag to scroll" / "‹ back: one level up" / "✕ closes all of it" | a page row opens on ONE tap; a double tap lands the second tap inside the page -->

![Tap MENU, tap Skin Editor, open All values, drag the list, tap back, tap ✕.](pics_user/howto-menu-navigate.gif)

### Skin

Double tap **Skin**: the rows give way to the list of skins. The arrow keys
↑ ↓ walk the list and preview each skin on the sphere; ENTER keeps the one
you are on, Escape or back puts the running one back. **A tap on a skin
chooses it straight away**, with no preview, and writes it into the device's
settings. Dragging the list only scrolls it.

<!-- QUESTION (maintainer): the preview is reachable only by the arrow keys (GlobalSettingsComponent::keyPressed → onPickerBrowsed); a drag scrolls without previewing, a tap applies and writes config.json (applySkin), and the panel's encoders don't reach the menu at all (handleEncoderTurn has no menu case, although previewSkin's comment speaks of "the encoder"). So on the device without a keyboard there is no way to look at a skin before it is chosen. Intended? -->

### Skin Editor

Every value of the loaded skin, under headings: surfaces, text, states,
channels, sphere, type, touch, then the effects. At the top, five action rows:
**» Save**, **» Save as new**, **» Rename**, **» Delete** (asks "sure?") and
**» Reset** (every value back to the shipped default, keeping the name). They
fire only on a double tap or ENTER.

- A number opens the edit box with − / + to step it live, by a tenth of its
  value each press (whole numbers by one). Escape puts the number back.
- A colour opens the **colour picker**: drag on the picking surface (hue,
  saturation, lightness); the change is live; **done** closes it. There is no
  undo in the picker: whatever you dragged to is kept, and Escape doesn't
  close it. The picker counts channels from zero, so channel 1's colour is
  labelled `channels.0`.
- **Leaving the editor saves the skin**, changed or not. On the shipped
  default skin it saves a copy called **custom** and switches to it, so the
  default itself is never written over.

![The Skin Editor, its sections on the left of the sphere](pics_user/a3-motion-ui-skin-editor.png)

<!-- QUESTION (maintainer): the colour picker has no undo (closeColourPicker keeps what applyPickedColour already wrote into the document) and no Escape, while the edit box undoes the whole document on Escape (_documentBeforeMask). Should the picker undo on back/Escape like the edit box? -->

### Button LEDs, Pattern Folder

Each shows only its own part of the device's settings, as rows: Button LEDs
the key colours; Pattern Folder the folder the library is read from. Double
tap a row to type a new value, or to pick a colour. The page is saved when you
leave it. Hosts, ports and addresses are not in the menu: see
[How to point the device at another Core](#motion-howto-network).

### Sphere in Menu, Developer Mode

Double tap the row, tap **on** or **off**.

(motion-keyboard)=

## The keyboard

The device has its own keyboard. It takes the **bar's place** — where CLIP,
MOTION, ACTION, CHMIX and REC are — so the sphere, the channel row, the tabs
and the global strip stay in view, and every field you type into sits on top
of the sphere, never under the keys.

- **KEYS** in the status bar shows or hides it; its icon follows.
- It comes up by itself when there is something to type — a Rename in FILES
  (every tab, sets too), a touch in the FILES editor, a name or a value in the
  Skin Editor and the menu — and goes again when that is done.
- **HIDE** puts it away and leaves the field open.

**The keyboard is the panel.** Its 44 keys stand on the same grid as the
panel's 44 buttons and the [PADS](#motion-pads) window — ten columns, six
rows — so every key on the screen is the button in the same place on the
device. The letters are **QWERTY**:

| Row | col 0 | cols 1–8 | col 9 |
| :--- | :--- | :--- | :--- |
| 0 | **ESC** | — | **DEL** |
| 1 | **123** | — | **ENTER** |
| 2 | q | w e r t y u i o | p |
| 3 | a | s d f g h j k l | - |
| 4 | z | x c v b n m , . | / |
| 5 | **SHIFT** | ◀ ▶ **SPACE** (four wide) ' " | **HIDE** |

**123** swaps rows 2–4 for what scripts, clips and sets are written with, and
reads **ABC** there to come back:

| Row | Symbols (**123**) |
| :--- | :--- |
| 2 | 1 2 3 4 5 6 7 8 9 0 |
| 3 | - / : ; ( ) = + _ * |
| 4 | { } [ ] < > \ \| ! ~ |

There are no umlauts and no ß.

![The keyboard in the bar's place](pics_user/a3-motion-ui-keyboard.png)

- **SHIFT** once: the next letter is a capital. Twice: caps lock. A third
  time: off.
- On the screen a key types when you **let go**: slide off a wrong key and
  nothing is typed. **DEL** and the arrows act at once and repeat while held.
- **ENTER** keeps what you typed and closes, in a name; in the FILES editor it
  is a new line, and **ESC** or **HIDE** put the keyboard away. **ESC** in a
  name, and Back or Close in the Skin Editor, undo it.

**From the panel: while the keyboard is up, the whole panel types.** Each of
the 44 buttons is the key drawn in its place — the pads are the letters; on
the left TAP is ESC and SHIFT is SHIFT, on the right TAP is DEL and SHIFT is
HIDE — and it types **as you press** it; DEL
and the arrows repeat while held. The pads and key LEDs show the keyboard: the
letters dim, the other keys in the skin's accent colour.

- **No clip fires and no key does its own job** while you type: no pad
  starts or stops anything, TAP taps no tempo, REC, MENU and SHIFT do nothing
  else. Clips that are running go on.
- **HIDE or ESC gives the panel back.** A key you pressed while typing is
  released to the keyboard too, so letting go of ESC never taps a tempo. A pad
  you were already holding when the keyboard came up lets go as usual.
- **Encoder 1** (channel 1, upper) moves the text cursor. The other encoders,
  SHIFT + encoder (freq and Q), the pots and the faders keep their jobs: the
  mix stays under your hands.

Open the keyboard only when you mean to type, and put it away with HIDE or
ESC before the next clip has to start.
