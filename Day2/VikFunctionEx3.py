#!/usr/bin/env python

from __future__ import print_function
import re

fila = open("show-ver.txt")
#version = []

def openfile():
    with fila as f:
        version = f.read().splitlines()
        getserial(version)

def getserial(version):
    for line in version:
        if re.search("Processor board ID", line):
            snumber = line.split("Processor board ID")
            snumber = "".join(snumber)
            snumber = snumber.strip()
            print ("The serial number is: " + snumber)


openfile()
fila.close()
