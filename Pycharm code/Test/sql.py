#!/Users/env python
# -*- coding:utf-8 -*-
# @author：麟听 WeChat:15019763969
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="Linting",
    passwd="34222220",
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)
# mycursor.execute("CREATE TABLE sites(name VARCHAR(255),url VARCHAR(255))")

