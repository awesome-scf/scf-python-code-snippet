# -*- coding: utf8 -*-
import time

def main_handler(event, context):
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))   
    return("Hello World")