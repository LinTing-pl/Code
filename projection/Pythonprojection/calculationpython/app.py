# coding:utf8
import tkinter
from functools import partial


# 按钮输入调用
class Calculation(object):
    def __init__(self):
        pass

    def get_input(self, entry, argu):
        # 从entry窗口展示中获取输入的内容
        input_data = entry.get()
        # 出现连续+，则第二个+为无效输入，不做任何处理
        if input_data[-1:] == '+' and argu == '+':
            return
        # 出现连续+--，则第三个-为无效输入，不做任何处理
        if input_data[-2:] == '+-' and argu == '-':
            return
        # 窗口已经有--后面字符不能为+或-
        if input_data[-2:] == '--' and argu in ['-', '+']:
            return
        # 窗口已经有 ** 后面字符不能为 * 或 /
        if input_data[-2:] == '**' and argu in ['*', '/']:
            return

        # 输入合法将字符插入到entry窗口结尾
        entry.insert("end", argu)

    # 退格(撤销输入)
    def backspace(self, entry):
        input_len = len(entry.get())
        # 删除entry窗口中最后的字符
        entry.delete(input_len - 1)

    # 清空entry内容(清空窗口)
    def clear(self, entry):
        entry.delete(0, "end")

    # 计算
    def calc(self, entry):
        input_data = entry.get()
        # 计算前判断输入内容是否为空;首字符不能为*/;*/不能连续出现3次;
        if not input_data:
            return

        self.clear(entry)

        # 异常捕获，在进行数据运算时如果出现异常进行相应处理
        # noinspection PyBroadException
        try:
            output_data = str(eval(input_data))
        except Exception:
            # 将提示信息输出到窗口
            entry.insert("end", "Calculation error")
        else:
            # 将计算结果显示在窗口中
            if len(output_data) > 20:
                entry.insert("end", "Value overflow")
            else:
                entry.insert("end", output_data)


class Gui(object):
    def __init__(self):
        self.cal = Calculation()
        self.root = tkinter.Tk()
        self.root.title("计算器")
        self.root.geometry("500x550")
        self.root.minsize(500, 550)
        self.entry1 = tkinter.Entry(self.root, justify="right", font=('宋体', 35))
        self.entry1.place(relx=0.01, rely=0.04, relwidth=0.98, relheight=0.2)
        self.place_button('7', self.cal.get_input, (self.entry1, '7'), relx=0.01, rely=0.27, relwidth=0.19,
                          relheight=0.16)
        self.place_button('8', self.cal.get_input, (self.entry1, '8'), relx=0.21, rely=0.27, relwidth=0.19,
                          relheight=0.16)
        self.place_button('9', self.cal.get_input, (self.entry1, '9'), relx=0.41, rely=0.27, relwidth=0.19,
                          relheight=0.16)
        self.place_button('4', self.cal.get_input, (self.entry1, '4'), relx=0.01, rely=0.45, relwidth=0.19,
                          relheight=0.16)
        self.place_button('5', self.cal.get_input, (self.entry1, '5'), relx=0.21, rely=0.45, relwidth=0.19,
                          relheight=0.16)
        self.place_button('6', self.cal.get_input, (self.entry1, '6'), relx=0.41, rely=0.45, relwidth=0.19,
                          relheight=0.16)
        self.place_button('1', self.cal.get_input, (self.entry1, '1'), relx=0.01, rely=0.63, relwidth=0.19,
                          relheight=0.16)
        self.place_button('2', self.cal.get_input, (self.entry1, '2'), relx=0.21, rely=0.63, relwidth=0.19,
                          relheight=0.16)
        self.place_button('3', self.cal.get_input, (self.entry1, '3'), relx=0.41, rely=0.63, relwidth=0.19,
                          relheight=0.16)
        self.place_button('0', self.cal.get_input, (self.entry1, '0'), relx=0.21, rely=0.81, relwidth=0.19,
                          relheight=0.16)
        self.place_button('.', self.cal.get_input, (self.entry1, '.'), relx=0.01, rely=0.81, relwidth=0.19,
                          relheight=0.16)
        self.place_button('+', self.cal.get_input, (self.entry1, '+'), relx=0.61, bg="lightyellow", abg="#f5f6df",
                          rely=0.45, relwidth=0.19, relheight=0.16)
        self.place_button('-', self.cal.get_input, (self.entry1, '-'), relx=0.805, bg="lightyellow", rely=0.45,
                          abg="#f5f6df", relwidth=0.19, relheight=0.16)
        self.place_button('*', self.cal.get_input, (self.entry1, '*'), relx=0.61, bg="lightyellow", rely=0.63,
                          abg="#f5f6df", relwidth=0.19, relheight=0.16)
        self.place_button('/', self.cal.get_input, (self.entry1, '/'), relx=0.805, bg="lightyellow", rely=0.63,
                          abg="#f5f6df", relwidth=0.19, relheight=0.16)
        self.place_button('<-', self.cal.backspace, (self.entry1,), bg="lightgreen", abg="#bfeec0", relx=0.61,
                          rely=0.27, relwidth=0.19, relheight=0.16)
        self.place_button('C', self.cal.clear, (self.entry1,), bg="#f20739", abg="#f15073", relx=0.805, rely=0.27,
                          relwidth=0.19, relheight=0.16)
        self.place_button('=', self.cal.calc, (self.entry1,), bg="#ec6618", abg="#e67737", relx=0.61, rely=0.81,
                          relwidth=0.385, relheight=0.16)
        self.place_button('(', self.cal.get_input, (self.entry1, '('), relx=0.41, bg="lightyellow", rely=0.81,
                          abg="#f5f6df", relwidth=0.09, relheight=0.16)
        self.place_button(')', self.cal.get_input, (self.entry1, ')'), relx=0.51, bg="lightyellow", rely=0.81,
                          abg="#f5f6df", relwidth=0.09, relheight=0.16)

    def place_button(self, text, func, func_params, bg="#F8F8FF", abg="#DCDCDC", **place_params):
        # 偏函数partial，定义一个模板，后续的按钮在模板基础上进行修改或添加特性
        # activebackground：按钮按下后显示颜place_params色
        my_button = partial(tkinter.Button, self.root, bg="#F8F8FF", activebackground=abg)
        button = my_button(text=text, bg=bg, font=('宋体', 25), command=lambda: func(*func_params))
        button.place(**place_params)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    gui = Gui()
    gui.run()
