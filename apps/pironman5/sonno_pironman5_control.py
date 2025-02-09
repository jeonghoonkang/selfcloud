
#Author : https://github.com/jeonghoonkang

from pm_auto.pm_auto import PMAuto

### This file run by sudo crontab
### @reboot python3 /home/***/selfcloud/devel_opment/pironman5/sonno_oled.py


config = {
  "peripherals": ['oled','ws2812',],
}

if __name__=="__main__":

  temp1 = config["peripherals"]
  ### print (temp1)

  pm = PMAuto(temp1)
  ### print (pm)

  pm.start()

