#!/usr/bin/env python

from __future__ import print_function
from __future__ import unicode_literals
import re

f = open ("show_int_fa4.txt")
output = f.readlines()

for line in output:
    line = line.strip()
    matchinput = re.search(r"(\d+) packets input, (\d+) bytes", line)
    matchoutput = re.search(r"(\d+) packets output, (\d+) bytes", line)
    if matchinput:
        print ("Input Packets: " + matchinput.group(1))
        print ("Input Bytes: " + matchinput.group(2))
    if matchoutput:
        print ("Output Packets: " + matchoutput.group(1))
        print ("Output Bytes: " + matchoutput.group(2))
