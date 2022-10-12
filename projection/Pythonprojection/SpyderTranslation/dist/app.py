# coding:utf-8
# @author：麟听 WeChat:15019763969
from threading import Thread
import tkinter as tk
from tkinter.ttk import *
from json import loads
from hashlib import md5
import requests
import random
from pyperclip import copy, paste


# spider翻译类
class FySpider(object):
    # https://www.iciba.com/fy
    language = {'自动检测': 'auto', '德语': 'de', '英语': 'en', '西班牙语': 'es', '法语': 'fr', '日语': 'ja', '韩语': 'ko', '中文': 'zh',
                '俄语': 'ru', '阿丘雅语': 'acu', '阿瓜鲁纳语': 'agr', '阿卡瓦伊语': 'ake', '阿姆哈拉语': 'am', '阿穆斯戈语': 'amu', '阿拉伯语': 'ar',
                '阿塞拜疆语': 'az', '埃维语': 'ee', '爱沙尼亚语': 'et', '爱尔兰语': 'ga', '奥吉布瓦语': 'ojb', '奥罗莫语': 'om', '奥利亚语': 'or',
                '奥赛梯语': 'os', '阿尔巴尼亚语': 'sq', '巴什基尔语': 'ba', '白俄罗斯语': 'be', '别姆巴语': 'bem', '柏柏尔语': 'ber', '保加利亚语': 'bg',
                '比斯拉马语': 'bi', '布列塔尼语': 'br', '波斯尼亚语': 'bs', '巴拉萨纳语': 'bsn', '巴斯克语': 'eu', '波斯语': 'fa', '冰岛语': 'is',
                '白苗文': 'mww', '波兰语': 'pl', '波塔瓦托米语': 'pot', '巴布亚皮钦语': 'tpi', '查莫罗语': 'cha', '楚瓦什语': 'cv', '茨瓦纳语': 'tn',
                '聪加语': 'ts', '丹麦语': 'da', "德语": "de", '丁卡语': 'dik', '迪维希语': 'dv', '德顿语': 'tet', '鞑靼语': 'tt',
                '恩都卡语': 'djk', "俄语": "ru", '芬兰语': 'fi', '菲律宾语': 'fil', '斐济语': 'fj', '法罗语': 'fo', "法语": "fr",
                '弗里西语': 'fy', '古吉拉特语': 'gu', '格鲁吉亚语': 'jy', '刚果语': 'kg', '高棉语': 'km', '盖丘亚语': 'quw', '豪萨语': 'ha',
                '海地克里奥尔语': 'ht', '哈萨克语': 'ka', '哈萨克语(西里尔)': 'kk', "韩语": "ko", '黑山语': 'me', '加泰罗尼亚语': 'ca', '捷克语': 'cs',
                '加莱拉语': 'gbi', '加利西亚语': 'gl', '吉尔吉斯语': 'ky', '基切语': 'quc', '卡克奇克尔语': 'cak', '卡韦卡尔语': 'cjp',
                '坎帕语': 'cni', '科西嘉语': 'co', '科普特语': 'cop', '克罗地亚语': 'hr', '卡拜尔语': 'kab', '科奇语': 'kbh', '凯克其语': 'kek',
                '卡纳达语': 'kn', '库尔德语': 'ku', '克雷塔罗奥托米语': 'otq', '卢克帕语': 'dop', '拉丁语': 'la', '卢森堡语': 'lb', '卢干达语': 'lg',
                '林加拉语': 'ln', '老挝语': 'lo', '立陶宛语': 'lt', '拉脱维亚语': 'lv', '罗姆语': 'rmn', '隆迪语': 'rn', '罗马尼亚语': 'ro',
                '卢旺达语': 'rw', '孟加拉语': 'bn', '马恩岛语': 'gv', '马姆语': 'mam', '马尔加什语': 'mg', '马里语': 'mhr', '毛利语': 'mi',
                '马其顿语': 'mk', '马拉雅拉姆语': 'ml', '蒙古语(西里尔)': 'mn', '马拉地语': 'mr', '马来语': 'ms', '马耳他语': 'mt', '缅甸语': 'my',
                '南非荷兰语': 'af', '尼泊尔语': 'ne', '纳瓦特尔语': 'nhg', '尼德兰语': 'nl', '挪威语': 'no', '南非科萨语': 'xh', '南非祖鲁语': 'zu',
                '旁遮普语': 'pa', '帕皮阿门托语': 'pap', '派特语': 'pck', '普什图语': 'ps', '葡萄牙语': 'pt', '切诺基语': 'chr', '齐切瓦语': 'ny',
                '契维语': 'tw', "日语": "ja", '瑞典语': 'sv', '宿务语': 'ceb', '塞舌尔克里奥尔语': 'crs', '世界语': 'eo', '苏格兰盖尔语': 'gd',
                '舒阿尔语': 'jiv', '山地马里语': 'mrj', '桑戈语': 'sg', '僧伽罗语': 'si', '斯洛伐克语': 'sk', '斯洛文尼亚语': 'sl', '萨摩亚语': 'sm',
                '索马里语': 'so', '塞尔维亚语': 'sr', '塞索托语': 'st', '斯瓦希里语': 'sw', '泰米尔语': 'ta', '泰卢固语': 'te', '塔吉克语': 'tg',
                '泰语': 'th', '提格雷语': 'tig', '土库曼语': 'tk', '图阿雷格语': 'tmh', '汤加语': 'to', '土耳其语': 'tr', '塔希提语': 'ty',
                '瓦哈卡语': 'chq', '威尔士语': 'cy', '乌玛语': 'ppk', '乌德穆尔特语': 'udm', '乌克兰语': 'uk', '乌尔都语': 'ur', '乌斯潘坦语': 'usp',
                '维吾尔语': 'uy', '乌兹别克语': 'uz', '文达语': 've', '瓦拉莫语': 'wal', '瓦瑞语': 'war', '沃洛夫语': 'wol', '希腊语': 'el',
                "西班牙语": "es", '夏威夷语': 'haw', '希伯来语': 'he', '匈牙利语': 'hu', '信德语': 'sd', '希尔哈语': 'shi', '修纳语': 'sn',
                '叙利亚语': 'syc', '亚齐语': 'ace', "英语": "en", '印地语': 'hi', '亚美尼亚语': 'hy', '印尼语': 'id', '伊博语': 'ig',
                '意大利语': 'it', '雅加达语': 'jac', '印尼爪哇语': 'jv', '印尼巽他语': 'su', '越南语': 'vi', '意第绪语': 'yi', '约鲁巴语': 'yo',
                '尤卡坦玛雅语': 'yua', '粤语': 'yue', '中文(繁体)': 'cht', '哲尔马语': 'dje', '宗喀语': 'dz', '藏语': 'ti', '中文': 'zh', }

    def __init__(self, query_str, query_from, query_to):
        """初始化"""
        self.query_content = query_str  # 搜索的内容
        self.query_from = query_from  # 源语言
        self.query_to = query_to  # to语言

        # &sign的加密算法
        # r = c()("6key_web_fanyi".concat(s.y2).concat(t.q.replace(/(^\s*)|(\s*$)/g, ""))).toString().substring(0, 16);
        #                 return g("/index.php?c=trans&m=fy&client=6&auth_user=key_web_fanyi&sign=".concat(r),                                                                                                         16)
        # 经分析s.y2返回i,找到函数i
        # i = (0, u)("z%C3%8F%C3%87%C3%8F%C3%A7%C3%A2%C3%A0%C3%9C%C3%87%C2%9A%C2%A0%C3%8B%C2%9C%C2%AC%C2%ACq%C2%9D")
        # 找到函数u
        # u = function(e){
        #   e = decodeURIComponent(e);
        #   for (var t = String.fromCharCode(e.charCodeAt(0) - e.length), r = 1; r < e.length; r++)
        #       t += String.fromCharCode(e.charCodeAt(r) - t.charCodeAt(r - 1));
        #   return t}
        # t执行出来为 ifanyiweb8hc9s98e
        sign = (md5(("6key_web_fanyi" + "ifanyiweb8hc9s98e" + self.query_content).encode()).hexdigest())[0:16]

        # url: https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_web_fanyi&sign=4b5dcb6d774603bc
        url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_web_fanyi'
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
        r = random.randint(0, 2)
        response = requests.post(self.url, proxies=self.proxies[r], data=self.data)
        print(response.status_code, r)
        return response.content.decode()

    # {"status":1,"content":{"from":"en","to":"zh","out":"\u4f60\u597d","vendor":"ciba","err_no":0,"ttsLan":8}}
    # {"status":1,"content":{"from":"en","to":"zh","vendor":"ciba","out":"\u4f60\u597d\u4e16\u754c","reqid":"27249569-48a3-4d3d-a306-6a1257a39ec0","version":"v2.21.220526.1","ciba_use":"\u4ee5\u4e0a\u7ed3\u679c\u6765\u81ea\u8bcd\u9738AI\u5b9e\u9a8c\u5ba4\u3002","ciba_out":"","err_no":0,"ttsLan":8,"ttsLanFrom":1}}
    def parse_data(self, json_str):
        """提取数据：翻译的结果"""
        dict_data = loads(json_str)
        result = dict_data['content']['out']  # 提取‘content’中的’out‘
        return result

    def run(self):
        """运行程序，返回翻译的结果"""
        json_str = self.get_data_fromurl()
        print(json_str)
        fy_result = self.parse_data(json_str)
        return fy_result


