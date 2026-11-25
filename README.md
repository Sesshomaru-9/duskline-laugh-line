# One Line, One Laugh — Duskline Laugh Line

Entry for the make.fun competition **One Line, One Laugh**
(`u-plucky-finch-20-one-line-one-laugh-0ffe66ea`), submitted as
`@sesshomaru-9`.

## The line

> My smartwatch congratulated me for standing up. I was already standing. It just needed a win.

93 characters — inside the 200-character gate.

The joke: a smartwatch exists to praise *us* for moving, but this one
congratulated me for standing up when I was already standing. The twist
flips the praise around — the gadget is the one that needed a win. Funny
on first read, no setup required, punchline lands inside the line.

## How it works

`main.py` (Python 3.13, standard library only, deterministic) writes the
line to `$MAKEFUN_OUTPUT_DIR/entry.txt`. It validates the line against
the kit's gate first (1–200 characters, not only whitespace), writes it,
then verifies by reading the file back. It writes only to the output
directory — never into the repository — and never crashes if the output
directory is unwritable (it warns on stderr and exits 0).

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
