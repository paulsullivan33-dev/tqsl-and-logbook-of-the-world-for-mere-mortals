# Glossary

Outcome: every term the guide relies on, defined once, in plain
language — the same definitions the earlier chapters used.

**ADIF** — Amateur Data Interchange Format, the text format
logging programs use to exchange QSO records, one record per
contact in `<TAG:length>value` fields. TQSL's own `.tq5` files
borrow the same field style.

**ARRL** — the American Radio Relay League, the US national
association for amateur radio, which runs Logbook of the World
and issues Callsign Certificates.

**Cabrillo** — the contest log format. TQSL accepts Cabrillo
files as signing input alongside ADIF.

**Callsign Certificate** — the ARRL-issued digital identity that
binds a callsign, a DXCC entity and a QSO date range to a key
pair stored in TQSL. Valid for three years.

**Certificate request (.tq5)** — the file your computer generates
and sends to the ARRL: your details, your address, and the
public half of a new key pair, formatted as a PKCS#10 request.

**Configuration data** — TQSL's signed, separately versioned
lists of DXCC entities, modes, bands and zone rules; version
11.34 was current during this guide's lab.

**DXCC entity** — a country or territory as the DXCC award
programme counts it; a numbered list (1 is Canada) that TQSL's
configuration data translates into names.

**Final Status** — the last line of a signing run
(`Final Status: Success (0)` and eleven other codes), TQSL's
authoritative receipt for batch work.

**Grid square** — a Maidenhead locator: a short code for where
on Earth a station is. Station locations stamp it onto every
signed QSO.

**LoTW (Logbook of the World)** — the ARRL's online service that
receives signed QSO uploads, matches them double-blind against
the other station's uploads, and records confirmations toward
DXCC, VUCC, WAS and WPX awards.

**Pending certificate** — a certificate request TQSL has stored
but the ARRL has not yet answered. It can be displayed, but it
cannot sign, and station locations cannot be built on it.

**PKCS#10** — the standard format for a certificate signing
request: identity details plus a public key, self-signed with
the matching private key to prove possession.

**PKCS#12 (.p12)** — the standard container for a certificate
together with its private key; TQSL's format for moving one
certificate between computers.

**Private key** — the secret half of the key pair, held in
`~/.tqsl/keys/`. Whoever holds it and the matching certificate
can sign as that station.

**QSO** — one logged radio contact between two stations.

**Station Location** — a named set of where-details (grid
square, CQ and ITU zones, IOTA reference, state or county)
attached to a Callsign Certificate and stamped onto signed
QSOs.

**.tbk** — TQSL's backup file: all certificates, station
locations and preferences in one file, written on demand or
automatically on exit.

**.tq6** — the file the ARRL sends back: an issued Callsign
Certificate, ready to load. Configuration updates arrive in the
same container shape.

**.tq8** — a signed log: QSOs stamped with a station location
and signed with a certificate's private key, ready for LoTW.

**ULS** — the FCC's Universal Licensing System database. TQSL
checks United States callsigns against it before building a
certificate request.

**The check.** You have the vocabulary when the sentence "the
.tq6 turned the pending request into a certificate, and the
first .tq8 it signed carried the station location's grid square"
needs no footnotes.
