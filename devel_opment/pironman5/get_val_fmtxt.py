# -*- coding: utf-8 -*-
# Author : JeongooonKang (github.com/jeonghoonkang)

#import json
import time
import socket
import fcntl
import struct
import os
import sys

import datetime

#import requests
from pytz import timezone


LOG_FILE = "/home/tinyos/devel_opment/log/berelogger_CO2_POC.log" #정확한 경로 지정 필요

def add_usr_func(target_str):
    try:
        with open(LOG_FILE) as m:
            msg = m.read() 
            index = msg.rfind(target_str)
            if index < 0:
                exit( " sonno Problem : can not find string in log file")   
            msg = msg[index-27:] #28 is for the exact position
        print (" original msg \n", msg)
    except IOError as e:
        print ("open error", e)
        exit(0)
    return msg


'''
sample log file
2025-02-18 00:45:04 [INFO] CO2_POC co2 ppm ==> 853
2025-02-18 00:48:04 [INFO] CO2_POC co2 ppm ==> 857
2025-02-18 00:51:04 [INFO] CO2_POC co2 ppm ==> 860
2025-02-18 00:54:04 [INFO] CO2_POC co2 ppm ==> 866
'''
sensor_list = ["CO2_POC", "PM25_DUST"] #if you have more sensor which is suported, add more

def get_value_log(sensor_name):

    if not sensor_name in sensor_list:
        print ("sensor name is not in the list", sensor_list)
        print ("log file probably in the /home/****/devel_opment/log/berelogger_CO2_POC.log")
        exit(0)
    
    _msg = add_usr_func(sensor_name)
    _msg_date = _msg[0:19] 
    if sensor_name == "CO2_POC":
        _ret_msg = _msg[46:50] # we should make proper index
        measure_val = (_ret_msg)

    if _ret_msg[-1:] == '(': # last '(' character should be deleted
        _ret_msg = _ret_msg[:-1]
        measure_val = (_ret_msg)

    return measure_val

if __name__ == "__main__" :


    print (get_value_log("CO2_POC"))
    exit(0)

    _limit = sys.argv[1]  # limit value, 0 means no limit

    monitoring_time = datetime.datetime.now(timezone("Asia/Seoul"))
    
    _msg = add_usr_func("CO2_POC") #get value from log text file

    _msg_date = _msg[0:19] 
    _ret_msg = _msg[46:50] # we should make proper index
    measure_val = (_ret_msg)

    if _ret_msg[-1:] == '(': # last '(' character should be deleted
        _ret_msg = _ret_msg[:-1]
        measure_val = (_ret_msg)

    #print (len(measure_val), measure_val, "int", int(measure_val))

    message = f"========== \n{monitoring_time}\n{_msg_date} CO2 is {measure_val}"
    # message += _msg_date 
    # message += ' PM2.5 is ' + measure_val
    
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

#https://api.telegram.org/bot5049312606:AAFjPh0VYhpxgh-J2VJsjGzP8NW7HAxzxng/sendMessage?chat_id=-1001170927838&text=%EA%B7%B8%EB%A3%B9
#https://api.telegram.org/bot5049312606:AAFjPh0VYhpxgh-J2VJsjGzP8NW7HAxzxng/getUpdates

