#!/usr/bin/env python2
import nxt.locator
sock = nxt.locator.find_one_brick()
if sock:
   brick = sock.connect()
   name, host, signal_strength, user_flash = brick.get_device_info()
   print 'NXT brick name: %s' % name
   print 'Host address: %s' % host
   print 'Bluetooth signal strength: %s' % signal_strength
   print 'Free user flash: %s' % user_flash
   sock.close()