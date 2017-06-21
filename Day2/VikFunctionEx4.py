#!/usr/bin/env python

from __future__ import print_function
import re

fila = open("show-ver.txt")
#version = []

def openfile():
    with fila as f:
        version = f.read().splitlines()
        getvendor(version)
        getmodel(version)
        getos(version)
        getserial(version)
        getuptime(version)

def getmodel(version):
    for line in version:
        model = re.search("Cisco (\d+) .*", line)
        if model:
            print ("The model is: " + model.group(1))

def getos(version):
    for line in version:
        version = re.search("Cisco IOS Software.*, Version (.*), ", line)
        if version:
            print ("The version is: " + version.group(1))

def getserial(version):
    for line in version:
        snumber = re.search("Processor board ID (.*)", line)
        if snumber:
            print ("The serial number is: " + snumber.group(1))

def getvendor(version):
    for line in version:
        if re.search("Cisco 881", line):
            snumber = line.split("881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.")
            snumber = "".join(snumber)
            snumber = snumber.strip()
            print ("The vendor is: " + snumber)

def getuptime(version):
    for line in version:
        uptime = re.search(".*uptime is (.*)", line)
        if uptime:
            print ("The uptime is: " + uptime.group(1))


openfile()
fila.close()
