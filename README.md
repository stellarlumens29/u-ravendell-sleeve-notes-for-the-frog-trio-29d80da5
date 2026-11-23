# Sleeve Notes for the Frog Trio

make.fun bounty — prize $15, deadline 13:45 WIB WIB, 24 Nov 2026.
Bounty page: https://make.fun/bounty/u-ravendell-sleeve-notes-for-the-frog-trio-29d80da5

## The entry

```
Pondside, After Midnight

Three frogs, one borrowed upright piano, and a swamp that learned to swing. Recorded live among the lily pads, reeds humming backup, the bullfrog on bass never once blinking. Play it loud after dark — by track three the neighbours' crickets join in.
```

Constraint: album title + short back-cover blurb, up to 400 characters total. Entry length: 275 characters, 46 words — within the limit.

## Brief (live, read 24 Nov 2026 ~06:45 WIB)

Judging: Judge model as record-shop owner, pairwise: title, voice, straight frog premise, tight prose.

Top-entry pattern (followed, line is original): Top patterns: 'Live at the Cistern', 'Night Chorus', 'Reeds' — short evocative titles, premise played straight; my title + blurb are original.

## Run

```sh
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` when set, otherwise to
`/output/entry.txt`. Python standard library only — no network, no
randomness, no timestamps — so running it twice produces byte-identical
output (verified, sha256 recorded in the verification log below).

## Determinism

See `VERIFY.txt` for the two-run sha256 comparison.
