#!/usr/bin/env python
# coding=utf-8

import MySQLdb
import MySQLdb.cursors

conn = MySQLdb.connect(host='182.92.223.12', user='wzjg520',port=3306, passwd='ABC201314', db='mall', charset='utf8')

cursor = conn.cursor(MySQLdb.cursors.DictCursor)

sql = 'select * from mall_nav;'

cursor.execute(sql)

ret = cursor.fetchall()
for  v in ret:
    print v['info']
