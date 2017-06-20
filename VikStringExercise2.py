#!/usr/bin/env python

from __future__ import print_function
import time

ipadd = raw_input("Enter an IP address... please: ")
ipadd = ipadd.split('.')

#The star specifies that you can read the split as each element the way it's formatted
print ("\n{:>12}{:>12}{:>12}{:>12}\n".format(*ipadd))
print ("It worked... ")
time.sleep(1)
print("good... ")
time.sleep(1)
print ("job...")
time.sleep(1)
