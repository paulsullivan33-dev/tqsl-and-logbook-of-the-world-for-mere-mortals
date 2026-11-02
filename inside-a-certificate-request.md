# Inside a certificate request

Outcome: you can open a `.tq5` file — it is plain text — and
explain every part of it, including how to verify with a script
that the request is whole and that its embedded key material is
real. This is the chapter where the lab takes its own artifact
apart; the specimen is `tqsl-lab/N0CALL.tq5`, the request the
previous chapter produced.

## The shape of the file

A `.tq5` is **ADIF-flavoured text**: a title line, then fields in
ADIF's `<TAG:length>value` form, closed by `<eor>`. TQSL's own
checker in the lab, `tqsl-lab/check-tq5.py`, parses those fields,
verifies that every value really is as long as its tag declares,
and decodes the cryptographic payload with OpenSSL. Its report
(transcript `t07`):

```console
$ python3 tqsl-lab/check-tq5.py tqsl-lab/N0CALL.tq5
file: tqsl-lab/N0CALL.tq5 (1164 bytes)
  TQSL_IDENT: 'TQSL: 2.7.2, Lib: V2.5, Config: 11.26'
  TQSL_CRQ_PROVIDER: 'American Radio Relay League'
  TQSL_CRQ_PROVIDER_UNIT: 'Logbook of the World'
  TQSL_CRQ_EMAIL: 'alex@example.com'
  TQSL_CRQ_NAME: 'Alex Example'
  TQSL_CRQ_ADDRESS1: '123 Example Street'
  TQSL_CRQ_ADDRESS2: ''
  TQSL_CRQ_CITY: 'Exampleton'
  TQSL_CRQ_STATE: 'Ontario'
  TQSL_CRQ_POSTAL: 'A1A 1A1'
  TQSL_CRQ_COUNTRY: 'Canada'
  TQSL_CRQ_DXCC_ENTITY: '1'
  TQSL_CRQ_QSO_NOT_BEFORE: '2020-01-01'
  TQSL_CRQ_REQUEST: <PEM certificate request, 615 bytes>
result: every field length checks out
  openssl: Subject: 1.3.6.1.4.1.12348.1.1 = N0CALL, CN = Alex Example, emailAddress = alex@example.com
  openssl: Public-Key: (1024 bit)
  openssl: Signature Algorithm: sha256WithRSAEncryption
  openssl: Certificate request self-signature verify OK
```

Four things are worth understanding here.

**The ident line is a fingerprint of the sender's setup.**
`TQSL: 2.7.2, Lib: V2.5, Config: 11.26` records the program
version, the version of the underlying signing library, and the
configuration-data version (chapter 2) in force when the request
was made. When the ARRL or a help forum asks "what are you
running?", this line is the complete answer.

**The entity is a number.** `TQSL_CRQ_DXCC_ENTITY: '1'` — 1 is
Canada in the DXCC numbering. The friendly names in the wizard
are TQSL's configuration data translating numbers it actually
works with.

**The request is a standard PKCS#10.** The
`TQSL_CRQ_REQUEST` field holds a PEM `CERTIFICATE REQUEST` — the
same object a web server administrator would send to a
certificate authority. Its subject carries the name and email
from the wizard, and the callsign itself rides in a dedicated
attribute, OID `1.3.6.1.4.1.12348.1.1`. OpenSSL verifies the
request's self-signature: whoever holds the matching private key
made this request, and the contents were not altered on the way.

**The key is 1024-bit RSA.** That is what this TQSL version
generates for a request. It is smaller than current fashion for
web certificates; it is also what LoTW's system is built around,
key sizes are the ARRL's design choice, and the practical
protection for your identity is the postal check in chapter 4
plus the privacy of the key file — not key length alone.

## The half that stays home

The `.tq5` holds only the **public** key. At the same moment the
wizard saved it, TQSL wrote `~/.tqsl/keys/N0CALL`: a sibling
file in the same field format whose last field is
`<PRIVATE_KEY:916>` containing an unencrypted PEM private key,
with the folder permissions (0700 on `~/.tqsl`) as its only
protection, because this request flow sets no passphrase.

Two rules follow, and they are the security core of the whole
guide:

- **The `.tq5` is safe to send; the keys folder is not.** Email
  the request anywhere. Never copy, upload or share
  `~/.tqsl/keys/` — anyone holding that file plus the issued
  certificate can sign as your station.
- **If the keys folder dies before the `.tq6` arrives, the
  request dies with it.** The issued certificate is useless
  without its matching private key. The fix is a fresh request;
  the prevention is the backup habit in chapter 9.

**The check.** Run the checker on the lab's request and read the
last lines: every length checks out, and OpenSSL reports the
self-signature valid. Then run it on your own `.tq5` before you
submit it — a request that fails either test was damaged in
transit, and the ARRL cannot issue from it.
