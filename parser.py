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

import argcomplete              ## Argumenten aanvullen 
import argparse                 ## Parst argumenten
import yaml                     ## Configuratie inlezen
import os                       ## Basislib
import re                       ## Regex

class Parser():
    def __init__(self):
        ## Zenderdictionary aanmaken
        DEFAULT_YAML = os.path.join(os.path.dirname(__file__), "zenders.yml")
        CUSTOM_YAML  = os.path.expanduser("~/.yamlradio.yml")
        
        if os.path.isfile(CUSTOM_YAML):
            ## Load a user-definded yaml file
            loaded_yaml = CUSTOM_YAML
        else:
            ## Load the included yaml file
            loaded_yaml = DEFAULT_YAML
        
        with open(loaded_yaml, "r") as f:
            self.zenderdict = yaml.load(f)
        
        ## Afkortingenlijsten vullen met afkortingen en evt. namen
        self.afkortingenlijst = [combinatie["afk"] \
        for combinatie in self.zenderdict]
        self.afkortingenennamenlijst = [(combinatie["afk"], combinatie ["naam"]) \
        for combinatie in self.zenderdict]
        
        ## Parser instantiëren en de te verwachten argumenten meegeven
        self.parser = argparse.ArgumentParser(prog="libre-yamlradio.py",
                formatter_class=argparse.RawTextHelpFormatter,
#                usage="joo",
                description="Python script to play various radio stations from a terminal:\n\n",
                epilog="This program is free software, and you are welcome to redistribute it under the \n" + 
                "condititions of the CC-BY-SA license. Try 'libre-yamlradio --license' for more info."
                )      
        #,usage=self.helpoutput())#(usage="jooo")#(usage=self.helpoutput(), add_help=False)
        self.parser.add_argument('zender', metavar="CHANNEL",choices=self.afkortingenlijst,
            help="one of the following radio channel abbreviations:\n" + self.dump_channels())
        
        self.parser.add_argument("-v", "--version", action="store_true", help="show version number and exit")
        self.parser.add_argument("-l", "--license", action="store_true", help="show license info and exit")
        self.parser.add_argument("--yaml-path", action="store_true", help="path to a custom yaml config file")
        
        group = self.parser.add_argument_group('communicator arguments').add_mutually_exclusive_group()
        group.add_argument("-r", "--raw", help="dump raw ICY info", action="store_true")
        group.add_argument("-t","--plaintext", help="show non-formatted (fine-grained) ICY info", action="store_true")
        group.add_argument("-c","--color", help="show formatted (fine-grained) ICY info", action="store_true")
        
    def zendervinden(self):
        ## De ingevoerde argumenten parsen
        argcomplete.autocomplete(self.parser)
        argumenten = self.parser.parse_args()
        for combinatie in self.zenderdict:
            if combinatie["afk"] == argumenten.zender:
                naam = combinatie["naam"]
                url  = combinatie["url"]
                
                if re.match("\d", combinatie["afk"][0]):
                    comm = "_" + combinatie["afk"]
                else:
                    comm = combinatie["afk"]
                    
        return (naam, url, comm)    
    
    def dump_channels(self, name=None):
        SPACING = 2
        INDENT = 1
        text=""
        abrv_col_width = max([len(afk) for afk in self.afkortingenlijst]) + SPACING
        
        for c in self.afkortingenennamenlijst:
            text += (INDENT * " " + \
            c[0] + \
            ((abrv_col_width - len(c[0])) * " " ) + \
            c[1] + \
            "\n")
        return text
