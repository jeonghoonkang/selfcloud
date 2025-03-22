
#Author : https://github.com/jeonghoonkang

import os, sys

sys.path.append('/home/tinyos/devel_opment/pironman5/pm_auto')

from pm_auto import PMAuto


### This file run by sudo crontab
### @reboot python3 /home/***/selfcloud/devel_opment/pironman5/sonno_oled.py


config = {
  "peripherals": ['oled'],
}

def find_module_path(module_name):
    for path in sys.path:
        module_path = os.path.join(path, module_name)
        if os.path.exists(module_path + '.py') or os.path.exists(os.path.join(module_path, '__init__.py')):
            return module_path
    return None


if __name__=="__main__":

  print (sys.path)

  name = 'pm_auto'
  module_path = find_module_path(name)
  if module_path:
      print( name + f" is found at: {module_path}")
  else:
      exit ("error in the path, no module found")

  temp1 = config["peripherals"]
  ### print (temp1)

  pm = PMAuto(temp1)
  print (pm)

  pm.onshot()

