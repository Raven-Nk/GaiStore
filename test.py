from tkinter import *
import tkinter.messagebox
from tkinter import filedialog

#比对系统
def check(uname,password):
    f = open('txt.txt','r',encoding = 'utf-8')
    conbine = f.readline()
    f.close()
    u,love,p,plove = conbine.split(',')
    if u == uname and p == password:
        tkinter.messagebox.showinfo('欢迎您！', uname)
    elif love == uname and plove == password:
        tkinter.messagebox.showinfo('欢迎宝！', '宝贝别生气~~')
    else:
        tkinter.messagebox.showinfo('警告', '用户名或密码错误')

def login():
    uname = unametext.get()
    password = passwordtext.get()
    check(uname,password)

#注册窗口
win = Tk()
win.title('登陆界面')
win.geometry('650x500')


#账号文本框
Label(text = '账号(姓名)：').place(x = 50, y = 110)
unametext = Entry(win)
unametext.place(x = 150,y = 110)

#密码文本框
Label(text='密码（生日日月如0321）：').place(x = 50, y = 150)
passwordtext = Entry(win,show = '*')
passwordtext.place(x = 200, y = 150)

# 登录

but = Button(text='登录',command = login)
but.place(x=100, y=180, width=190)
win.mainloop()

