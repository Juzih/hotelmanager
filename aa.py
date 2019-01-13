# -*- coding:UTF-8 -*-
import MySQLdb as mdb
import tkinter
def connect_mysql():    #连接mysql数据库，老师若想使用请更改db，user，passwd参数为环境里的数据库名和密码
    db_config = dict(host='localhost', port=3306, db='BOAO', charset='utf8', user='BOAO', passwd='19981228')
    cnx = mdb.connect(**db_config)
    return cnx
cnx = connect_mysql()
cus = cnx.cursor()
cus.execute("DROP TABLE IF EXISTS people2")
people2= """create table people2(
        week int not null,
        all_money int,
        room_rate float
        )
"""
cus.execute(people2)
cnx.commit()
cus.execute("DROP TABLE IF EXISTS room2")
room2= """create table room2 (
        room_id char(3) not null,
        cus_name varchar(5),
        id_num char(18),
        cus_phone char(11),
        in_time char(8),
        out_time char(8),
        ats char(2),
        bts char(2),
        cts char(2),
        dts char(2),
        money int,
        money_day int
        )
"""
cus.execute(room2)
cnx.commit()
for i in range(1,8):
    sql="INSERT INTO people2(week,all_money,room_rate)VALUES(%d,%d,%f)"%(i,0,0)
    cus.execute(sql)
    cnx.commit()
sql="INSERT INTO people2(week,all_money,room_rate)VALUES(%d,%d,%f)"%(8,20190108,1)      #通过修改2019****和1这个参数可以调整初始日期和星期
cus.execute(sql)
cnx.commit()
for i in range(101,201):
    a=str(i)
    sql="INSERT INTO room2(room_id,cus_name,id_num,cus_phone,in_time,out_time,ats,bts,cts,dts,money,money_day)VALUES(%s,%s,%s,%s, \
                %s,%s,%s,%s,%s,%s,%d,%d)"%(a,'0','0','0','0','0','0','0','0','0',0,0)
    cus.execute(sql)
    cnx.commit()
cus.close()
cnx.close()