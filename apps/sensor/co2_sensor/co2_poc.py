
# Author : https://github.com/jeonghoonkang

# http://www.eltsensor.co.kr/products-by-gas/co2/ndir/monitor?tpf=product/view&category_code=101012&code=22
# Mac OSX /dev/cu.usbserial-D200A1RU 

# sudo python3 $(realpath ./co2_poc.py)
# sudo crontab 
# */3 * * * *     python3 /home/***t/selfcloud/apps/sensor/co2_sensor/co2_poc.py

import serial
import time
import sys

BNAME = "/home/tinyos/devel_opment/"
LOG_DIR = BNAME + "selfcloud/apps/log"

sys.path.append(LOG_DIR)

import berepi_logger


def find_ppm(ins):
    print ('RAW string',ins)
    
    #ix = ins.find(10) #find '/n' 
    #print ('ix', ix, type(ix), ins[ix:ix+1])

    stnum = 0
    if ins[0] == 0xF1 and ins[1] == 0xF2 and ins[2] == 0x02 :
        stnum = ins[3] * 256 + ins[4]
    else :
        print ('error in data')
        return None
                
    ret = stnum
    print ('...', stnum, 'ppm') #ppm print
    return ret


def pass2file(ins):
    print("...logging...", )
    print(time.strftime("%Y-%m-%d %H:%M"),)  
    sensor_type='CO2_POC'
    berepi_logger.berelog('co2 ppm', str(ins), sensor_type)

if __name__ == "__main__":
    if len(sys.argv) > 1 :
        port = sys.argv[1]    
    else :
        port = '/dev/ttyUSB0'
        print ("using port ", port)
        
    print (' open port ', port )
    op = serial.Serial(port, baudrate=9600, rtscts=True)
    time.sleep(3) 

    rq_str = b"\xF1\xF2\x01\x1C"
    op.write(rq_str)
    in_string = op.read(size=8)
    ppm = find_ppm(in_string)

    if ppm == None :
        in_string = op.read(size=8)
        ppm = find_ppm(in_string)
    
    if ppm == None :
        print ('error in data')
        exit(__file__ + " [X] error in data")

    pass2file(ppm)

    exit(__file__ + " [O] all done...")
    
