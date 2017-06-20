#!/usr/bin/env python

from __future__ import print_function


fila = open("testfile.txt")
for line in fila:
    print (line.strip())

fila.close()


fila = open("testfile.txt", 'a')
with fila as append:
    append.write("K'POW!\n")
fila.close()
