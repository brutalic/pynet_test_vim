#!/usr/bin/env python

from __future__ import print_function

dude1 = 'Viktor'
dude2 = 'Tim'
dude3 = 'Graham'

print ("\n{:10}{:10}{:10}\n".format(dude1, dude2, dude3))

dude4 = raw_input("Enter a fourth dude for goodness sakes: ")

print ("\n\n{:10}{:10}{:10}{:10}\n".format(dude1, dude2, dude3, dude4))
print ("Nicely done - you entered another dude's name! Bravo!")
