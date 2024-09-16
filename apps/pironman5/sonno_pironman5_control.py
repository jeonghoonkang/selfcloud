
#Author : https://github.com/jeonghoonkang

from pm_auto.pm_auto import PMAuto

config = {
  "peripherals": ['oled','ws2812',],
}

if __name__=="__main__":

  temp1 = config["peripherals"]
  ### print (temp1)

  pm = PMAuto(temp1)
  ### print (pm)

  pm.start()
