# OLED, LED driver for Pironman5 sunfounder case
- using PMAuto class for run hardware peripherals
- should have pmauto, and sf_rpi_status package
  - https://github.com/sunfounder/pm_auto
  - https://github.com/sunfounder/sf_rpi_status  

## Detials of installation and run (just OLED driver)
- https://github.com/jeonghoonkang/selfcloud/tree/main/devel_opment/pironman5
- Thermal Fan is supported and run by default RaspberryPi5 driver 

## Installation SUNFOUNDER SW Pironman5
- Pironman5 sometimes (not always) crashes (system down)  when restart Pironman5 service by systemctl
<pre>
cd ~
git clone https://github.com/sunfounder/pironman5.git
cd ~/pironman5
sudo python3 install.py
</pre>

- Web dashboard port : 34001
- influxdb : 8086
