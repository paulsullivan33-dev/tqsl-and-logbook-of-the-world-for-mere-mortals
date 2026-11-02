# Station locations

Outcome: you know exactly what a station location records, why
TQSL refuses to create one before a certificate exists — the lab
hit that wall three ways, on the record — and the full procedure
you will follow the day your certificate arrives.

## What a station location is

A Callsign Certificate says **whose** QSOs these are. A Station
Location says **where the station was** when they were made, and
LoTW needs both on every signed QSO: your partner's award credit
for grid squares and zones depends on your location being right.
One certificate can own many locations — home, a portable site, a
club station, last year's holiday address — and you pick the
right one each time you sign.

## The lab's attempt, honestly recorded

The lab tried to create a location for N0CALL's pending request
three ways (transcript `t06`):

1. The **Station Locations** tab, "Create a new Station
   Location": no dialog; the Status Log gained one line —
   `No certificates available`.
2. The **Station Location** menu, "Add Station Location": the
   same line a second time.
3. Batch mode from the shell (transcript `t05`):

```console
$ tqsl -s -x
TQSL Version 2.7.2 [unknown]
No certificates available
```

A **pending request is not a certificate**. A station location's
first field is the certificate it belongs to, so with nothing
issued, there is nothing to attach a location to, and TQSL says
so instead of letting you build on sand. This is a genuine limit
of any lab that cannot use a real callsign, and it is why the
rest of this chapter is labelled:

## The procedure (documented-only)

From TQSL's bundled help ("Specifying a Station Location"), the
dialog you will get once a certificate is loaded:

1. **Select your callsign** — the certificate this location
   belongs to. Its DXCC entity frames everything else.
2. **Grid Square** — the Maidenhead square the station is in.
   TQSL calls this out as especially important for VHF, UHF and
   satellite operators, whose partners chase VUCC grid awards.
3. **ITU Zone** and **CQ Zone** — the two zone systems. If the
   zones and the DXCC entity disagree, the dialog reports
   "Invalid zone selections for DXCC entity" and disables its
   Next button until they are consistent; TQSL would rather stop
   you than stamp a wrong zone onto thousands of QSOs.
4. **IOTA Reference Number**, if the station is on an island —
   a continent code and a three-digit number, like `OC-005`.
5. Depending on the entity, a further page asks for the
   administrative subdivision awards care about: **state and
   county** for US stations, province for Canadian ones, and
   their equivalents elsewhere.
6. **Name the location** and click Finish. The help's advice is
   to make the name carry the callsign and the place — you will
   be choosing it from a list while signing, often for a log
   from months ago, and "Home" ages badly when there turn out
   to be three homes.

The finished location appears in the Station Locations tab and
in the `-l` argument of the batch signer. Editing, deleting and
restoring deleted locations live in the same tab and menu, and
locations travel with certificates in the `.tbk` backups of
chapter 9.

**The check.** On a machine with an issued certificate: create
the location, then look at the Station Locations tab — your name
for it should be listed beside its callsign. In the lab's terms,
the matching check is the transcript: three attempts, one clear
sentence from the program, `No certificates available`.
