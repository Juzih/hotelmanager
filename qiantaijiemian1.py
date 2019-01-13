#coding=utf-8
import tkinter
import tkinter.messagebox
from qiantaigeshiyanzheng import *
import bbb as b
"""
本程序中有指令01234
"""

def ruzhu1(windows):
    """
        涉及指令0的地方，改的时候请把下面三两行直接改掉就行，下面其余的指令都一样
    """
    m = ['0']
    i =b.sql(m)  # 指令0看客房是否全满
      # 改完占领后把这一行删了，我是用来做测试用的
    if i == 0:
        tkinter.messagebox.showinfo(title='full', message='全部客房已满，无法入住')
    elif i== 1:
        windows_ruzhu = tkinter.Toplevel(windows, width=500, height=200)
        varName = tkinter.StringVar()
        varName.set('')
        varName2 = tkinter.StringVar()
        varName2.set('')
        varName3 = tkinter.StringVar()
        varName3.set('')
        varName4 = tkinter.StringVar()
        varName4.set('')
        varName5 = tkinter.StringVar()
        varName5.set('')

        # 创建标签和输入文本框
        labelName = tkinter.Label(windows_ruzhu, text='姓名：', justify=tkinter.RIGHT, width=80)
        labelName.place(x=10, y=10, width=80, height=20)

        entryName = tkinter.Entry(windows_ruzhu, width=80, textvariable=varName)
        entryName.place(x=100, y=5, width=140, height=20)

        user_id = tkinter.Label(windows_ruzhu, text='身份证号：', justify=tkinter.RIGHT, width=80)
        user_id.place(x=10, y=40, width=80, height=20)

        user_ID = tkinter.Entry(windows_ruzhu, width=80, textvariable=varName2)
        user_ID.place(x=100, y=40, width=140, height=20)

        telephone = tkinter.Label(windows_ruzhu, text='电话号码：', justify=tkinter.RIGHT, width=80)
        telephone.place(x=10, y=70, width=80, height=20)

        telephone_number = tkinter.Entry(windows_ruzhu, width=80, textvariable=varName3)
        telephone_number.place(x=100, y=70, width=140, height=20)

        ruzhu_time = tkinter.Label(windows_ruzhu, text='入住时间：', justify=tkinter.RIGHT, width=80)
        ruzhu_time.place(x=10, y=100, width=80, height=20)

        ruzhu_Time = tkinter.Entry(windows_ruzhu, width=80, textvariable=varName4)
        ruzhu_Time.place(x=100, y=100, width=140, height=20)

        leave_time = tkinter.Label(windows_ruzhu, text='离开时间：', justify=tkinter.RIGHT, width=80)
        leave_time.place(x=10, y=130, width=80, height=20)

        leave_Time = tkinter.Entry(windows_ruzhu, width=80, textvariable=varName5)
        leave_Time.place(x=100, y=130, width=140, height=20)

        def queren():  # 在这个函数里面实现验证输入信息是否规范以及发送数据
            name = entryName.get()
            idcard = user_ID.get()
            ruzhutime = ruzhu_Time.get()
            leavetime = leave_Time.get()
            telephonenumber=telephone_number.get()
            jz = jiaozheng_ruzhu(name, idcard, telephonenumber, ruzhutime, leavetime)
            if jz == 0:
                tkinter.messagebox.showerror('error', message='输入数据格式错误，请重新输入')
            else:
                """
                关于指令1的地方
                """
                m1 = ['1',name, idcard, telephonenumber, ruzhutime, leavetime]
                room_number = b.sql(m1)
                  # 改完占领后把这一行删了，我是用来做测试用的
                tkinter.messagebox.showinfo(title='success', message=
                                            '入住成功，请去客房%u' % room_number)
        buttonOK = tkinter.Button(windows_ruzhu,text='确认',command=queren)
        buttonOK.place(x=40,y=160)

        def cancel():
            varName.set('')
            varName2.set('')
            varName3.set('')
            varName4.set('')
            varName5.set('')
        buttoncancel = tkinter.Button(windows_ruzhu,text='取消',command=cancel)
        buttoncancel.place(x=120,y=160)


