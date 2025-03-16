# -*- coding: utf-8 -*-
# author : http://github.com/jeonghoonkang

import logging
#import logging.config
from logging.handlers import RotatingFileHandler
import sys
import os

import socket
import fcntl
import struct
import pytz

import datetime


class selfdatalogger:
    def __init__(self):
        self.name = 'selfdatalogger'
        self.BNAME = "/home/tinyos/devel_opment/log/"
        self.LOG_FILENAME = None
        self.logger = None

    def set_logger(self, sensor_type):

        # file 이름 정의 
        # Sensor type에 따라서 파일 이름이 다르게 설정, such as CO2_POC
        if sensor_type != None:
            if sensor_type.find('CO2') != -1:
                sensor_type = 'berelogger_' + sensor_type
            elif sensor_type.find('DUST') != -1:
                sensor_type = 'berelogger_' + sensor_type
            elif sensor_type.find('TEST') != -1:
                sensor_type = 'berelogger_' + sensor_type
        else:
            sensor_type = 'berelogger_' + 'No_sensor_type'

        self.LOG_FILENAME = self.BNAME + sensor_type + ".log"

        if not os.path.exists(self.LOG_FILENAME):
            log_directory = os.path.dirname(self.LOG_FILENAME)

            # Create directory if it does not exist
            if log_directory and not os.path.exists(log_directory):
                os.makedirs(log_directory)

            with open(self.LOG_FILENAME, 'w') as file :
                file.close()

        self.logger = logging.getLogger('BereLogger')
        self.logger.setLevel(logging.DEBUG)

        # Choose TimeRoatatingFileHandler or RotatingFileHandler 
        #handler = logging.handlers.TimedRotatingFileHandler(filename=LOG_FILENAME, when="midnight", interval=1, encoding="utf-8")
        handler = logging.handlers.RotatingFileHandler(self.LOG_FILENAME, mode='a', maxBytes=2000000, backupCount=9)  # 2메가 파일 10개 까지 저장 (1년정도 데이터양)
        handler.formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        self.logger.addHandler(handler)

    def berelog(self, msg_name, value=None, sensor_type=None):

        if (value == None):
            self.logger.info(msg_name )
        elif (value != None):
            self.logger.info( sensor_type + msg_name + ' ==> ' + value)
            print ("logging to", self.LOG_FILENAME, 'log file name', value)


def args_proc():
 
    num_of_args = len(sys.argv)
    if num_of_args < 2:
       print('current number of args -->  ', num_of_args )
       exit("[bye] you have to write input args for test")

    arg=[0 for i in range(num_of_args)]
    for loop_num in range(num_of_args): 
        #print ('##loop_num :', loop_num)
        #print (arg[loop_num])
        arg[loop_num] = sys.argv[loop_num]
    return arg


if __name__ == "__main__":

    args = args_proc()

    log = selfdatalogger()
    log.set_logger('TEST')

    log.berelog('logging test value', args[1], 'TEST')
    
    # 'application' code
    #logger.debug('debug message')
    #logger.info('info message')
    #logger.warn('warn message')
    #logger.error('error message')
    #logger.critical('critical message')
    """
      if you want to use, this berepi_logger
      import logging, and use berelog('*****')
    """


'''
To do:
    LOG_FILENAME has to have sensor name on the file name
'''

''' 




LOG_FILE = "/home/tinyos/logs/berelogger.log" #정확한 경로 지정 필요

def add_usr_func(target_str):
    with open(LOG_FILE) as m:
        msg = m.read() 
        index = msg.rfind(target_str)
        if index < 0:
            exit( " Problem : can not find string in log file")   
        msg = msg[index-28:] #28 is for the exact position
    #print (" original msg \n", msg)
    return msg

if __name__ == "__main__" :

    _limit = sys.argv[1]  # limit value

    monitoring_time = datetime.datetime.now(timezone("Asia/Seoul"))
    
    _msg = add_usr_func("PM2.5 Dust")
    _msg_date = _msg[0:19] 
    _ret_msg = _msg[39:42] # we should make proper index
    measure_val = (_ret_msg)

    if _ret_msg[-1:] == '(': # last '(' character should be deleted
        _ret_msg = _ret_msg[:-1]
        measure_val = (_ret_msg)

    #print (len(measure_val), measure_val, "int", int(measure_val))

    message = "========== \n" + f"""{monitoring_time}""" +"\n"
    message += _msg_date 
    message += ' PM2.5 is ' + measure_val
    
    #print (_limit)
    #print (int(dust))
    try:
        if int(measure_val) < int(_limit): 
            exit(0) # shell 연동시, no output 조건을 만들기 위해서 미리 종료 
            print (' measure is under limit < ', _limit)
    except ValueError :
        print (ValueError)
        print ("Exception int value,", _ret_msg ,"20:23", __file__)
        print ("Exception int value,", _msg , __file__)
        exit(0)

    print (message)
    #print ("finish end, good bye .... ")


2025-02-18 07:15:04 [INFO] CO2_POC co2 ppm ==> 1023


'''
