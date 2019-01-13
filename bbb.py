#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb as mdb
import datetime
def connect_mysql():
    db_config = dict(host='localhost', port=3306, db='BOAO', charset='utf8', user='BOAO', passwd='19981228')
    try:
        cnx = mdb.connect(**db_config)
    except Exception as err:
        raise err
    return cnx
def date_caculate(j,k):
    if k!=1:
        d1=datetime.datetime.strptime(j, '%Y%m%d')
        d2 = datetime.datetime.strptime(k, '%Y%m%d')
        delta=d1-d2
        return int(delta.days)
    else:
        d1 = datetime.datetime.strptime(j, '%Y%m%d')
        delta = datetime.timedelta(days=k)
        n_days = d1 + delta
        return n_days.strftime('%Y%m%d')

def sql(list):
    if list[0]=='0':
        return full()
    if list[0]=='1':
        cnx = connect_mysql()
        cus = cnx.cursor()
        room = "SELECT * FROM room2 WHERE money =%d"%(0)
        cus.execute(room)
        b=str(cus.fetchone()[0])
        cus.close()
        cnx.close()
        checkin(b,list)
        return 1
    if list[0]=='2':
        return checkout(list)
    if list[0]=='3':
        continued(list)
        return 1
    if list[0] == '4':
        return day_pass()
    if list[0]=='5':
        eat(list)
        return 1
    if list[0]=='6':
        return money()
    if list[0]=='7':
        return rate()
    if list[0]=='8':
        return money_people()
def full():
    cnx = connect_mysql()
    cus = cnx.cursor()
    room = "SELECT * FROM room2 WHERE cus_name =%s"%('0')
    cus.execute(room)
    results = cus.fetchone()
    cus.close()
    cnx.close()
    if results:
        return 1
    else:
        return 0
def checkin(b,list):
    cnx = connect_mysql()
    cus = cnx.cursor()
    c=(date_caculate(list[5],list[4]))*150
    room="update room2 set cus_name='%s',id_num='%s',cus_phone='%s',in_time='%s', \
        out_time='%s',ats='%s',bts='%s',cts='%s',dts='%s',money='%d', \
        money_day='%d'" %(list[1], list[2], list[3], list[4],list[5],'0','0','0','0',c,c)+"where room_id = '%s'" %(b)
    cus.execute(room)
    cnx.commit()
    cus.close()
    cnx.close()
def checkout(list):
    cnx = connect_mysql()
    cus = cnx.cursor()
    room = "SELECT * FROM room2 WHERE room_id ='%s'" % (list[1])
    cus.execute(room)
    d = cus.fetchone()
    room = "UPDATE  room2 SET cus_name= '%s' , id_num= '%s', cus_phone = '%s',in_time = '%s', \
            out_time ='%s',ats='%s',bts='%s',cts='%s',dts='%s',  \
            money='%d'" % ('0','0','0','0','0','0','0','0','0',0) + "where room_id = '%s'" % (list[1])
    cus.execute(room)
    cnx.commit()
    cus.close()
    cnx.close()
    return d[10]
def continued(list):
    cnx = connect_mysql()
    cus = cnx.cursor()
    room = "SELECT * FROM room2 WHERE room_id ='%s'"%(list[1])
    cus.execute(room)
    d=cus.fetchone()
    c=(date_caculate(d[5],list[2])*150)+d[10]
    b=(date_caculate(d[5],list[2])*150)+d[11]
    room = "UPDATE  room2 SET out_time ='%s',money='%d',money_day='%d'" % (list[2],c,b) + "where room_id = '%s'" % (list[1])
    cus.execute(room)
    cnx.commit()
    cus.close()
    cnx.close()
def eat(list):
    cnx = connect_mysql()
    cus = cnx.cursor()
    room = "SELECT * FROM room2 WHERE room_id ='%s'" % (list[1])
    cus.execute(room)
    d = cus.fetchone()
    da=str(int(d[6])+int(list[2][0]))
    db = str(int(d[7]) + int(list[2][1]))
    dc = str(int(d[8]) + int(list[2][2]))
    dd = str(int(d[9]) + int(list[2][3]))
    c=(int(list[2][0])*10+int(list[2][1])*8+int(list[2][2])*15+int(list[2][3])*20)+d[10]
    b=(int(list[2][0])*10+int(list[2][1])*8+int(list[2][2])*15+int(list[2][3])*20)+d[11]
    room = "UPDATE  room2 SET ats='%s',bts='%s',cts='%s',dts='%s',  \
            money='%d',money_day='%d'" % (da,db,dc,dd,c,b) + "where room_id = '%s'" % (list[1])
    cus.execute(room)
    cnx.commit()
    cus.close()
    cnx.close()
def day_pass():
    cnx = connect_mysql()
    cus = cnx.cursor()
    sqlo = "select * from people2 where week = '%d'" % (8)
    cus.execute(sqlo)
    m= str(cus.fetchone()[0])
    n=cus.fetchone()[1]
    if n>=8:
        n=1
        for i in range(1,8):
            sqln = "UPDATE  people2 SET all_money ='%d',room_rate='%f'" % (0,0) + "where week = '%d'" % (i)
            cus.execute(sqln)
            cnx.commit()
    m=date_caculate(m,1)
    sql1="select sum(money) from room2 where money_day<>'%d'"%(0)
    cus.execute(sql1)
    p=cus.fetchone()[0]
    if p is not None:
        b=int(p)
    else:
        b=0
    sql2="select * from room2 where money<>'%d'"%(0)
    cus.execute(sql2)
    result= cus.fetchall()
    c=float(len(result))/100
    sqll="UPDATE  people2 SET all_money ='%d',room_rate='%f'" % (b,c) + "where week = '%d'" % (n)
    cus.execute(sqll)
    cnx.commit()
    sqlm="select * from room2 where out_time<=%s and out_time<>%s"%(m,'0')
    cus.execute(sqlm)
    results = cus.fetchall()
    d=[]
    for row in results:
        d.append(row[0])
    for i in range(101, 201):
        q=str(i)
        sqln = "UPDATE  room2 SET money_day ='%d'" % (0) + "where room_id = '%s'" % (q)
        cus.execute(sqln)
        cnx.commit()
    m=int(m)+1
    n=n+1
    sqql="UPDATE  people2 SET all_money ='%d',room_rate='%f'" % (m,n) + "where week = '%d'" % (8)
    cus.execute(sqql)
    cnx.commit()
    cus.close()
    cnx.close()
    return d
def money():
    cnx = connect_mysql()
    cus = cnx.cursor()
    sql="select * from people2 "
    cus.execute(sql)
    results = cus.fetchall()
    d = []
    for row in results:
        d.append(row[1])
    return d
def rate():
    cnx = connect_mysql()
    cus = cnx.cursor()
    sql="select * from people2 "
    cus.execute(sql)
    results = cus.fetchall()
    d = []
    for row in results:
        d.append(int(row[2]))
    return d
def money_people(list):
    cnx = connect_mysql()
    cus = cnx.cursor()
    sql = "select * from room2 where room_id='%s'"%(list[1])
    cus.execute(sql)
    results = cus.fetone()
    d=results[10]
    return d