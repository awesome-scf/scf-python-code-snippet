# -*- coding: utf8 -*-
import requests


def main_handler(event, context):
    addr = "https://cloud.tencent.com"    
    resp = requests.get(addr)
    print(resp)
    print(resp.text)
    return resp.status_code
