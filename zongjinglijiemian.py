#coding=utf-8
import tkinter
import caiwutu
import bbb as b

"""
本程序中有指令6 7
"""


def sql(m):
    return 0


def zongjingli(m):
    windows_jingli = tkinter.Toplevel(m, width=300, height=200)
    windows_jingli.title('经理界面')
    windows_jingli.attributes('-topmost', 1)

    def caiwu():

        m = ['6']
        y = b.sql(m)
        """
        指令6部分
        """
        #y = [2000,3000,5000,11000,3000,4000,8000]
        caiwutu.huatu(y,windows_jingli)

    button_caiwu = tkinter.Button(windows_jingli, text='财务报表', command=caiwu)
    button_caiwu.place(x=20, y=20, height=30, width=100)

    def ruzhulv():
        m = ['7']
        n = b.sql(m)
        """
        指令7部分
        """
        #n =99.2
        tkinter.messagebox.showinfo(title='入住率', message="今日入住率为%5.2f" % n)


    button_ruzhulv = tkinter.Button(windows_jingli, text='入住率', command=ruzhulv)
    button_ruzhulv.place(x=20, y=80, height=30, width=100)

    button_quit = tkinter.Button(windows_jingli, text='退出', command=windows_jingli.quit)
    button_quit.place(x=150, y=140, height=30, width=100)
