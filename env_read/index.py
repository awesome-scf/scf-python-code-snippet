# -*- coding: utf8 -*-
import os

def main_handler(event, context):
    print(os.environ)
    print(os.environ.get("SCF_RUNTIME"))
    return("Hello World")