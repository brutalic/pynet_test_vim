#!/usr/bin/env python

from __future__ import print_function

def function(x, y, z=5):
    return x + y + z

result1 = function(1, 2, 3)
print ("Three positional arguments: " + str(result1))

result2 = function(x=1, y=2)
print ("Two named arguments: " + str(result2))

result3 = function(1, z=3, y=9)
print ("One positional and two named arguments: " + str(result3))

result4 = function(x='x', y='y', z='z')
print ("Three strings: " + str(result4))

result5 = function(x=['x'], y=['y'], z=['z'])
print ("Three lists: " + str(result5))
