# Uploading and confirmations

Outcome: you can describe what happens to a `.tq8` after signing,
how a confirmation comes into existence, and why you cannot
hurry one. The lab signed nothing and uploaded nothing — the
account this chapter needs is a real one — so the whole chapter
is **documented-only**, drawn from TQSL's bundled help and the
program's own dialogs and files, all of which the lab did
inspect.

## Getting the signed log to LoTW

There are three routes, and TQSL supports all of them because
the signing machine and the internet machine are not always the
same computer:

- **Automatic.** *Sign a log and upload it automatically to
  LoTW* does both steps in one action; chapter 7's Final Status
  then covers the upload too (code 2 is "Rejected by LoTW",
  code 11 is a connection failure).
- **Manual.** *Sign a log and save it for uploading later* leaves
  you a `.tq8`, which you upload through the LoTW website's
  upload page, signed in to your account.
- **By hand, offline.** TQSL's help documents the
  no-internet-access flow explicitly: sign on the offline
  machine, carry the `.tq8` to a connected one, upload there.
  The signature travels inside the file; the uploading machine
  needs no certificate at all.

However it arrives, LoTW queues the file for processing — a
successful automatic upload reports the result "File queued for
processing". Two bookkeeping details matter afterwards. TQSL
records the upload locally in `~/.tqsl/uploaded.db`, which is
what powers the duplicate warnings in chapter 7; and LoTW keeps
your submitted QSOs visible in your account, under your QSO
queries, so you can always verify that what you sent is what
LoTW received.

## How a confirmation is born

LoTW matches **independently submitted** records. Your uploaded
QSO confirms when the station you worked uploads a record that
agrees on the essentials — callsigns, band, mode, and a time
close enough to be the same contact. Neither side sees the
other's data in advance: that is the **double-blind** design
from chapter 1, and it is why a confirmation means something.
The other station cannot have copied your log, because they
cannot see it.

Consequences worth internalising:

- **A confirmation needs two uploads.** If your partner never
  joins LoTW, the QSO sits unconfirmed forever, correctly.
- **You cannot edit history.** If you uploaded a wrong time, the
  remedy is to upload a corrected record; LoTW's matching uses
  the best agreement, and your QSO list shows what you sent.
- **Confirmations appear when processing and matching finish**,
  not when you upload. LoTW shows them in your account, and they
  are what feed the DXCC, VUCC, WAS and WPX standings the
  service tracks for you.

**The check.** In your LoTW account, the QSO query for a range
you uploaded lists those QSOs as submitted; a confirmed one
shows its confirmation once the other side's upload has matched.
If a QSO you are sure you signed is absent, the upload — not the
matching — is where to look first, and chapter 7's Final Status
line is the evidence to re-check.
