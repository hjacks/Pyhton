
# -*- coding: utf-8 -*-
#!/usr/bin/python 
import datetime
import time
import sys
import pymysql

def get_data():
    day = datetime.date.today()-datetime.timedelta(days=1)
    #print(day)
    sql1 = "select reportdb.func_agg_function_execute('%s');" % day
    cursor.execute(sql1)
    conn.commit()
    #print(day)
    time.sleep(180)
    sql2 = "select reportdb.func_report_function_execute('%s');" % day
    cursor.execute(sql2)
    conn.commit()
    #print (day,' finished-1!')

    sql3 = "select reportdb_ml.func_report_function_execute('%s');" % day
    cursor.execute(sql3)
    conn.commit()

    sql4 = "select reportdb_ms.func_report_function_execute('%s');" % day
    cursor.execute(sql4)
    conn.commit()

if __name__ == '__main__':

    conn = pymysql.connect(db="bmdb", user="", passwd="", host="", port=)
    cursor = conn.cursor()
    get_data()
    cursor.close()
    conn.close()
