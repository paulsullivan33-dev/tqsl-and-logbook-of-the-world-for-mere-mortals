# Renewals, backups and moving

Outcome: your LoTW identity can survive a dead hard drive, a new
computer and the passage of three years — if you set up the
backups TQSL already offers, which the lab watched it write.

## The three-year clock

Every Callsign Certificate **expires after three years** — that
is TQSL's own help text, not a rule of thumb. TQSL watches the
clock for you: the news check in chapter 3 (`tqsl -n`) reports
expiring certificates alongside program updates, in lines like
"The certificate for YOURCALL expires in 9 days", and it also
reports requests still pending.

Renewal has one sharp edge, again in the help's own words:
renewing is easy **before** the certificate expires, and
"requesting the renewal immediately invalidates the existing
Callsign Certificate" — so renew at a moment when the new
certificate's arrival will not strand a half-signed log. Let the
certificate lapse entirely, and there is no renewal path: you
request a **replacement** certificate, through the chapter 4
flow, identity checks and all.

## Backups: the .tbk

TQSL can save **all** of your Callsign Certificates, Station
Locations and Preferences into one **Backup File** with a `.tbk`
extension: File → *Backup Station Locations, Certificates, and
Preferences…*, and the matching *Restore…* item brings them back
on a fresh install. This file — not the `.tq5` — is the thing to
keep somewhere safe, because it contains the private keys your
signatures depend on.

Better still, it can be automatic, and the lab watched it
happen: on exit, TQSL wrote both a rolling backup and a dated
snapshot into its data folder (transcript `t04`):

```console
$ ls ~/.tqsl/*.tbk
tqslconfig-2026-11-02-15-30.tbk
tqslconfig.tbk
```

The preferences let you choose the folder those exit backups go
to and how many dated copies to keep. Put the folder somewhere
that is itself backed up; a `.tbk` on the same dying drive is a
keepsake, not a backup.

## Moving one certificate: the .p12

To move a **single** certificate to another machine — the club
station's computer, a new laptop — select it in the Callsign
Certificates tab and use **Save a Callsign Certificate**. The
saved file is a **PKCS#12** container (`.p12`): the certificate
together with its private key. On the other machine, **Load a
Callsign Certificate** (or `tqsl -i`) accepts both `.p12` files
and fresh `.tq6` certificates.

Treat a `.p12` with the same respect as the keys folder in
chapter 5: it *is* your identity, in a single portable file.
Carry it on media you control, and delete stray copies.

**The check.** Two files prove this chapter is working on your
machine: a `.tbk` newer than your last change to a location or
certificate, and — if you run two computers — a deliberate,
findable `.p12` for each certificate you move, rather than a
keys folder copied by hand and forgotten.
