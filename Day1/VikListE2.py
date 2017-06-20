#!/usr/bin/env python

from __future__ import print_function


ipadd = "10.1.2.666"
ipaddlist = ipadd.split(".")
print ("This is just an IP: " + str(ipaddlist))

#remove the last element
ipaddlist.pop()

#add a new element
ipaddlist.append('0')

print ("This is the network version list: " + str(ipaddlist))

ipaddbinary = []
ipaddbinary.append(bin(int(ipaddlist[0])))
ipaddbinary.append(bin(int(ipaddlist[1])))
ipaddbinary.append(bin(int(ipaddlist[2])))
ipaddbinary.append(bin(int(ipaddlist[3])))
print ("This is the network binary version: " + str(ipaddbinary))
#print (ipaddbinary)
