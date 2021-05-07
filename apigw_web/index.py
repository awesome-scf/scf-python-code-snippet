# -*- coding: utf8 -*-
import time

def main_handler(event, context):
    resp = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type":"text/html"},
        "body": "<html><body><h1>Hello</h1><p>Hello World.</p></body></html>"
    }  
    return resp