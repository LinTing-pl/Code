#!/Users/env python
# -*- coding:utf-8 -*-
# @author：麟听 WeChat:15019763969
import tkinter as tk
from tkinter.ttk import *
import json
import hashlib
import requests
import random


# spider翻译类
class FjSpider(object):
    language = {'自动检测': 'auto', "中文": 'zh', '中文(繁体)': 'cht', "英语": 'en', "法语": 'fr', "日语": 'ja', "韩语": 'ko', '俄语': 'ru',
                "德语": 'de', "西班牙语": 'es', '希腊语': 'el', '世界语': 'eo'}  # 可翻译的语言 也可自行添加到language
    """A: {sq: "阿尔巴尼亚语", ar: "阿拉伯语", am: "阿姆哈拉语", acu: "阿丘雅语", agr: "阿瓜鲁纳语", ake: "阿卡瓦伊语", amu: "阿穆斯戈语",…}
    B: {tpi: "巴布亚皮钦语", bsn: "巴拉萨纳语", ba: "巴什基尔语", eu: "巴斯克语", be: "白俄罗斯语", mww: "白苗文", ber: "柏柏尔语",…}
    C: {cha: "查莫罗语", cv: "楚瓦什语", tn: "茨瓦纳语", ts: "聪加语"}
    D: {tt: "鞑靼语", da: "丹麦语", de: "德语", tet: "德顿语", dv: "迪维希语", dik: "丁卡语"}
    E: {ru: "俄语", djk: "恩都卡语"}
    F: {fr: "法语", fo: "法罗语", fil: "菲律宾语", fj: "斐济语", fi: "芬兰语", fy: "弗里西语"}
    G: {km: "高棉语", quw: "盖丘亚语", kg: "刚果语", jy: "格鲁吉亚语", gu: "古吉拉特语"}
    H: {ka: "哈萨克语", kk: "哈萨克语(西里尔)", ht: "海地克里奥尔语", ko: "韩语", ha: "豪萨语", me: "黑山语"}
    J: {ky: "吉尔吉斯语", quc: "基切语", gbi: "加莱拉语", gl: "加利西亚语", ca: "加泰罗尼亚语", cs: "捷克语"}
    K: {kn: "卡纳达语", kek: "凯克其语", cni: "坎帕语", cop: "科普特语", kbh: "科奇语", co: "科西嘉语", otq: "克雷塔罗奥托米语",…}
    L: {la: "拉丁语", lv: "拉脱维亚语", lo: "老挝语", rn: "隆迪语", lt: "立陶宛语", ln: "林加拉语", lg: "卢干达语", dop: "卢克帕语",…}
    M: {mg: "马尔加什语", mt: "马耳他语", gv: "马恩岛语", mr: "马拉地语", ml: "马拉雅拉姆语", ms: "马来语", mhr: "马里语", mam: "马姆语",…}
    N: {nhg: "纳瓦特尔语", af: "南非荷兰语", xh: "南非科萨语", zu: "南非祖鲁语", ne: "尼泊尔语", nl: "尼德兰语", no: "挪威语"}
    P: {pap: "帕皮阿门托语", pck: "派特语", pa: "旁遮普语", pt: "葡萄牙语", ps: "普什图语"}
    Q: {ny: "齐切瓦语", tw: "契维语", chr: "切诺基语"}
    R: {ja: "日语", sv: "瑞典语"}
    S: {sm: "萨摩亚语", sr: "塞尔维亚语", crs: "塞舌尔克里奥尔语", st: "塞索托语", sg: "桑戈语", si: "僧伽罗语", mrj: "山地马里语", eo: "世界语",…}
    T: {tg: "塔吉克语", ty: "塔希提语", te: "泰卢固语", ta: "泰米尔语", th: "泰语", to: "汤加语", tig: "提格雷语", tmh: "图阿雷格语",…}
    W: {chq: "瓦哈卡语", wal: "瓦拉莫语", war: "瓦瑞语", uy: "维吾尔语", cy: "威尔士语", ve: "文达语", wol: "沃洛夫语", udm: "乌德穆尔特语",…}
    X: {es: "西班牙语", he: "希伯来语", shi: "希尔哈语", el: "希腊语", haw: "夏威夷语", sd: "信德语", hu: "匈牙利语", sn: "修纳语",…}
    Y: {hy: "亚美尼亚语", jac: "雅加达语", ace: "亚齐语", ig: "伊博语", it: "意大利语", yi: "意第绪语", hi: "印地语", su: "印尼巽他语",…}
    Z: {ti: "藏语", dje: "哲尔马语", zh: "中文", cht: "中文(繁体)", dz: "宗喀语"}
    common: {zh: "中文", en: "英语", fr: "法语", ja: "日语", ko: "韩语", de: "德语", es: "西班牙语"}"""

    def __init__(self, query_str, query_from, query_to):
        """初始化"""
        self.query_content = query_str  # 搜索的内容
        self.query_from = query_from  # 源语言
        self.query_to = query_to  # to语言

        # &sign的加密算法
        # r = c()("6key_cibaifanyicjbysdlove1".concat(t.q.replace(/(^\s*)|(\s*$)/g, ""))).toString().substring(0, 16);
        #       return g("/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=".concat(r), {
        sign = (hashlib.md5(("6key_cibaifanyicjbysdlove1" + self.query_content).encode()).hexdigest())[0:16]

        # url: https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=bbea7edbe8ff7465
        url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba'
        self.url = url + '&sign=' + sign

        self.proxies = [
            {'https1': 'https://106.75.226.36:808'},
            {'https2': 'https://61.157.206.174:37259'},
            {'https3': 'https://106.75.164.15:3128'}

        ]  # 请求头（高匿代理）

        self.data = self.get_data()  # 获取请求体

    def get_data(self):
        """获取请求体数据"""
        data = {'from': self.query_from,
                'to': self.query_to,
                'q': self.query_content
                }
        return data

    def get_data_fromurl(self):
        """从服务器获取数据 并解析返回"""
        response = requests.post(self.url, proxies=self.proxies[random.randint(0, 2)], data=self.data)
        print(response.status_code)
        return response.content.decode()

    # {"status":1,"content":{"from":"en","to":"zh","out":"\u4f60\u597d","vendor":"ciba","err_no":0,"ttsLan":8}}
    def parse_data(self, json_str):
        """提取数据：翻译的结果"""
        dict_data = json.loads(json_str)
        result = dict_data['content']['out']  # 提取‘content’中的’out‘
        print(dict_data)
        return result

    def run(self):
        """运行程序，返回翻译的结果"""
        json_str = self.get_data_fromurl()
        fy_result = self.parse_data(json_str)
        return fy_result


