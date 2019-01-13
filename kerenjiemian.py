import tkinter
import tkinter.messagebox
import zifuchuan
"""
本程序中有指令5 8
"""
def sql():
    return 0

def jiaozheng_xiaofei(a):
    zf = 1
    alen = len(a)
    if alen != 3:
        zf = 0
        return zf
    for i in range(alen):
        if zifuchuan.is_number(a[i]):
            zf = 1
        else:
            zf = 0
            return zf
    return zf

def keren(m):
    windows_keren = tkinter.Toplevel(m, width=300, height=200)
    windows_keren.title('客人界面')
    windows_keren.attributes('-topmost', 1)

    def xiaofei():

        windows_xiaofei = tkinter.Toplevel(windows_keren, width=500, height=200)
        windows_xiaofei.title("消费界面")
        varName = tkinter.StringVar()
        varName.set('')

        xiaofei_room_label = tkinter.Label(windows_xiaofei, text='房间号码：',
                                          justify=tkinter.RIGHT, width=80)
        xiaofei_room_label.place(x=10, y=10, width=80, height=20)

        xiaofei_number = tkinter.Entry(windows_xiaofei, width=80, textvariable=varName)
        xiaofei_number.place(x=100, y=10, width=80, height=20)

        def queren():  # 在这个函数里面实现验证输入信息是否规范以及发送数据
            room = xiaofei_number.get()

            jz = jiaozheng_xiaofei(room)
            if jz == 0:
                tkinter.messagebox.showerror('error', message='输入数据格式错误，请重新输入')
            else:
                """
                指令8
                
                
                """
                # m = ['8',room]
                # money = sql(m)
                money=1000
                tkinter.messagebox.showinfo(title='消费', message='您当前消费总金额为%u元'% money)

        buttonOK = tkinter.Button(windows_xiaofei, text='确认', command=queren)
        buttonOK.place(x=40, y=160)

        def cancel():
            varName.set('')

        buttoncancelb = tkinter.Button(windows_xiaofei, text='取消', command=cancel)
        buttoncancelb.place(x=120, y=160)

    button_ruzhu = tkinter.Button(windows_keren, text='消费情况', command=xiaofei)
    button_ruzhu.place(x=20, y=20, height=30, width=100)

    def dingcan():
        windows_dingcan = tkinter.Toplevel(windows_keren, width=300, height=220)
        windows_dingcan.title("订餐界面")

        varName = tkinter.StringVar()
        varName.set('')

        dingcan_room_label = tkinter.Label(windows_dingcan, text='房间号码：',
                                           justify=tkinter.RIGHT, width=80)
        dingcan_room_label.place(x=10, y=10, width=80, height=20)

        dingcan_number = tkinter.Entry(windows_dingcan, width=80, textvariable=varName)
        dingcan_number.place(x=100, y=10, width=80, height=20)

        def queren1():  # 在这个函数里面实现验证输入信息是否规范以及发送数据
            room = dingcan_number.get()
            jz = jiaozheng_xiaofei(room)
            if jz == 0:
                tkinter.messagebox.showerror('error', message='输入数据格式错误，请重新输入')
            else:
                windows_taocan = tkinter.Toplevel(windows_dingcan, width=300, height=220)
                windows_taocan.title("套餐界面")
                """
                指令5，该指令一共有4处分别在taocanABCD里面
                """

                def taocanA():
                    # m = ['5',room,'1000']
                    # l = sql(m)
                    tkinter.messagebox.showinfo(title='订餐', message="您已预定套餐A成功")

                buttonA = tkinter.Button(windows_taocan, text='套餐A(10元)', command=taocanA)
                buttonA.place(x=20, y=20)

                def taocanB():
                    # m = ['5',room,'0100']
                    # l = sql(m)
                    tkinter.messagebox.showinfo(title='订餐', message="您已预定套餐B成功")

                buttonB = tkinter.Button(windows_taocan, text='套餐B(15)元', command=taocanB)
                buttonB.place(x=20, y=70)

                def taocanC():
                    # m = ['5',room,'0010']
                    # l = sql(m)
                    tkinter.messagebox.showinfo(title='订餐', message="您已预定套餐C成功")

                buttonC = tkinter.Button(windows_taocan, text='套餐C(8元)', command=taocanC)
                buttonC.place(x=20, y=120)

                def taocanD():
                    # m = ['5',room,'0001']
                    # l = sql(m)
                    tkinter.messagebox.showinfo(title='订餐', message="您已预定套餐D成功")

                buttonD = tkinter.Button(windows_taocan, text='套餐D(20元)', command=taocanD)
                buttonD.place(x=20, y=170)

        buttonOK = tkinter.Button(windows_dingcan, text='确认', command=queren1)
        buttonOK.place(x=40, y=160)

    button_ruzhu = tkinter.Button(windows_keren, text='消费情况', command=xiaofei)
    button_ruzhu.place(x=20, y=20, height=30, width=100)

    button_xuding = tkinter.Button(windows_keren, text='订餐', command=dingcan)
    button_xuding.place(x=20, y=90, height=30, width=100)

    button_quit = tkinter.Button(windows_keren, text='退出', command=windows_keren.quit)
    button_quit.place(x=170, y=150, height=30, width=100)
