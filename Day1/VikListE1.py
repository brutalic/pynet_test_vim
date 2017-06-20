#!/usr/bin/env python

from __future__ import print_function


mylist = ['cloud', 'google it', 3, 5, 22]

print (mylist)

mylisteh = mylist + ['new', 'dude']
print (mylisteh)

mylisteh.pop()
print (mylisteh)


print ("The length of my current list is: " + str(len(mylisteh)))

mylisteh.sort()
print ("This is my sorted list: " + str(mylisteh))
