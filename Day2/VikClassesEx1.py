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


object1 = NetworkDevice(ipaddr='6.6.6.6', user='bob', passw='pass')
object2 = NetworkDevice(ipaddr='7.7.7.7', user='dude', passw='pass')
object3 = NetworkDevice(ipaddr='8.8.8.8', user='hey', passw='pass')
object4 = NetworkDevice(ipaddr='9.9.9.9', user='whut!', passw='pass')
