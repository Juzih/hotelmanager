import tkinter
import qiantaijiemian
import kerenjiemian
import zongjinglijiemian


root = tkinter.Tk()
# root.config(height=360)
# root.config(width=260)
root.geometry('300x220+400+300')
root.resizable(False,False)
root.title('酒店管理系统主界面')


def button_qiantaijiemian():          # 前台界面
    qiantaijiemian.qiantai(root)


button_qiantai = tkinter.Button(root, text='前台界面', command=button_qiantaijiemian)
button_qiantai.place(x=20,y=20,height=30,width=100)


def buttion_kerenjiemian():            # 客人界面
    kerenjiemian.keren(root)


button_keren = tkinter.Button(root, text='客人界面', command=buttion_kerenjiemian)
button_keren.place(x=20, y=90, height=30, width=100)


def button_jinglijiemian():            # 经理界面
    zongjinglijiemian.zongjingli(root)


button_jingli = tkinter.Button(root, text='经理界面', command=button_jinglijiemian)
button_jingli.place(x=20, y=160, height=30, width=100)

root.mainloop()