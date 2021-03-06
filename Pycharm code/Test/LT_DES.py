import tkinter as tk
from tkinter.ttk import *

Database = {
    'ip': {
        'ip': [58, 50, 42, 34, 26, 18, 10, 2,
               60, 52, 44, 36, 28, 20, 12, 4,
               62, 54, 46, 38, 30, 22, 14, 6,
               64, 56, 48, 40, 32, 24, 16, 8,
               57, 49, 41, 33, 25, 17, 9, 1,
               59, 51, 43, 35, 27, 19, 11, 3,
               61, 53, 45, 37, 29, 21, 13, 5,
               63, 55, 47, 39, 31, 23, 15, 7],
        'inverseip': [40, 8, 48, 16, 56, 24, 64, 32,
                      39, 7, 47, 15, 55, 23, 63, 31,
                      38, 6, 46, 14, 54, 22, 62, 30,
                      37, 5, 45, 13, 53, 21, 61, 29,
                      36, 4, 44, 12, 52, 20, 60, 28,
                      35, 3, 43, 11, 51, 19, 59, 27,
                      34, 2, 42, 10, 50, 18, 58, 26,
                      33, 1, 41, 9, 49, 17, 57, 25],
    },
    'Ebox': [32, 1, 2, 3, 4, 5,
             4, 5, 6, 7, 8, 9,
             8, 9, 10, 11, 12, 13,
             12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21,
             20, 21, 22, 23, 24, 25,
             24, 25, 26, 27, 28, 29,
             28, 29, 30, 31, 32, 1
             ],
    'Pbox': [16, 7, 20, 21, 29, 12, 28, 17,
             1, 15, 23, 26, 5, 18, 31, 10,
             2, 8, 24, 14, 32, 27, 3, 9,
             19, 13, 30, 6, 22, 11, 4, 25],
    'Sbox': {
        's1': [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
               [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
               [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
               [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
        's2': [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
               [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
               [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
               [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
        's3': [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
               [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
               [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
               [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
        's4': [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
               [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
               [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
               [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
        's5': [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
               [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
               [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
               [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
        's6': [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
               [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
               [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
               [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
        's7': [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
               [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
               [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
               [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
        's8': [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
               [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
               [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
               [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
    },
    'PC': {
        'PC-1': [57, 49, 41, 33, 25, 17, 9,
                 1, 58, 50, 42, 34, 26, 18,
                 10, 2, 59, 51, 43, 35, 27,
                 19, 11, 3, 60, 52, 44, 36,
                 63, 55, 47, 39, 31, 23, 15,
                 7, 62, 54, 46, 38, 30, 22,
                 14, 6, 61, 53, 45, 37, 29,
                 21, 13, 5, 28, 20, 12, 4],
        'PC-2': [14, 17, 11, 24, 1, 5, 3, 28,
                 15, 6, 21, 10, 23, 19, 12, 4,
                 26, 8, 16, 7, 27, 20, 13, 2,
                 41, 52, 31, 37, 47, 55, 30, 40,
                 51, 45, 33, 48, 44, 49, 39, 56,
                 34, 53, 46, 42, 50, 36, 29, 32]
    },
    'step': [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
}


def IP(m):
    """IP????????????,64??????64??????"""
    ip = Database['ip']['ip']
    return [m[ip[i] - 1] for i in range(64)]


def InverseIP(m):
    """InverseIP???????????????,64??????64??????"""
    inverseip = Database['ip']['inverseip']
    return [m[inverseip[i] - 1] for i in range(64)]


def E_extend(m):
    """E????????????,32??????48??????"""
    E = Database['Ebox']
    return [m[E[i] - 1] for i in range(48)]


def Sboxchange(m):
    """s???????????????48???????????????????????????6???8????????????????????????????????????????????????S????????????4??????????????????????????????32????????????"""
    result = []
    S_box = [Database['Sbox'][i] for i in ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8']]
    for i in range(8):
        entry = m[i * 6:(i + 1) * 6]
        row = int(str(entry[0]) + str(entry[-1]), 2)
        col = int(str(entry[1]) + str(entry[2]) + str(entry[3]) + str(entry[4]), 2)
        result.extend(f'{S_box[i][row][col]:04b}')
    return [int(i) for i in ''.join(result)]


def Pboxchange(m):
    """P???????????????32????????????P?????????????????????32????????????"""
    P = Database['Pbox']
    return [m[P[i] - 1] for i in range(32)]


def Xor(m, n):
    """????????????"""
    return [a ^ b for a, b in zip(m, n)]


def leftmove(m, step):
    """????????????"""
    return m[step:] + m[:step]


def createSubkey(prekey):
    """?????????????????????64???->56???->48???"""
    result = []
    K = prekey
    PC_1 = Database['PC']['PC-1']
    PC_2 = Database['PC']['PC-2']
    step = Database['step']
    Key56 = [K[PC_1[i] - 1] for i in range(56)]
    C, D = Key56[:28], Key56[28:]
    for i in range(16):
        C, D = leftmove(C, step[i]), leftmove(D, step[i])
        K = C + D
        Key48 = [K[PC_2[i] - 1] for i in range(48)]
        result.append(Key48)
    return result


def string2bit(m):
    """??????????????????????????????????????????64bit"""
    output = []
    result = []
    a = [ord(i) for i in m]
    num = 0
    for i in range(len(a)):
        b = bin(a[i]).replace('0b', '')
        length = len(b)
        space = 16 - length
        c = '0' * space + b
        for j in range(len(c)):
            num += 1
            result.append(int(c[j]))
            while i == len(a) - 1 and j == len(c) - 1 and num < 64:
                num += 16
                result.extend([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
            if num >= 64:
                output.append(result)
                num = 0
                result = []
    return output


def key2bit(m):
    """??????????????????????????????????????????64bit"""
    result = []
    num = 0
    a = [ord(i) for i in m]
    for i in range(len(a)):
        b = bin(a[i]).replace('0b', '')
        length = len(b)
        space = 8 - length
        c = '0' * space + b
        for j in range(len(c)):
            num += 1
            result.append(int(c[j]))
        while i == len(a) - 1 and num < 64:
            num += 8
            result.extend([0, 0, 1, 0, 0, 0, 0, 0])
    return result


def bit2string(m):
    result = []
    length = len(m)
    for i in range(length):
        matrix = m[i]
        string = ''.join([str(n) for n in matrix])
        for j in range(4):
            result.append(chr(int(string[j * 16:(j + 1) * 16], 2)))
    return ''.join(result)


def cipher(message, key, opt):
    result = []
    subkey = createSubkey(key) if opt == '0' else createSubkey(key)[::-1]
    for i in range(len(message)):
        m = IP(message[i])
        for j in range(16):
            L, R = m[:32], m[32:]
            E = E_extend(R)
            X1 = Xor(E, subkey[j])  # E????????????????????????
            S = Sboxchange(X1)
            P = Pboxchange(S)
            X2 = Xor(L, P)  # L???P(F????????????)??????
            m = R + X2
        m = m[32:] + m[:32]
        IIP = InverseIP(m)
        result.append(IIP)
    output = bit2string(result)
    return output


class DES(object):
    def __init__(self, message='', key='', opt='0'):
        self.message = message
        self.key = key
        self.opt = opt
        self.result = []

    @property
    def enc(self):
        return self.__encrypt()

    @property
    def dec(self):
        return self.__decrypt()

    def __encrypt(self):
        self.message = string2bit(self.message)
        self.key = key2bit(self.key)
        self.result = cipher(self.message, self.key, self.opt)
        return self.result

    def __decrypt(self):
        self.message = string2bit(self.message)
        self.key = key2bit(self.key)
        self.opt = '1'
        self.result = cipher(self.message, self.key, self.opt)
        return self.result.rstrip(b'\x00'.decode('utf-8'))

    def run(self):
        self.message = input('??????????????????????????????:')
        self.opt = input('??????????????????????????????????????????0???????????????1:')
        while not (self.opt == '0' or self.opt == '1'):
            print('Warming!!!??????????????????????????????0???1')
            self.opt = input('??????????????????????????????????????????0???????????????1:')
        if self.opt == '0':
            self.key = input('?????????8???????????????:')
            while not len(self.key) == 8:
                self.key = input('?????????8?????????,???????????????:')
            print(f'??????????????????:{self.enc}')
        elif self.opt == '1':
            self.key = input('?????????8???????????????:')
            while not len(self.key) == 8:
                self.key = input('?????????8?????????,???????????????:')
            print(f'??????????????????:{self.dec}')


class Gui(object):
    def __init__(self):
        """?????????"""
        self.tk = tk.Tk()  # ???????????????
        self.tk.title('DES')
        self.tk.geometry('600x400')  # ????????????

        self.lb1 = tk.Label(self.tk, text='??????:', font=('??????', 12))  # ??????Lable??????
        self.lb2 = tk.Label(self.tk, text='??????:', font=('??????', 12))
        self.lb3 = tk.Label(self.tk, text='??????:', font=('??????', 12))
        self.entry1 = tk.Entry(self.tk, relief='groove', font=('??????', 13))
        self.text1 = tk.Text(self.tk, relief='groove')  # ?????????????????????????????????
        self.text2 = tk.Text(self.tk, relief='groove', state='disabled')  # ????????????????????????(????????????)
        self.button1 = tk.Button(self.tk, text='??????', font=('??????', 14), bg='white', overrelief='groove',
                                 command=self.encrypt)  # ????????????
        self.button2 = tk.Button(self.tk, text='??????', font=('??????', 14), bg='white', overrelief='groove',
                                 command=self.decrypt)  # ????????????

    def display(self):
        """????????????????????????????????????"""
        self.lb1.place(relx=0.12, rely=0.01, relheight=0.04)
        self.lb2.place(relx=0.12, rely=0.57, relheight=0.04)
        self.lb3.place(relx=0.12, rely=0.45, relheight=0.04, relwidth=0.1)
        self.text1.place(relheight=0.35, relwidth=0.80, relx=0.15, rely=0.05)
        self.text2.place(relheight=0.35, relwidth=0.80, relx=0.15, rely=0.61)
        self.button1.place(relx=0.02, rely=0.40, relwidth=0.10, relheight=0.10)
        self.button2.place(relx=0.02, rely=0.50, relwidth=0.10, relheight=0.10)
        self.entry1.place(relx=0.22, rely=0.43, relwidth=0.35, relheight=0.09)

    def normal_text(self, text):
        """Text???state NORMAL"""
        text.config(state='normal')

    def disabled_text(self, text):
        """Text???state DISABLED"""
        text.config(state='disabled')

    def encrypt(self):
        """??????class:DES"""
        des = DES(self.text1.get('1.0', '1.3000'), self.entry1.get())
        res = des.enc
        self.normal_text(self.text2)  # ??????Text
        self.text2.delete('1.0', 'end')  # ??????self.text2??????
        self.text2.insert('insert', res)  # ??????self.text2??????
        self.disabled_text(self.text2)  # ??????Text

    def decrypt(self):
        """??????class:DES"""
        des = DES(self.text1.get('1.0', '1.3000'), self.entry1.get())
        res = des.dec
        self.normal_text(self.text2)  # ??????Text
        self.text2.delete('1.0', 'end')  # ??????self.text2??????
        self.text2.insert('insert', res)  # ??????self.text2??????
        self.disabled_text(self.text2)  # ??????Text

    def run(self):
        """????????????"""
        self.display()
        self.tk.mainloop()  # ?????????????????????????????????????????????????????????????????????????????????


if __name__ == '__main__':
    gui = Gui()
    gui.run()