def qiantai(m):
    windows_qiantai = tkinter.Toplevel(m, width=300, height=200)
    windows_qiantai.title('前台界面')
    windows_qiantai.attributes('-topmost', 1)

    def ruzhu():
        ruzhu1( windows_qiantai)

    button_ruzhu = tkinter.Button(windows_qiantai, text='入住', command=ruzhu)
    button_ruzhu.place(x=20, y=20, height=30, width=100)

    def xuding():
        windows_xuding = tkinter.Toplevel(windows_qiantai, width=500, height=200)
        varName = tkinter.StringVar()
        varName.set('')
        varName1 = tkinter.StringVar()
        varName1.set('')

        xuding_room_label = tkinter.Label(windows_xuding, text='续订房间：',
                                          justify=tkinter.RIGHT, width=80)
        xuding_room_label.place(x=10, y=10, width=80, height=20)

        room_number = tkinter.Entry(windows_xuding, width=80, textvariable=varName)
        room_number.place(x=100, y=10, width=80, height=20)

        xuding_date_label = tkinter.Label(windows_xuding, text='续订时间：',
                                          justify=tkinter.RIGHT, width=80)
        xuding_date_label.place(x=10, y=40, width=80, height=20)

        xuding_date_string = tkinter.Entry(windows_xuding, width=80, textvariable=varName1)
        xuding_date_string.place(x=100, y=40, width=80, height=20)

        def queren1():  # 在这个函数里面实现验证输入信息是否规范以及发送数据
            room = room_number.get()
            date = xuding_date_string.get()

            jz = jiaozheng_xuding(room, date)
            if jz == 0:
                tkinter.messagebox.showerror('error', message='输入数据格式错误，请重新输入')
            else:
                """
                指令三的位置
                """
                m = ['3',room,date]
                m = b.sql(m)
                tkinter.messagebox.showinfo(title='success', message='续订成功')

        buttonOK = tkinter.Button(windows_xuding, text='确认', command=queren1)
        buttonOK.place(x=40, y=160)

        def cancel():
            varName.set('')
            varName1.set('')

        buttoncancela = tkinter.Button(windows_xuding, text='取消', command=cancel)
        buttoncancela.place(x=120, y=160)

    button_xuding = tkinter.Button(windows_qiantai, text='续订', command=xuding)
    button_xuding.place(x=20, y=80, height=30, width=100)

    def tuifang():

        windows_tuifang = tkinter.Toplevel(windows_qiantai, width=500, height=200)
        varName = tkinter.StringVar()
        varName.set('')

        tuifang_room_label = tkinter.Label(windows_tuifang, text='退订房间：',justify=tkinter.RIGHT, width=80)
        tuifang_room_label.place(x=10, y=10, width=80, height=20)

        tuidingroom_number = tkinter.Entry(windows_tuifang, width=80, textvariable=varName)
        tuidingroom_number.place(x=100, y=10, width=80, height=20)

        def queren2():  # 在这个函数里面实现验证输入信息是否规范以及发送数据

            room = tuidingroom_number.get()
            jz = jiaozheng_tuifang(room)
            if jz == 0:
                tkinter.messagebox.showerror('error', message='输入数据格式错误，请重新输入')
            else:
                """
                指令2的位置
                """
                m = ['2',room]
                money = b.sql(m)
                money=1000
                tkinter.messagebox.showinfo(title='success', message='退房成功，您共消费%u元'% money)

        buttonOK = tkinter.Button(windows_tuifang, text='确认', command=queren2)
        buttonOK.place(x=40, y=160)

        def cancel():
            varName.set('')

        buttoncancelb = tkinter.Button(windows_tuifang, text='取消', command=cancel)
        buttoncancelb.place(x=120, y=160)

    button_tuifang = tkinter.Button(windows_qiantai, text='退房', command=tuifang)
    button_tuifang.place(x=20, y=140, height=30, width=100)

    button_quit = tkinter.Button(windows_qiantai, text='退出', command=windows_qiantai.quit)
    button_quit.place(x=150, y=140, height=30, width=100)

    def qingdian():
        m=['4']
        y = b.sql(m)
        if (len(y)==0):tkinter.messagebox.showinfo(title='清点', message='今日无须退房顾客')
        else:
            tkinter.messagebox.showinfo(title='清点', message=y)

    button_qingdian = tkinter.Button(windows_qiantai, text='今日清点', command=qingdian)
    button_qingdian.place(x=150, y=80, height=30, width=100)
