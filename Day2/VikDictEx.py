#!/user/bin/env python

from __future__ import print_function

netdevice = {}

netdevice['username'] = 'root'
netdevice['ipadd'] = '10.1.1.10'
netdevice['password'] = 'passme'
netdevice['vendor'] = 'juniper'
netdevice['model'] = 'ex4200-f'

for key, val in netdevice.items():
    print (key, val)

netdevice['password'] = 'newpass'
netdevice['secret'] = 'secretstuff'

device_type = netdevice.get('device_type', 'cisco_ios')
print("\nDevice type: {}\n".format(device_type))
