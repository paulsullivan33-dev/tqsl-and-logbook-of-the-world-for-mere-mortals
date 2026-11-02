# Getting a Callsign Certificate

Outcome: you have walked the whole request wizard, produced a
real `.tq5` certificate request, and can point at the exact step
where the ARRL — not the software — has to take over. The lab ran
every step below with the dummy callsign **N0CALL**, the call the
hobby reserves for exactly this kind of demonstration; no real
certificate can ever be issued for it, and none was requested
from the ARRL. Where the real flow continues past the lab, the
chapter says so plainly.

## Page 1: callsign, entity, dates

Answer **Yes** to the first-run alert (or use the Callsign
Certificate menu) and the **Request a new Callsign Certificate**
wizard opens. Page 1 asks for:

- **Call sign** — the call this certificate will sign for.
- **DXCC entity** — a list of some 340 entities, countries and
  territories in the DXCC programme's sense.
- **Date of the first QSO** you made or will make with this call,
  and **date of the last QSO** — leave the last one blank if the
  call is still yours. The certificate will only sign QSOs inside
  that window, so the first date matters: pick the earliest log
  you will ever want to upload, not the day you installed TQSL.

The page validates as you go: "You must enter a valid call
sign.", "You must select a DXCC entity.", and a spelling-out of
the date rule if the date fields are incomplete.

## The check nobody warns you about

With N0CALL and **UNITED STATES OF AMERICA** chosen, clicking
Next produced this (transcript `t03`):

> The callsign N0CALL is not currently registered in the FCC ULS
> database as of null. If this is a newly registered call, you
> must wait at least one business day for it to be valid. Please
> enter a currently valid callsign.

TQSL downloads the FCC's licence database and checks United
States callsigns against it **before** it will even build a
request. For a real, newly granted US call the practical lesson
is the one in the message: wait a business day after your licence
appears in the ULS, then request. For the lab's dummy call, the
US route is simply closed — N0CALL is registered to nobody, and
TQSL knows it.

Two more refusals map the edges. The entity list's `-NONE-`
entry is refused too:

> You cannot select DXCC Entity NONE as you must sign any request
> for entity NONE and you have no valid Callsign Certificates
> that you can use to sign this request.

(NONE exists for the rare request that an existing certificate
must endorse.) Choosing **CANADA** — an entity with no FCC-style
check for TQSL to make — let the lab proceed. Be clear about
what that means: pairing a dummy US-style call with the wrong
country is a lab device to exercise the wizard. Such a request
could never survive the ARRL's own checks, and the guide treats
it as scrap paper throughout.

## Pages 2 and 3: who and where

Page 2 asks for name, postal address, city, state or province,
postal code and country; every field is required ("You must
enter your name"). The lab entered plainly fictitious details —
Alex Example of Exampleton, Ontario. Page 3 asks one thing, with
the most consequential note in the wizard:

> Your e-mail address. **Note: The e-mail address you provide
> here is the address to which the issued Certificate will be
> sent. Make sure it's the correct address!**

The wizard then offers a choice:

> Do you want to upload this certificate request to LoTW now?
> You do not need an account on LoTW to do this.

The lab answered **No** — uploading the dummy's request would be
sending scrap paper to a real service — and saved the request to
a file instead, which produced the final dialog:

> You may now send your new certificate request (…/N0CALL.tq5)
> to: lotw-help@arrl.org — or see: https://www.arrl.org/lotw/

On disk, two things now exist (transcript `t03`): the request
file `N0CALL.tq5`, taken apart in the next chapter, and the
private half of a brand-new key pair in `~/.tqsl/keys/N0CALL`,
which never leaves your machine. In the main window's Callsign
Certificates tab the request sits under **Certificates that are
awaiting ARRL approval**, and its Properties read "Certificate
Request: Awaiting response from ARRL" and — because this wizard
flow never asks for one — "Passphrase: None".

## What happens next is the ARRL's part (documented-only)

Nothing in this section was run; it is the real flow, described
from TQSL's bundled help and the dialogs above, and it requires
a real callsign.

1. **The request reaches the ARRL** — uploaded by TQSL, or the
   `.tq5` file emailed to the address in the dialog.
2. **The ARRL checks that you are you.** This is deliberately
   not done over the internet. US licensees receive a **postcard
   at the address on their FCC licence** carrying a validation
   code; entering that code on the LoTW website sets the
   password on the LoTW account the request created. Most
   non-US applicants prove identity by posting copies of their
   licence and photo ID to the ARRL instead. Either way, the
   trust comes from the postal system reaching the licence
   holder — the software's cryptography only takes over after
   that handshake.
3. **The issued certificate arrives by email as a `.tq6` file**,
   sent to the address from page 3.
4. **You load it**: Callsign Certificate → Load a Callsign
   Certificate, choose the `.tq6`. The pending entry in the
   Certificates tab becomes an **active, usable certificate**,
   matched to the private key that has been waiting in
   `~/.tqsl/keys/` since the request.

Only then can station locations be created and logs signed —
the wall the lab keeps meeting in chapters 6 and 7 is exactly
the gap between steps "request saved" and "certificate loaded".

**The check.** After the wizard, your Callsign Certificates tab
should show your call under *awaiting ARRL approval*, and a
`.tq5` file (or an upload) carrying your callsign should exist.
If the tab is empty, the request was never finished — the wizard
keeps nothing until its last page.
