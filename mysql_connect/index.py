# -*- coding: utf8 -*-
import pymysql

def main_handler(event, context):
        
    # 打开数据库连接
    db = pymysql.connect(host="host ip",port=3306,user="user",password="password",database="db name")
    
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    
    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("SELECT VERSION()")
    
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    
    print ("Database version : %s " % data)
    
    # 关闭数据库连接
    db.close()
    