# What TQSL is

By the end of this chapter you can say, in one sentence each, what
Logbook of the World does and why it needs a separate signing
program on your computer.

A **QSO** is one logged radio contact: who you worked, when, on
what band and mode. For awards like DXCC — worked 100 countries —
a QSO only counts when it is **confirmed**, and for a century the
confirmation was a paper card posted across the world.
**Logbook of the World (LoTW)** is the ARRL's electronic version
of that card exchange. You upload your QSOs; the station you
worked uploads theirs; when the two records match closely enough,
LoTW marks the QSO confirmed, and the confirmation feeds your
DXCC, VUCC, WAS and WPX award standings. LoTW is a website and a
database. It lives at `lotw.arrl.org`.

The catch is trust. A confirmation is only worth anything if LoTW
knows the uploaded QSOs really came from the station whose call
is on them. **TQSL** — the program's full name is **TrustedQSL** —
is the ARRL's answer. Before any log leaves your computer, TQSL
**digitally signs** it with a private key that belongs to your
**Callsign Certificate**, an identity the ARRL issues only after
checking that you really hold the licence for that callsign. LoTW
accepts the signature as proof the upload is genuinely yours.

Two design choices follow from that, and they shape the whole
guide:

- **The signing happens on your machine, not on the website.**
  Your private key never leaves your computer. TQSL produces a
  signed file (a `.tq8`), and only that file travels.
- **Matching is double-blind.** In TQSL's own words, LoTW's
  approach "prevents users from seeing what other users have
  uploaded": you cannot browse what the other station sent and
  adjust your log to match. You find out that a QSO confirmed,
  never what the other side claimed.

TQSL itself is a modest desktop program — one window, three tabs —
plus a batch mode for scripts. It is free, published by the ARRL,
and available for Linux, Windows and macOS. It does not log QSOs
for you (your logging program does that, and exports an **ADIF**
file), it does not operate a radio, and it cannot give you an
identity: the certificate behind the signature comes from the
ARRL, by post if necessary. Chapter 4 walks that request as far
as it can honestly go.

**The check.** Without looking anything up: LoTW is the service
that confirms contacts; TQSL is the signer that makes an upload
provably yours. If that sentence feels obvious, you are ready for
the moving parts.
