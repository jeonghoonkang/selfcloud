# OLED, LED driver for Pironman5 sunfounder case
- using PMAuto class for run hardware peripherals
- should have pmauto, and sf_rpi_status package
  - https://github.com/sunfounder/pm_auto
  - https://github.com/sunfounder/sf_rpi_status  

## Detials of installation and run (some part of drivers .. )
- https://github.com/jeonghoonkang/selfcloud/tree/main/devel_opment/pironman5
- Thermal Fan is supported and run by default RaspberryPi5 driver
- In some case, there are system panic down from systemctl management of PIRONMAN5
  - thus SONNO will use periodic application run for safe long-time running   

## Installation SUNFOUNDER SW Pironman5
- Pironman5 sometimes (not always) crashes (system down)  when restart Pironman5 service by systemctl
<pre>
cd ~
git clone https://github.com/sunfounder/pironman5.git
cd ~/pironman5
sudo python3 install.py
</pre>

![image](https://github.com/user-attachments/assets/f943ac93-7123-4d93-b1f8-596483766a10)


- Web dashboard port : 34001
- influxdb : 8086

## pm_auto.py modification
- what to do : replace pm_auto.py file which is installed by pironman5 installation
- download : https://raw.githubusercontent.com/jeonghoonkang/selfcloud/refs/heads/main/apps/pironman5/pm_auto.py
- location dir : /opt/pironman5/venv/lib/python3.12/site-packages/pm_auto
- which shows different displays 

## OLED size
- ![image](https://github.com/user-attachments/assets/484dfc7d-4c47-4061-be40-3ac90994206e)
