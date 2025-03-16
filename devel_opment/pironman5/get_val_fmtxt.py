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


LOG_FILE = "/home/****/devel_opment/log/berelogger_CO2_POC.log" #정확한 경로 지정 필요

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

if __name__ == "__main__" :

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

