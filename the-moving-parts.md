# The moving parts

Outcome: given any file or dialog TQSL shows you, you can name
which of the six parts below it belongs to — and spot the one
part that lives on the ARRL's computers, not yours.

**1. Logbook of the World.** The online service: your account, the
matching engine, your confirmations and award standings. TQSL
talks to it, but LoTW is not in the program. Everything else on
this list exists to prepare one trustworthy upload to it.

**2. The Callsign Certificate.** A digital identity binding three
things together: a callsign, a DXCC entity (roughly, a country),
and a range of QSO dates it may sign for. It is created from a
**certificate request** your computer generates, and it becomes
real only when the ARRL issues it back to you. The certificate
has a public half that travels, and a **private key** that stays
in TQSL's data folder (`~/.tqsl/keys/` on Linux) and is the only
thing that can produce your signatures. Certificates are valid
for three years.

**3. The Station Location.** A named description of where the
station was for a set of QSOs: grid square, CQ and ITU zones,
optionally an IOTA island reference and, where they apply, state
and county. TQSL stamps these onto every QSO it signs, so your
partners get correct grid and zone credit. A location is defined
in terms of a certificate — TQSL will not let you create one
until a certificate exists, which the lab confirmed the direct
way (transcript `t06`).

**4. The configuration data.** The lists of DXCC entities, modes,
bands and zone rules are not built into the program. They arrive
as a signed data file, versioned separately from TQSL itself:
this guide's lab ran program 2.7.2 with configuration 11.26, and
accepted an update to 11.34 mid-session when TQSL offered one
(transcript `t04`). When a new entity or mode appears in the
hobby, a configuration update is how TQSL learns about it.

**5. The file family.** TQSL speaks in numbered files, and the
numbers are a timeline:

| File | What it is | Direction |
|---|---|---|
| `.tq5` | A certificate **request** — your details plus a public key | you → ARRL |
| `.tq6` | An **issued certificate** (and also the shape configuration updates arrive in) | ARRL → you |
| `.tq8` | A **signed log** ready for LoTW | you → LoTW |
| `.p12` | One certificate plus its private key, for moving to another computer | you → you |
| `.tbk` | A backup of certificates, station locations and preferences | you → safe place |
| `.adi` / `.log` | Your unsigned log: ADIF from a logging program, or Cabrillo from a contest | input |

**6. TQSL's data folder.** On Linux, `~/.tqsl/` holds `certs/`
(issued certificates), `keys/` (private keys and pending
requests), `certtrash/` (deleted certificates), `config.xml`
(the configuration data), and `uploaded.db` — TQSL's own memory
of what has already been uploaded, which is how it warns you
about duplicates. Treat the whole folder the way you would a
keyring: it *is* your LoTW identity.

**The check.** Cover the table and reconstruct it from the logic:
a request (5) goes out, a certificate (6) comes back, signed logs
(8) go up. If the numbers read as a story rather than a list, you
have the model.
