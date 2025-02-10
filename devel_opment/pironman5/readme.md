## Driver from Sunfounder 
<pre>
Sunfounder 드라이버를 서비스로 등록하지 않고,
로컬 응용SW 영역에서 실행하도록 설정하는 방법 
</pre>
- using open source, pmauto, sf_rpi_status
  - https://github.com/sunfounder/pm_auto
  - util : https://github.com/sunfounder/sf_rpi_status

### run
- PMAuto class which will run peripherals
- <code> sudo python3 sonno_oled.py </code>
  
## Before installation
### require to install, example CLI
- <code>pm_auto</code>, <code>sf_rpi_status</code> git clone 후, 위치 이동 해야함
<pre>
mv pm_auto_main/pm_auto/ .
mv sf_rpi_status_main/sf_rpi_status/ ./
# 패키지들이 동일 디렉토리에 위치해야함. git clone 으로 생성된 디렉토리 하위에 package 위치함. 위치 변경 필요함 
sudo python3 sonno_oled.py 
sudo mv /usr/lib/python3.12/EXTERNALLY-MANAGED /usr/lib/python3.12/EXTERNALLY-MANAGED_OLD
sudo pip3 install smbus2 
sudo pip3 install board
sudo pip3 install adafruit-circuitpython-neopixel
sudo pip3 install adafruit-circuitpython-neopixel-spi
sudo apt-get install python3-dev 
sudo apt-get install python3-rpi.gpio
</pre>

### Thread 실행, One Shot 실행
- Thread 실행, One Shot 실행 파일 다름
- <code> sonno_all_thread.py, sonno_oled.py </code>
    
### Code modification
- pm_auto.py
  - change \_\_init\_\_ parameter which should get moving config=DEFAULT_CONFIG to inside the \_\_init\_\_ function 
  - change to <img width="580" alt="image" src="https://github.com/user-attachments/assets/cd10f814-5b7e-4aca-a5cc-a1ffdb218d0c">

