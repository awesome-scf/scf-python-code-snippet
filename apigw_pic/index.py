# -*- coding: utf8 -*-
import base64

def main_handler(event, context):
    with open("tencent_cloud_logo.png","rb") as f:
        data = f.read()
    base64_data = base64.b64encode(data)    
    base64_str = base64_data.decode('utf-8')
    resp = {
        "isBase64Encoded": True,
        "statusCode": 200,
        "headers": {"Content-Type":"image/png"},
        "body": base64_str
    }
    return resp