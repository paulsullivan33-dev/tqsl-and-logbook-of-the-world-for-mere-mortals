# Troubleshooting

Outcome: the message in front of you is in this chapter, with
what it means and what to do. Every entry was either produced in
the lab (transcripts in `tqsl-lab/`) or is quoted from TQSL's
bundled help.

## "The callsign … is not currently registered in the FCC ULS database"

TQSL checked your US callsign against the FCC database and did
not find it (chapter 4). If your licence is brand new, wait at
least one business day, as the message says, and check that the
call has actually appeared in the ULS. If it has been there for
years, you have mistyped it. The request cannot proceed for a US
entity until the check passes.

## "You cannot select DXCC Entity NONE …"

Entity NONE is only for requests an existing certificate must
sign. A first request always names a real entity — the one your
licence was issued in.

## "No certificates available"

You asked TQSL to create a station location, or to sign, with no
**issued** certificate loaded. A pending request does not count
(chapters 4 and 6). Check the Callsign Certificates tab: if your
call is under *awaiting ARRL approval*, the `.tq6` has not been
loaded yet — find the ARRL's email, load the file, and look for
the call under *Active, usable certificates* instead.

## "The selected station location could not be found"

Batch signing (`-l "Name"`) names a location that does not exist
in this TQSL's data — a typo, or a location that lives on a
different computer. The run ends `Final Status: Command Syntax
Error(10)`. List your locations in the Station Locations tab and
copy the name exactly. (Transcript `t05`.)

## `Error: Unable to initialize GTK+, is DISPLAY set properly?`

TQSL needs a graphical display for every operation, including
`-v` and `-h`. On a headless machine run it under a virtual
display: `xvfb-run -a tqsl …`, or forward X over SSH. The
program is not broken; it is a desktop application being asked
to work in the dark. (Chapter 3.)

## TQSL exits 255 but the output looks successful

For query operations (`-v`, `-n`, `-h` under `xvfb-run`), the
lab measured exit status 255 on completely successful runs.
Trust the printed output. For signing runs, trust the
`Final Status:` line and its code — there, the exit status does
mirror the code. (Transcripts `t01`, `t05`.)

## The help window shows angle brackets and raw HTML

Seen in the Debian build: the bundled help viewer displays its
pages as source text. The content is intact — read the pages as
files in `/usr/share/TrustedQSL/help/tqslapp/`, run `man tqsl`
for the program itself, and use the ARRL's online LoTW
documentation for the rest. Your installation is not damaged.

## "A new TQSL release is available" — but your package manager disagrees

Normal. Upstream releases (2.8.7 at lab time) reach distribution
packages (2.7.2) later. LoTW accepts signatures from both.
Upgrade from your distribution when it offers one; treat
TQSL's own announcement as information, not an instruction.
Configuration updates are the exception — accept those when
offered, since entities and modes depend on them (chapter 2).

## The certificate never arrived

The `.tq6` is emailed to the address entered on page 3 of the
request wizard. Check that mailbox's spam folder first. If the
address was wrong, the request cannot be repaired — the ARRL's
help directs you to make a fresh request with the right address,
and chapter 5's rule applies: the new request makes a new key,
so the matching private key is the one from the new request.

## Final Status 8 or 9 — "already uploaded" / "out of date range"

Not an error in your log. TQSL's uploads database remembers what
was sent (code 8: nothing new to do; code 9: some QSOs signed,
some skipped). Causes: the log was already submitted, or the
QSOs fall outside the signing date range or the certificate's
date window (chapters 4 and 7). If the database itself is wrong
— after restoring onto a new machine, for instance — the
nuclear option is `tqsl -w` to wipe it, knowing the duplicate
protection goes with it.

## Still stuck

Switch on **Diagnostic Mode** (File menu) and repeat the failing
operation; TQSL then logs verbosely, and the batch option `-t`
names a diagnostic log file. The ARRL's LoTW help desk is the
audience for those logs — and chapter 5's ident line (program,
library and configuration versions) is the first thing to quote
in any report.

**The check.** Every message above should now read as a
sentence in plain language rather than a verdict. If yours is
not in this chapter, it is almost certainly a Final Status code
— and chapter 7's table has all twelve.
