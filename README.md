# Letter Board Planner

This is a utility for planning a letter board message so you can figure out how it'll fit and whether you have enough letters before you start placing them.

Features:
* Checks your message against your letter inventory
* Previews the board with lines wrapped
* Estimates whether your message will fit on your board size (see caveats below)

## Usage

### Describe your board and letters

Update `board_letters.txt` with the letters you have for your board. Format the list however you like; spaces and line breaks are ignored. The default file has the inventory for the letter board I impulse bought at Target in July 2023, so if you also impulse bought a letter board at Target around that time, it may already be correct.

Put a few letters on the real board to get a sense of how many will fit both vertically and horizontally. Vertical is straightforward, just remember to include some spacing between rows. Horizontal is trickier because the letters are different widths. I placed wide letters (like W) across the board to get a ballpark, then added a few to account for the fact that many letters (like I) are narrower.

At the top of `letter_test.py`, change the `BOARD_ROWS` and `BOARD_COLS` numbers to how many letters fit on your board. I could fit 8 rows of letters with a little space between them, and about 10 wide letters in a single row, so the defaults are 8 rows and 13 columns.

### Test and preview a message

Edit `board_message.txt` with the message you'd like to put on your board. The script will add line breaks for you, but you can add your own and it will keep them. Completely empty lines will be ignored, so if you want an empty line, put a space on it.

Run `python letter_test.py` to check whether you have enough letters and if the message might fit on the board. Note that because the preview assumes a fixed-width font and the actual board letters are variable-width, the fit is just an estimate. If the message looks way too long or clearly short enough, it's probably correct, but if it's close, think about what specific letters are on each line and use your judgment. (Or try just the questionable line on the real board before adding the rest.)

## Examples

Both of these use the default letter inventory and board size settings.

---

Contents of `board_message.txt` (using spaces on empty lines to ensure they stay in the output):

```
snail,
 
ever so slowly, climb
 
mt. fuji
 
    -issa
```

Output:

```
$ python letter_test.py
You have enough letters.

Preview:
+---------------+
| SNAIL,        |
|               |
| EVER SO       |
| SLOWLY, CLIMB |
|               |
| MT. FUJI      |
|               |
|     -ISSA     |
+---------------+
```

---

Contents of `board_message.txt`:

```
this message is very long. it probably won't fit on the board, and it might even have too many of the same letters!
```

Output:

```
$ python letter_test.py
You're missing these letters: TTTEEEV'
You might not have enough space.

Preview:
+---------------+
| THIS MESSAGE  |
| IS VERY LONG. |
| IT PROBABLY   |
| WON'T FIT ON  |
| THE BOARD,    |
| AND IT MIGHT  |
| EVEN HAVE TOO |
| MANY OF THE   |
+---------------+
```
