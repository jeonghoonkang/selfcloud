# -*- coding: utf-8 -*-
# author : http://github.com/jeonghoonkang

import logging
#import logging.config
from logging.handlers import RotatingFileHandler
import sys
import os

class selfdatalogger:
    def __init__(self):
        self.name = 'selfdatalogger'
        self.BNAME = "/home/tinyos/devel_opment/log/"
        self.LOG_FILENAME = None
        self.logger = None

    def set_logger(self, sensor_type):

        # file 이름 정의 
        if sensor_type != None:
            if sensor_type.find('CO2') != -1:
                sensor_type = 'berelogger_' + sensor_type
            elif sensor_type.find('DUST') != -1:
                sensor_type = 'berelogger_' + sensor_type

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
       exit("[bye] you have to write input args ")

    arg=[0 for i in range(num_of_args)]
    for loop_num in range(num_of_args): 
        #print ('##loop_num :', loop_num)
        #print (arg[loop_num])
        arg[loop_num] = sys.argv[loop_num]
    return arg


if __name__ == "__main__":

    args = args_proc()
    berelog('logging cpu temp', args[1])
    
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