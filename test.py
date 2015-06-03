#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK

## Dependencies:    mplayer, argparse, argcomplete, pyYAML
## Author:          Gijs Timmers: https://github.com/GijsTimmers

## Licence:         CC-BY-SA-4.0
##                  http://creativecommons.org/licenses/by-sa/4.0/

## This work is licensed under the Creative Commons
## Attribution-ShareAlike 4.0 International License. To  view a copy of
## this license, visit http://creativecommons.org/licenses/by-sa/4.0/ or
## send a letter to Creative Commons, PO Box 1866, Mountain View,
## CA 94042, USA.

print "Imports testen...",
try:
    import radio
    print "OK"
except Exception as e:
    print "ERROR"
    print e.message, e.args


print "Radio() instantiëren...",
try:
    rd = radio.Radio()
    print "OK"
except Exception as e:
    print "ERROR"
    print e.message, e.args

print "Variabelen testen...",
try:
    rd.parser
    rd.zenderdict
    print "OK"
except Exception as e:
    print "ERROR"
    print e.message, e.args