# Gui界面类
class Gui(object):
    def __init__(self):
        """初始化"""
        self.spider = tk.Tk()  # 创建根窗口
        self.spider.title('翻译小软件（spider）')
        self.spider.geometry('800x400')  # 窗口大小
        self.spider.config(background="#e8f7f6")

        self.lb1 = tk.Label(self.spider, text='源语言:', height=1, font=('宋体'))  # 创建Lable文本
        self.lb2 = tk.Label(self.spider, text='翻译为:', height=1, font=('宋体'))  # 创建Lable文本

        self.text1 = tk.Text(self.spider, font=("宋体"))  # 用于接收输入的翻译内容
        self.text2 = tk.Text(self.spider, font=("宋体"), state='disabled')  # 用于显示翻译结果(禁止编辑)

        self.button1 = tk.Button(self.spider, text='→', font=('宋体', 20), bg='#ffffff', overrelief='groove',
                                 command=self.translate)  # 翻译按钮

        self.var1 = tk.StringVar()  # Comboxbox textvariable变量
        self.var2 = tk.StringVar()  # Comboxbox textvariable变量

        self.comb1 = Combobox(self.spider, textvariable=self.var1,
                              values=list(FjSpider.language.keys()))  # 组合框用于选择from语言
        self.comb2 = Combobox(self.spider, textvariable=self.var2, values=list(FjSpider.language.keys()))  # 组合框用于选择to语言
        self.comb1.current(0)  # 默认选项 list(FjSpider.language.keys())[0]
        self.comb2.current(0)  # 默认选项 list(FjSpider.language.keys())[0]

    def display(self):
        """显示组件，并设置组件大小"""
        self.lb1.place(relx=0.02, rely=0.01, relheight=0.05)
        self.lb2.place(relx=0.55, rely=0.01, relheight=0.05)

        self.text1.place(relheight=0.85, relwidth=0.43, relx=0.02, rely=0.1)
        self.text2.place(relheight=0.85, relwidth=0.43, relx=0.55, rely=0.1)

        self.button1.place(relx=0.46, rely=0.41, relwidth=0.08, relheight=0.18)

        self.comb1.place(relx=0.12, rely=0.01, relwidth=0.2, relheight=0.05)
        self.comb2.place(relx=0.65, rely=0.01, relwidth=0.2, relheight=0.05)

        self.spider.bind('<Return>', lambda x: self.translate())
        self.text1.bind('<Return>', lambda x: self.translate())

    def normal_text(self, text):
        """Text：state NORMAL"""
        text.config(state='normal')

    def disabled_text(self, text):
        """Text：state DISABLED"""
        text.config(state='disabled')

    def translate(self):
        """button command:获取self.text1的内容并翻译，将结果显示在self.text2"""
        try:
            query = FjSpider(self.text1.get('1.0', '1.3000'), FjSpider.language[self.comb1.get()],
                             FjSpider.language[self.comb2.get()])
            fy_result = query.run()
            self.normal_text(self.text2)  # 启用Text
            self.text2.delete('1.0', 'end')  # 清空self.text2文本
            self.text2.insert('insert', fy_result)  # 插入self.text2文本
            self.disabled_text(self.text2)  # 关闭Text
        except Exception:  # 运行错误则清空self.text2文本
            self.normal_text(self.text2)  # 启用Text
            self.text2.delete('1.0', 'end')
            self.disabled_text(self.text2)  # 关闭Text

        finally:
            return 'break'

    def run(self):
        """运行程序"""
        self.display()
        self.spider.mainloop()  # 接收操作系统发来的事件，然后把事件分发给各个控件和窗体


if __name__ == '__main__':
    py_Gui = Gui()
    py_Gui.run()
