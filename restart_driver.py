import time

import uiautomator2 as u2

d = u2.connect('5921d37d')

# d.service('uiautomator').stop()
d.uiautomator.stop()
time.sleep(5)
d.uiautomator.start()
# d.service('uiautomator').start()
time.sleep(10)
