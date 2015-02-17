[![Build Status](https://travis-ci.org/GijsTimmers/radio.svg)](https://travis-ci.org/GijsTimmers/radio)

[![cc-logo](https://licensebuttons.net/l/by-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-sa/4.0/)


# radio
A small Python script to play various radio stations from a terminal.

## Dependencies:
- `pip`
- `mplayer`
- `argparse`


You can install pip and mplayer via your package manager:

On Ubuntu:
    
    sudo apt-get install python-pip mplayer

On Arch:
    
    sudo pacman -S python2-pip mplayer
    
You can install argparse via `pip`:

    sudo pip install argparse

## Adding other radio stations
There's a dictionary in `radio.py`, called `zenderlijst`. You can edit
this dictionary to add other radio stations. To have command-line access to
these radio stations, be sure to add entries to Radio().zenderparser 
as well.