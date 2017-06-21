#!/usr/bin/env python

from __future__ import print_function


class NetworkDevice(object):
    def __init__(self, ipaddr, user, passw):
        self.ipaddr = ipaddr
        self.user = user
        self.passw = passw

        self.serial_number = ''
        self.vendor = ''
        self.model = ''
        self.os_version = ''
        self.uptime = ''

    def printip(self):
        print ("IP Address: " + self.ipaddr)
    
    def printcred(self):
        print ("Username: {}\nPassword: {}".format(self.user, self.passw)) 
    
    def vendorname(self, vendor):
        self.vendor = vendor
        print ("Vendor: " + self.vendor)

if __name__ == "__main__":
    object1 = NetworkDevice(ipaddr='6.6.6.6', user='admin', passw='pwd')
    object1.printip()
    object1.printcred()
    object1.vendorname("Juniper")
