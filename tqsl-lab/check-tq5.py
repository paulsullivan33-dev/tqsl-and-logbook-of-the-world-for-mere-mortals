#!/usr/bin/env python3
"""check-tq5.py -- read a TQSL certificate request (.tq5) and report what is in it.

A .tq5 file is ADIF-flavoured text: a short header, then fields in the
<TAG:length>value form, one of which holds a PEM certificate request.
This script parses the fields, checks every declared length against the
value actually present, and (when openssl is available) decodes the
embedded PKCS#10 request so you can see the subject and key size TQSL
generated -- without needing a LoTW account or TQSL itself.

Usage: python3 check-tq5.py N0CALL.tq5
"""

import re
import subprocess
import sys

FIELD = re.compile(r"<([A-Za-z0-9_]+):(\d+)>")


def parse_fields(text):
    """Yield (tag, declared_length, value) for each ADIF-style field."""
    pos = 0
    while True:
        m = FIELD.search(text, pos)
        if not m:
            return
        tag, declared = m.group(1), int(m.group(2))
        start = m.end()
        value = text[start:start + declared]
        yield tag, declared, value
        pos = start + declared


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    with open(sys.argv[1], "r", encoding="utf-8", errors="replace") as fh:
        text = fh.read()

    print(f"file: {sys.argv[1]} ({len(text)} bytes)")
    pem = None
    problems = 0
    for tag, declared, value in parse_fields(text):
        if len(value) != declared:
            print(f"  !! {tag}: declared {declared} bytes, found {len(value)}")
            problems += 1
        if tag == "TQSL_CRQ_REQUEST":
            pem = value
            print(f"  {tag}: <PEM certificate request, {declared} bytes>")
        elif tag.startswith("TQSL_"):
            print(f"  {tag}: {value!r}")
    if problems:
        print(f"result: {problems} field length mismatch(es) -- file may be damaged")
        return 1
    print("result: every field length checks out")

    if pem is None:
        print("no TQSL_CRQ_REQUEST field -- this is not a .tq5 request file")
        return 1
    try:
        proc = subprocess.run(
            ["openssl", "req", "-text", "-noout", "-verify"],
            input=pem.encode(), capture_output=True, timeout=30,
        )
    except FileNotFoundError:
        print("openssl not found; skipping the PKCS#10 decode")
        return 0
    out = (proc.stdout + proc.stderr).decode(errors="replace")
    for line in out.splitlines():
        line = line.strip()
        if line.startswith(("Certificate request self-signature verify OK",
                            "Subject:", "Public-Key:", "Signature Algorithm:")):
            print(f"  openssl: {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
