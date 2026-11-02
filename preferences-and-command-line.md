# Preferences and the command line

Outcome: you can drive TQSL from scripts for the jobs scripts
are good at — checking for news, signing a folder of logs — and
you know which dialogs the batch mode cannot replace.

## The preferences worth knowing

File → *Display or Modify Preferences…* holds TQSL's settings.
The one a new user should meet first is the behaviour of the
automatic `.tbk` backups on exit (chapter 9): the folder they
are written to and how many dated copies are retained. The
**File** menu also holds a **Diagnostic Mode** toggle, which
makes TQSL log verbosely — the first thing to switch on when
chapter 12's recipes are not enough and you are writing to the
ARRL for help. A **Language** submenu switches the interface
language where a translation is installed.

## The command line, honestly surveyed

`tqsl -h` prints eighteen options (transcript `t02` keeps the
full list with the manual's wording). Grouped by job:

- **Ask the program things:** `-v` (version), `-h` (help),
  `-n` (news: new releases, new configuration files, expiring
  or pending certificates).
- **Work with certificates:** `-i` imports a `.p12` or `.tq6`
  file; `-c` sets the default callsign for signing. (Exporting a
  certificate is a GUI job — chapter 9's Save action.)
- **Station locations:** `-s` creates a location, or edits the
  one `-l` names; `-l` selects a location by name for signing.
- **Sign:** a bare log filename signs it; `-u` signs **and**
  uploads; `-o` names the output file instead of the default;
  `-a` chooses how QSOs that are already uploaded or out of the
  date range are handled (`abort`, `compliant`, `all`, or `ask`
  — the default); `-b` and `-e` bound the QSO date range and
  `-d` suppresses the date-range dialog; `-f` chooses the QSO
  verification action (`ignore`, `report`, `update`).
- **Housekeeping, handle with care:** `-w` wipes TQSL's uploads
  database — the memory that powers duplicate warnings — and
  `-t` names a file for a diagnostic tracking log.
- **Batch control:** `-x` exits after processing instead of
  staying open (`-q`, quiet mode, behaves the same), so a script
  never blocks on the window, and `-p` supplies the passphrase
  for a signing key when one is set.

Three behaviours, all measured in the lab, define batch use:

1. **A display is still required** — every command in this
   chapter runs under `xvfb-run` on a headless box (chapter 3).
2. **The Final Status line is the contract.** Scripts should
   read the timestamped status output and its code, not the
   process exit status alone: batch signing mirrors its code
   into the exit status, but query commands like `-v` and `-n`
   exit 255 even when they work (transcript `t01`).
3. **Missing prerequisites fail fast with a sentence, not a
   crash** — `No certificates available`,
   `The selected station location could not be found`
   (transcript `t05`). In a script, those sentences *are* the
   error handling.

A realistic script use, once a real certificate exists:

```console
$ xvfb-run -a tqsl -n
A new TQSL release (V2.8.7) is available.
A new TrustedQSL configuration file (V11.34) is available.
```

— a weekly cron job that only speaks when there is something to
do, exactly like the news run the lab actually made.

**The check.** `tqsl -n` under a display prints either news or
silence, and `tqsl -s -x` on a machine without a certificate
prints `No certificates available`. If you can predict both
outputs before you run them, the command line holds no more
surprises for you.
