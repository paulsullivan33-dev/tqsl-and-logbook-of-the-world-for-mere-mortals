# TQSL and Logbook of the World for Mere Mortals

An amateur radio contact only counts toward the big awards when the
other station confirms it. Logbook of the World (LoTW) is the ARRL's
online service for those confirmations, and TQSL — short for
TrustedQSL — is the free program that digitally signs your log on
your own computer so LoTW can trust what you upload. This guide
takes you from installing TQSL to understanding exactly what a
callsign certificate is, how a signing request is built, and where
the line sits between what the software does and what only the
ARRL can do.

The lab behind this guide ran TQSL 2.7.2 for real: the install, the
first-run dialogs, a complete certificate request for the dummy
callsign N0CALL, the program's refusal to accept that callsign for
a United States entity, the request file taken apart field by
field, and signing and station-location attempts that failed for
reasons the guide explains rather than hides. Nothing was uploaded
to LoTW, and no real certificate can be issued for a dummy call —
so the parts of the journey that need a real licence and a real
LoTW account are marked documented-only and described from TQSL's
own bundled help and dialogs.

## What this guide covers

- What LoTW is, what TQSL adds to it, and why uploads are signed
  at all.
- Installing TQSL and surviving its first run — a program that
  wants a display even to answer `--help`.
- The certificate request wizard, exercised end to end, including
  the FCC database check that stops a request for an unregistered
  United States callsign.
- The `.tq5` request file dissected with a small script kept in
  the lab: what the ARRL is actually being sent, and what stays
  on your machine.
- Station locations, signing, and the Final Status codes — what
  the lab could do, what it honestly could not, and what a run
  looks like once a real certificate arrives.
- Backups, renewals, the `.tq6`, `.tq8`, `.p12` and `.tbk` file
  family, and the batch command line.

## What this guide doesn't cover

- Operating a radio or keeping a log. Your logging program makes
  the ADIF file; this guide starts where the log file exists.
- Creating a LoTW account, the ARRL's identity checks (a postcard
  for US addresses, posted documents for most other countries),
  and loading the issued `.tq6` certificate. These steps belong
  to the ARRL, need a real callsign, and are described — clearly
  labelled documented-only — but never presented as run here.
- Award rules themselves. LoTW feeds DXCC, VUCC, WAS and WPX;
  what counts for each award is the ARRL's business.
- Anyone else's certificate. A callsign certificate is a
  cryptographic identity tied to a real licence; this guide only
  ever requests one for the dummy call N0CALL, which can never
  be issued.

## How to use this guide

Read it in order the first time — each chapter builds on the
last, and each opens by naming the outcome it delivers and shows
a check so you can confirm you got it. The lab files live in
`tqsl-lab/`: the request file (`N0CALL.tq5`), the sample log
(`sample-log.adi`), the checker script (`check-tq5.py`), and the
transcripts (`t00`–`t07`) that this guide's claims rest on.

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Ham Radio for Mere Mortals](https://paulsullivan33-dev.github.io/ham-radio-for-mere-mortals/)
- [WSJT-X for Mere Mortals](https://paulsullivan33-dev.github.io/wsjtx-for-mere-mortals/)
- [Pat (Winlink) for Mere Mortals](https://paulsullivan33-dev.github.io/pat-winlink-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/tqsl-and-logbook-of-the-world-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/tqsl-and-logbook-of-the-world-for-mere-mortals/blob/main/LICENSE-CODE).