# Gui界面类
class Gui(object):
    def __init__(self):
        """初始化"""
        self.spider = tk.Tk()  # 创建根窗口
        self.spider.title('翻译小软件（spider）')
        self.spider.geometry('800x420')  # 窗口大小
        self.spider.minsize(700, 320)
        self.spider.config(background="#e8f7f6")

        self.lb3_var = tk.StringVar()
        self.lb1 = tk.Label(self.spider, text='源语言:', height=1, font=('宋体', 12))  # 创建Lable文本
        self.lb2 = tk.Label(self.spider, text='翻译为:', height=1, font=('宋体', 12))  # 创建Lable文本
        self.lb3 = tk.Label(self.spider, textvariable=self.lb3_var, background='lightblue', height=1,
                            font=('宋体', 10))  # 创建Lable文本

        self.text1 = tk.Text(self.spider, font=("宋体"))  # 用于接收输入的翻译内容
        self.text2 = tk.Text(self.spider, font=("宋体"), state='disabled')  # 用于显示翻译结果(禁止编辑)

        self.button1 = tk.Button(self.spider, text='→', font=('宋体', 20), bg='#ffffff', overrelief='groove',
                                 command=lambda: self.thread_it(self.translate))  # 翻译按钮
        self.button2 = tk.Button(self.spider, text='清空输入', font=('宋体', 10), bg='#ffffff', overrelief='groove',
                                 command=lambda: self.thread_it(self.clearInput))  # 翻译按钮
        self.button3 = tk.Button(self.spider, text='复制\n翻译文本', font=('宋体', 10), bg='#ffffff', overrelief='groove',
                                 command=lambda: self.thread_it(self.copyText))  # 翻译按钮

        self.var1 = tk.StringVar()  # Comboxbox textvariable变量
        self.var2 = tk.StringVar()  # Comboxbox textvariable变量

        self.comb1 = Combobox(self.spider, textvariable=self.var1,
                              values=list(FySpider.language.keys()))  # 组合框用于选择from语言
        self.comb2 = Combobox(self.spider, textvariable=self.var2, values=list(FySpider.language.keys()))  # 组合框用于选择to语言
        self.comb1.current(0)  # 默认选项 list(FjSpider.language.keys())[0]
        self.comb2.current(0)  # 默认选项 list(FjSpider.language.keys())[0]
        self.comb1_lan = "自动检测"
        self.comb2_lan = "自动检测"

    def display(self):
        """显示组件，并设置组件大小"""
        self.lb1.place(relx=0.02, rely=0.01, relheight=0.05)
        self.lb2.place(relx=0.55, rely=0.01, relheight=0.05)
        self.lb3.place(relx=0.02, rely=0.94, relheight=0.05)

        self.lb3.config(textvariable=self.lb3_var, background='lightblue')
        self.lb3_var.set('当前[自动选择]目标语言,选择翻译为[自动选择]')

        self.text1.place(relheight=0.82, relwidth=0.43, relx=0.02, rely=0.1)
        self.text2.place(relheight=0.82, relwidth=0.43, relx=0.55, rely=0.1)

        self.button1.place(relx=0.46, rely=0.41, relwidth=0.08, relheight=0.18)
        self.button2.place(relx=0.46, rely=0.21, relwidth=0.08, relheight=0.14)
        self.button3.place(relx=0.46, rely=0.65, relwidth=0.08, relheight=0.14)

        self.comb1.place(relx=0.12, rely=0.01, relwidth=0.2, relheight=0.05)
        self.comb2.place(relx=0.65, rely=0.01, relwidth=0.2, relheight=0.05)
        self.comb1.bind('<<ComboboxSelected>>', lambda x: self.thread_it(self.select_comb1_lan))
        self.comb2.bind('<<ComboboxSelected>>', lambda x: self.thread_it(self.select_comb2_lan))

        self.text1.bind('<Return>', lambda x: self.translate())
        self.spider.bind('<Return>', lambda x: self.translate())

    def normal_text(self, text):
        """Text：state NORMAL"""
        text.config(state='normal')

    def disabled_text(self, text):
        """Text：state DISABLED"""
        text.config(state='disabled')

    def translate(self):
        """button command:获取self.text1的内容并翻译，将结果显示在self.text2"""
        try:
            query = FySpider(self.text1.get('1.0', '1.3000').strip(), FySpider.language[self.comb1_lan],
                             FySpider.language[self.comb2_lan])
            fy_result = query.run()
            self.normal_text(self.text2)  # 启用Text
            self.text2.delete('1.0', 'end')  # 清空self.text2文本
            self.text2.insert('insert', fy_result)  # 插入self.text2文本
            self.disabled_text(self.text2)  # 关闭Text
            self.lb3.config(background='lightgreen')
            self.lb3_var.set(f'翻译完成...已翻译为[{self.comb2_lan}]')
        except Exception:  # 运行错误则清空self.text2文本
            self.normal_text(self.text2)  # 启用Text
            self.text2.delete('1.0', 'end')
            self.disabled_text(self.text2)  # 关闭Text
            self.lb3_var.set("翻译内容为空白!")
            self.lb3.config(background='#e35464')
        finally:
            return 'break'

    def clearInput(self):
        self.text1.delete("1.0", "end")
        self.lb3.config(background='lightgreen')
        self.lb3_var.set("清空成功！")

    def copyText(self):
        tr_res = self.text2.get('0.0', "end")
        tr_res = tr_res.rstrip("\n")
        copy(tr_res)
        spam = paste()
        if spam:
            self.lb3.config(background='lightyellow')
            self.lb3_var.set('复制成功！')
        else:
            self.lb3.config(background='#e35464')
            self.lb3_var.set('复制内容为空白！')

    def select_comb1_lan(self):
        self.comb1_lan = self.comb1.get()
        self.lb3.config(background="lightblue")
        self.lb3_var.set(f'当前[{self.comb1_lan}]目标语言,选择翻译为[{self.comb2_lan}]')

    def select_comb2_lan(self):
        self.comb2_lan = self.comb2.get()
        self.lb3.config(background="lightblue")
        self.lb3_var.set(f'当前[{self.comb1_lan}]目标语言,选择翻译为[{self.comb2_lan}]')

    def thread_it(self, func):
        t = Thread(target=func)
        t.start()

    def run(self):
        """运行程序"""
        self.display()
        self.spider.mainloop()  # 接收操作系统发来的事件，然后把事件分发给各个控件和窗体


if __name__ == '__main__':
    py_Gui = Gui()
    py_Gui.run()
