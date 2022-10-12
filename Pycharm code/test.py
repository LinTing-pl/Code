import tkinter, sys, time

root = tkinter.Tk()
root.minsize(500, 500)
Label1 = tkinter.Label(text=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
Label1.pack()


def trickit():
    currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    Label1.config(text=currentTime)
    root.update()
    Label1.after(1000, trickit)


Label1.after(1000, trickit)

root.mainloop()
