import tkinter
from tkinter import *


def huatu(y,windows):
    windows_huatu = tkinter.Toplevel(windows)
    zhexiantu = tkinter.Canvas(windows_huatu,width=1500,height=700)
    zhexiantu.pack()
    w0 = 40
    h0 = 650 # 起始点

    zhexiantu.create_line(w0,h0,w0+1300,h0,fill="red", arrow=LAST)
    zhexiantu.create_line(w0,h0,w0,h0-600,fill="red", arrow=LAST)

    # x轴刻度
    for i in range(1,8):
           j=i*200
           zhexiantu.create_line((j-200)+w0,h0,(j-200)+w0,h0-5,fill="red")
           zhexiantu.create_text((j-200)+w0,h0+5,text=str(i))
    # y轴刻度
    for i in range(0,20000,500):
           j=i*0.03
           zhexiantu.create_line(w0,h0-j,w0+5,h0-j,fill="red")
           zhexiantu.create_text(w0-15,h0-j,text=str(i))

    def yi(y,i):
        h0 = 650
        y = y[i]*0.03
        y = h0-y
        return y


    def x(i):
        w0=40
        x = w0+i*200
        return x
    i = 0
    while i<6:
        zhexiantu.create_line(x(i),yi(y,i),x(i+1),yi(y,i+1), fill='blue')
        i = i+1
