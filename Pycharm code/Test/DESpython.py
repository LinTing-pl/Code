#!/Users/env python
# -*- coding:utf-8 -*-
# @author：麟听 WeChat:15019763969
from DEStodo import *


# 算法实现
def cipher(message, key, mode='encrypt'):
    # 初始化明文和密钥，将其转化为二进制串
    message = string2bin(message)
    key = string2bin(key)
    # 子密钥的生成，当mode为'decrypt'时，反转子密钥序列
    subkeys = createSubKey(key) if mode == 'encrypt' else createSubKey(key)[::-1]
    text = IpTable(message)

    # F函数
    for i in range(16):
        l, r = text[:32], text[32:]
        r_extend = E_extend(r)  # 对右半部分进行E扩展运算，转换成48位对串
        xor1 = xor(r_extend, subkeys[i])  # 对得到对48位串与48位对子密钥进行异或运算
        s_box_result = s_box_change(xor1)  # 异或得到对结果进行S盒转换
        p_box_result = p_box_change(s_box_result)  # p置换，得到轮函数的输出
        xor2 = xor(l, p_box_result)  # 将左半部分与轮函数输出做异或，得到新串对右半部分
        text = r + xor2  # 左右部分结合，形成新串

    text = text[32:] + text[:32]
    # print(InverseIpTable(text))
    # 将二进制密文串转换为字符串返回
    return bin2string(InverseIpTable(text))


def fill(string):  # 如果二进制串的位数不是8的倍数，则用补满空缺位数
    mod = len(string) % 8
    space = 8 - mod
    return string + bytes(space).decode('utf-8')


class DES(object):
    def __init__(self, message, key):
        self.message = message
        self.key = key

    @property
    def ciphertext(self):  # 密文
        return self.__encrypt()

    @property
    def plaintext(self):  # 明文
        return self.__decrypt()

    def __encrypt(self):  # 加密
        output = []
        length = len(self.message)
        # 按64bit为一组(8bytes)进行切分
        times, mod = length // 8, length % 8
        if mod:  # 补位
            self.message = fill(self.message)
            times += 1
        # 对明文对每一组进行操作
        for i in range(times):
            result = cipher(self.message[i * 8:i * 8 + 8], self.key, 'encrypt')
            output.append(result)

        return ''.join(output)

    def __decrypt(self):  # 解密
        output = []
        length = len(self.message)
        times, mod = length // 8, length % 8

        if not times:
            return None

        if mod:
            self.message = fill(self.message)
            times += 1

        for i in range(times):
            result = cipher(self.message[i * 8:i * 8 + 8], self.key, 'decrypt')
            output.append(result)

        return ''.join(output).rstrip(b'\x00'.decode('utf-8'))


while True:
    mess = input("请输入需要操作的内容:")
    opt = input("请选择是进行加密还是解密，加密输入0，解密输入1:")
    while not (opt == '0' or opt == '1'):
        print("Warming!!!选择的操作类型只能是0或者是1")
        opt = input("请选择是进行加密还是解密，加密输入0，解密输入1:")
    if opt == '0':
        key = input("请输入加密密钥:")
        while len(key) != 8:
            print("请输入八字节字符的密钥，请重新输入:")
            key = input()
        cipher1 = DES(mess, key)
        print("加密后的密文:", cipher1.ciphertext, sep='')
    if opt == '1':
        key = input("请输入解密密钥:")
        while len(key) != 8:
            print("请输入八字节字符的密钥，请重新输入:")
            key = input()
        cipher2 = DES(mess, key)
        print("解密后的明文:", cipher2.plaintext, sep='')
