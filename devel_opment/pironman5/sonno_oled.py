# Author : https://github.com/jeonghoonkang 

from pm_auto.pm_auto import PMAuto

### This file run by sudo crontab
### @reboot python3 /home/tinyos/devel_opment/selfcloud/devel_opment/pironman5/sonno_oled.py

config = {
  #"peripherals": ['oled','ws2812','gpio_fan','pwm_fan',],
  "peripherals": ['oled',],
}

temp1 = config["peripherals"]
### print (temp1)

pm = PMAuto(temp1)
### print (pm)

### decide what to run
### one shot
pm.stop()
pm.onshot()

### periodic every 1 sec.
#pm.start()
