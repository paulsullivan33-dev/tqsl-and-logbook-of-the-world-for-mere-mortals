# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab used the hobby's dummy callsign, N0CALL, a fictitious
   name and address, and an example.com email address.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** The Limits chapter names what the
   tool cannot do: a pending request is not a certificate and
   nothing can be signed or located until the ARRL issues one;
   United States requests are gated by an FCC database check a
   new licence can fail for a day; certificates sign only a
   fixed date window and expire after three years, with early
   renewal invalidating the old one; the request flow leaves
   the private key unencrypted on disk; matching is double-blind
   so a missing confirmation explains nothing; and the program
   needs a display even for queries and exits 255 on runs that
   succeeded.
8. **The credential line is in the text, early.** A Callsign
   Certificate is a cryptographic identity tied to a real
   amateur licence, and the README and chapter 4 state the rule
   before any procedure depends on it — request a certificate
   only for a callsign you hold, keep its private key on your
   own machine, and never handle another operator's certificate
   or key. The lab requested nothing for any real callsign and
   uploaded nothing to LoTW.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is an Ubuntu 24.04 (noble) sandbox. TQSL was
installed from the distribution package **trustedqsl
2.7.2-1build3**, which provides TQSL **2.7.2** and its bundled
help; the ARRL's upstream 2.8.7 release was announced by the
program during the lab and deliberately not installed, so every
quoted behaviour is the packaged version's. The GUI was run
under a virtual display (Xvfb) with a throwaway home directory,
so the first-run experience is a genuinely fresh one; dialog
texts in transcripts `t03`, `t04` and `t06` are transcribed
verbatim from that session, and every dialog claim is paired
with file evidence from the shell. All transcripts live in
`tqsl-lab/transcripts/`; the fixtures are `tqsl-lab/N0CALL.tq5`
and `tqsl-lab/sample-log.adi`, and the measuring script is
`tqsl-lab/check-tq5.py`.

Run for real, with transcripts as evidence:

- Installation by apt, and the package's inventory: the `tqsl`
  binary, both manual pages, and the bundled help tree (t00).
- Version and news queries under a virtual display, including
  the finding that successful `-v`/`-n` runs exit 255, and the
  two announcements (release 2.8.7, configuration 11.34) (t01);
  the full `-h` option list (t02).
- The first-run sequence (Notice, help window, no-certificate
  alert) and the complete certificate-request wizard for
  N0CALL: the FCC ULS refusal for a United States entity, the
  refusal of entity NONE, the field validations, and a finished
  request paired with the CANADA entity, saved as a 1,164-byte
  `.tq5` and **not** uploaded when the wizard offered (t03).
- The pending request's footprint: the private key file in
  `~/.tqsl/keys/`, the Certificates tab grouping ("awaiting
  ARRL approval"), and the Properties dialog, including
  "Passphrase: None" (t03, t04).
- The main window mapped — menus, three tabs, Status Log — and
  the configuration-data update from 11.26 to 11.34 accepted
  and verified on disk (`config.tq6`, `config.xml` header), plus
  the automatic `.tbk` backups written on exit (t04).
- The request file taken apart by the lab's own script and by
  OpenSSL: every field length valid; the PKCS#10 subject with
  the callsign in OID 1.3.6.1.4.1.12348.1.1; a 1024-bit RSA key;
  sha256WithRSAEncryption; self-signature verified (t07).
- The walls, hit on purpose: station-location creation refused
  three ways with `No certificates available` (GUI tab, GUI
  menu, batch `-s`), and batch signing refused with "The
  selected station location could not be found" and `Final
  Status: Command Syntax Error(10)`, exit status 10 (t05, t06).

Documented only — described from TQSL's bundled help, its
manual pages and its dialogs, not run, and the text does not
claim otherwise:

- LoTW account creation and the ARRL's identity checks — the
  postcard validation code mailed to a US licensee's FCC
  address, and the posted-documents route for most other
  countries.
- The `.tq6` certificate arriving by email and being loaded,
  turning the pending request into an active certificate.
- The station-location dialog's fields and procedure.
- A successful signing run and the `.tq8` it produces, uploads
  by all three routes, and LoTW's matching and confirmations.
- Renewal of a certificate, and saving or loading a single
  certificate as a `.p12`.
- The neighbour systems of the neighbours chapter (eQSL, QRZ
  Logbook, Club Log, paper cards) — characterised, not used.

Fixtures are this guide's own and deliberately generic: the
dummy callsign N0CALL (which no authority can issue a
certificate for), the fictitious Alex Example of Exampleton
with an example.com address, and a two-QSO sample log in which
N0CALL works N0CALL in grid square FN31, labelled in the file
itself as existing to exercise the signer. No real callsign, no
real person's details, and nothing was uploaded anywhere.
