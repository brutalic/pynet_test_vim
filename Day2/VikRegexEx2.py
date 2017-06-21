#!/usr/bin/env python

from __future__ import print_function
from pprint import pprint
import re

f = open ("show_mac_multicast.txt")
output = f.readlines()

mydict = {}
macvaluesdict = {}

for line in output:
    line = line.strip()
    macsearch = re.search("(\d+) (ffff.ffff.ffff) (system) (.*)", line)
    if macsearch:
        macaddress = macsearch.group(2)
        vlan = macsearch.group(1)
        systype = macsearch.group(3)
        ports = macsearch.group(4)
        port_list = re.split(r",", ports)
        mydict = {
            macaddress: {
                'vlan': int(vlan), 'type': systype, 'ports': port_list}}
        pprint (mydict)
