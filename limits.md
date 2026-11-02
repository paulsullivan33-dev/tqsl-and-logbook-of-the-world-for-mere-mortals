# Limits

Outcome: a clear-eyed list of what TQSL and LoTW cannot do,
cannot promise, and cannot fix — each one met in the lab or
stated in TQSL's own documentation.

**The trust anchor is the post, not the program.** TQSL's
cryptography is sound, but the identity it protects is only as
strong as the ARRL's out-of-band check that the applicant holds
the licence — a postcard to the address on file, or posted
documents. The software never sees that step and cannot
strengthen it.

**A request is not a certificate.** Everything a new user wants
to do — station locations, signing, uploading — waits on the
issued `.tq6`. TQSL enforces the ordering bluntly, as the lab
recorded: `No certificates available`. There is no trial mode,
no self-signed option, no way to practise the full pipeline with
a dummy call; the lab's N0CALL ceiling is the system's design,
not a lab accident.

**TQSL validates US callsigns against the FCC database before
building a request.** A callsign too new to have propagated —
the message says allow at least one business day — is refused
for a US entity. The check is a courtesy filter, not the
identity proof; the ARRL still performs its own verification.

**Certificates sign a date window, and they expire.** A
certificate signs only QSOs between the first and last dates it
was issued for, and it dies after three years. Renewal requested
early invalidates the old certificate immediately; renewal
requested late does not exist — only a fresh request.

**Signing keys are modest and, in the request flow, unprotected.**
The lab's generated request used a 1024-bit RSA key, and its
private half sits in `~/.tqsl/keys/` as unencrypted PEM because
the request wizard sets no passphrase (Properties: "Passphrase:
None"). File permissions are the only lock on that door unless
you add protection when saving and moving certificates.

**Double-blind cuts both ways.** You cannot see what another
station uploaded — which also means you cannot discover *why* a
QSO has not confirmed. Wrong time, wrong mode, or a partner who
never uploaded at all look identical from your side: silence.

**Uploaded history is append-only from where you sit.** A wrong
QSO is corrected by uploading a better record, not by editing
the old one, and TQSL's duplicate protection depends on its
local uploads database — wipe it (`tqsl -w`) and the warnings go
with it.

**The program is a desktop program.** It needs a display even
for pure queries, its exit status is 255 on runs that plainly
succeeded (only signing's Final Status line is a reliable
receipt), and in this distribution build its bundled help window
shows raw HTML. None of these stop it signing; all of them
surprise scripters.

**Configuration drifts separately from code.** Entities, modes
and zone rules arrive as signed configuration data (11.26 →
11.34 during one lab session). A TQSL that is never allowed to
check for updates slowly falls behind the hobby it describes.

**The check.** Read the list again and notice its shape: the
hard limits are about identity and ordering, not about file
formats or speed. TQSL is a narrow, careful tool; everything it
refuses to do is refused on purpose.
