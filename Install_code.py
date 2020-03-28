#!/usr/bin/python3

import tkinter as tk
import tkinter.messagebox
import ctypes
import os

# 代码内容
ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0)


# 第一个按钮
def ne_d():
    try:
        a = open('data1.txt')
        a.close()
    except FileNotFoundError:
        tkinter.messagebox.showerror(title='程序出错 Error！', message='没有找到源数据！\r\n请确保您正常的解压了完整的音源包，而不是单独的exe程序。')
        return

    ach.destroy()
    ne.destroy()
    lic.pack()
    gre.pack(side="bottom")
    return


# 第二个按钮
def gre_d():
    lic.destroy()
    gre.destroy()

    inp_t.pack()
    inp_in.pack()
    inp_en.pack(side="bottom")
    return


# 第三个按钮
def ins_d():
    link = File_Name.get()[:-8]
    # 路径取得！检查是否为UTAU路径
    try:
        a = open(link+'readme.txt')
        a.close()
    except FileNotFoundError:
        tkinter.messagebox.showerror(title="程序出错 Error!",
                                     message="您输入了错误的UTAU路径\r\n注意：请使用反斜杠\\而不是/，路径结尾应为utau.exe\r\n例：D:\\UTAU\\utau.exe")
        return

    inp_t.destroy()
    inp_in.destroy()
    inp_en.destroy()

    # 恶搞之前先验证下文件夹，防止bug
    istrue = os.path.exists(link+'res')
    if not istrue:
        os.makedirs(link+'res')

    # 开始恶搞，替换语言文件
    with open('data1.txt', encoding='UTF-16LE') as f:
        path = link+"res\\000.labelbuttonstring.txt"
        replace = open(path, 'w', encoding='UTF-16LE')
        replace.write(f.read())
        replace.close()
    with open('data2.txt', encoding='UTF-16LE') as f:
        path = link + "res\\000.menu.txt"
        replace = open(path, 'w', encoding='UTF-16LE')
        replace.write(f.read())
        replace.close()
    with open('data3.txt', encoding='UTF-16LE') as f:
        path = link + "res\\000.menustring.txt"
        replace = open(path, 'w', encoding='UTF-16LE')
        replace.write(f.read())
        replace.close()
    with open('data4.txt', encoding='UTF-16LE') as f:
        path = link + "res\\001.labelbuttonstring.txt"
        replace = open(path, 'w', encoding='UTF-16LE')
        replace.write(f.read())
        replace.close()
    with open('data5.txt', encoding='UTF-16LE') as f:
        path = link + "res\\001.menu.txt"
        replace = open(path, 'w', encoding='UTF-16LE')
        replace.write(f.read())
        replace.close()
    with open('data6.txt', encoding='UTF-16LE') as f:
        path = link + "res\\001.menustring.txt"
        replace = open(path, 'w', encoding='UTF-16LE')
        replace.write(f.read())
        replace.close()
    with open('data7.txt', encoding='UTF-16LE') as f:
        path = link + "res\\alias.txt"
        replace = open(path, 'w', encoding='UTF-16LE')
        replace.write(f.read())
        replace.close()
    # 完事，拜拜了您内
    fin.pack()
    return


# 主UI
windows = tk.Tk()
windows.title("酒绿 UTAU音源 安装程序 v0.1")
windows.geometry('680x400')

# 第一控件
lab = tk.Label(windows, text="酒绿 UTAU音源 安装程序", bg="white", font=("SimSun", 20), width=50, height=3)
lab.pack()
ach = tk.Label(windows, text="author@OrangeSun", bg="white", font=("KaiTi", 15), width=30, height=1)
ach.pack()
ne = tk.Button(windows, text="继续 next→", width=10, height=1,  command=ne_d)
ne.pack(side='bottom')
# 第二控件
lic_txt = "使用协议：\r\n本音源开放一切使用授权，但其法律责任由使用者独自承担。\r\n此程序抽风带来的一切后果，程序编写者不承担其一切责任。"
lic = tk.Label(windows, text=lic_txt, bg='white', font=("SimSun", 12))
gre = tk.Button(windows, text="我同意 I agree →", width=15, height=1, command=gre_d)
# 第三控件
inp_t = tk.Label(windows, text="请输入 你电脑里 utau.exe 所在路径。", bg='white', font=("SimSun", 15))
File_Name = tk.StringVar()
File_Name.set("D:\\UTAU\\utau.exe")
inp_in = tk.Entry(windows, textvariable=File_Name, font=('Arial', 15), width=35)
inp_en = tk.Button(windows, text="开始安装 install→", width=16, height=1, command=ins_d)
# 完事
fin = tk.Label(windows, text='April Fool!\r\n恶搞完成，快去看看你的UTAU吧！', bg='white', font=('SimSun', 20))
windows.tk.call('tk', 'scaling', ScaleFactor/75)
windows.mainloop()
