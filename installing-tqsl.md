# Installing TQSL

Outcome: TQSL is installed, you can prove which version you got,
and you know about the one behaviour that surprises everyone —
this program wants a graphical display even for its text options.

## On Ubuntu and Debian

The package is not called `tqsl`; it is called **trustedqsl**.
The lab installed it the ordinary way (transcript `t00`):

```console
$ sudo apt-get update && sudo apt-get install trustedqsl
$ dpkg -s trustedqsl | grep -E '^(Package|Version|Status)'
Package: trustedqsl
Status: install ok installed
Version: 2.7.2-1build3
```

That one package brings the program (`/usr/bin/tqsl`), two manual
pages (`man tqsl` for the command line, `man 5 tqsl` for its
configuration files), and a full set of bundled help pages under
`/usr/share/TrustedQSL/help/` — several chapters of this guide
quote them, because they ship with the program you are running
and describe your version, not somebody else's.

On Windows and macOS, TQSL comes from the ARRL's LoTW pages as a
normal installer (documented-only here; this guide's lab is
Linux). The ARRL also publishes the source, and TQSL will remind
you about newer upstream releases — the lab's 2.7.2 announced
that 2.8.7 was available. A distribution package a few releases
behind upstream is normal and harmless; LoTW accepts the
signatures either way.

## The display surprise

TQSL is a graphical program that happens to accept command-line
options. Without a display it refuses to do anything at all —
even print its version:

```console
$ tqsl -v
Error: Unable to initialize GTK+, is DISPLAY set properly?
(exit status 255)
```

On a desktop this never comes up. On a headless machine, or over
SSH, run it under a virtual display. The lab used `xvfb-run`,
which gives the program a display that exists only in memory:

```console
$ xvfb-run -a tqsl -v
TQSL Version 2.7.2 [unknown]
```

Two honest quirks, measured in transcript `t01` and worth knowing
before they confuse you: under `xvfb-run` those successful query
runs still **exit with status 255**, and `tqsl -n` — "tell me
what's new" — prints its news the same way. The batch *signing*
runs in chapter 7 behave differently: they end with a proper
`Final Status:` line, and there the exit status does mirror the
status code. Judge TQSL by the words it prints, not by its exit
code alone.

## First run

Start `tqsl` and you get three things in order: a Notice asking
you to review the introductory documentation, the bundled help
window, and — because a fresh install has no certificate — an
alert that becomes the subject of the next chapter:

> You have no callsign certificate installed on this computer
> with which to sign log submissions. Would you like to request
> a callsign certificate now?

In this Debian build the bundled help window renders its pages as
raw HTML text rather than formatted pages. It is a cosmetic flaw
in the package's help viewer, not in your install; the same text
reads perfectly well as files under `/usr/share/TrustedQSL/help/`,
and `man tqsl` covers the program itself.

**The check.** `xvfb-run -a tqsl -n` on the lab machine answered
with two pieces of news — a new TQSL release and a new
configuration file (transcript `t01`). When your run prints news,
or politely reports nothing new, your install is alive and
talking to the ARRL's servers.
