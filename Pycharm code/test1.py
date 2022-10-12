import tkinter as tk  # 装载tkinter模块,用于Python3
from tkinter import ttk  # 装载tkinter.ttk模块,用于Python3

root = tk.Tk()  # 创建窗口对象
root.title('闹钟和时钟')  # 设置窗口标题
root.geometry('400x300+200+200')
root.resizable(width=False, height=False)  # 设置窗口是否可变，宽不可变，高不可变，默认为True

ttk.Style().configure(".", font=("仿宋", 20))

tabControl = ttk.Notebook(root)  # 创建Notebook
tab1 = tk.Frame(tabControl, bg='blue')  # 增加新选项卡
tabControl.add(tab1, text='闹钟')  # 把新选项卡增加到Notebook
tab2 = tk.Frame(tabControl, bg='yellow')
tabControl.add(tab2, text='时钟')
tab3 = tk.Frame(tabControl, bg='green')
tabControl.add(tab3, text='计时器')
tab4 = tk.Frame(tabControl, bg='blue')
tabControl.add(tab4, text='秒表')

tabControl.pack(expand=1, fill="both")

tabControl.select(tab1)  # 选择tab1

root.mainloop()  # 进入消息循环
'''
如要将每个默认按钮更改为具有一些填充和不同背景颜色的平面按钮：
from tkinter import ttk
import tkinter

root = tkinter.Tk()

ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ccc")

btn = ttk.Button(text="Sample")
btn.pack()
'''
