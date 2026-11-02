# Signing your first log

Outcome: you can state exactly what signing needs and what it
produces, you have the lab's real batch-mode failures to learn
the receipts from, and you know how to read the one line that
tells you whether a signing run worked — the Final Status.

## The ingredients

Signing is where the previous chapters meet. TQSL takes:

- an **unsigned log** — ADIF from your logging program, or a
  Cabrillo contest log;
- an **active Callsign Certificate** whose date window covers
  the QSOs;
- a **Station Location** belonging to that certificate.

It emits a **`.tq8`**: the same QSOs, each stamped with the
location's details and wrapped in your key's signature. The lab's
specimen input is `tqsl-lab/sample-log.adi`: two QSOs, both
stations written as the dummy call N0CALL, in grid FN31 — a file
that exists to exercise the signer, not to describe a real
contact.

## What the lab could run

With the pending request as the only "certificate", every route
to signing stops early, and the failures are instructive because
TQSL reports them so cleanly (transcript `t05`):

```console
$ tqsl -d -a all -x -l "Lab Home" sample-log.adi
TQSL Version 2.7.2 [unknown]
The selected station location could not be found
Final Status: Command Syntax Error(10)
```

The `-l` name matched nothing — no location exists — and the run
ends with a **Final Status** line and exit status 10. Attempting
to sign by picking a location interactively stops even earlier,
at the same `No certificates available` wall as chapter 6. There
is no dishonest way past this point: a signature from an issued
certificate is the product, and the lab does not have one. The
rest of the chapter is therefore —

## A successful signing (documented-only)

From TQSL's bundled help and the batch-mode documentation that
ships in `man tqsl`:

In the GUI, the **Log Operations** tab offers *Sign a log and
upload it automatically to LoTW* and *Sign a log and save it for
uploading later*. You choose the log file, the station location,
and a **QSO date range** — signing can be restricted to QSOs
between two dates, which is how a catch-up upload of one contest
avoids resubmitting a decade. TQSL warns if the file contains
QSOs it has already uploaded (it remembers, in `uploaded.db`),
and proceeds.

From the shell, the same work is one line, in the shape the lab
used:

```console
$ tqsl -d -a compliant -x -l "Home" mylog.adi
```

`-d` suppresses the date-range dialog, `-a compliant` sets how
QSOs that were already uploaded, or fall outside the date
range, are handled, `-x` is batch mode (no dialogs), and `-l`
names the station location.
The output file is named for the input: `mylog.tq8` beside
`mylog.adi`, ready to upload or to carry to a machine that has
internet access.

Every run ends with a timestamped progress log whose last line
is the receipt:

```
06:05:56 PM: /home/user/mylog.tq8 is ready to be emailed or uploaded.
06:05:56 PM: Final Status: Success (0)
```

The Final Status codes, from TQSL's own command-line help page,
are the vocabulary of every signing conversation:

| Code | Meaning |
|---|---|
| 0 | Success — all QSOs signed and saved or uploaded |
| 1 | Cancelled by user |
| 2 | Rejected by LoTW |
| 3 | Unexpected response from the TQSL server |
| 4 / 5 | TQSL error / TQSL library error |
| 6 / 7 | Could not open the input / output file |
| 8 | No QSOs processed — all already uploaded or out of the date range |
| 9 | Some processed, some ignored for the same reasons |
| 10 | Command syntax error |
| 11 | LoTW connection error |

Codes 8 and 9 are not failures of your log; they are TQSL
telling you its memory worked. When a batch run does produce a
`Final Status` line, the process exit status mirrors the code —
the lab's run above exited 10, as advertised.

**The check.** A signing you can trust ends two ways: a `.tq8`
file exists where the log said it would be written, and the last
line reads `Final Status: Success (0)` — or a code from the
table that you can explain. Anything else, including silence, is
not a signed log.
