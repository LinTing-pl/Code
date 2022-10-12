#!/Users/env python
# -*- coding:utf-8 -*-
# @author：麟听 WeChat:15019763969
import random
import re
import time

import requests


class DouBan(object):
    def __init__(self, offset):
        self.url = 'https://movie.douban.com/top250?start=' + str(offset)
        self.headers = {
            "User-Agent": "用你们自己的"}

    def get_html(self):
        response = requests.get(self.url, headers=self.headers)
        print(response.status_code)
        response.encoding = "utf-8"
        return response.text

    def find(self, content):
        try:
            pattern = re.compile(r'<div class="info">.*?class="title">(.*?)</span>'
                                 r'.*?导演: (.*?)&nbsp;'
                                 r'.*?主演: (.*?)\.'
                                 r'.*?<br>(.*?)&nbsp;/&nbsp;(.*?)&nbsp;'
                                 r'.*?rating_num" property="v:average">(.*?)</span>', re.S)
            for item in pattern.findall(content):
                yield {
                    '电影名': item[0],
                    '导演': item[1].strip(),
                    '主演': item[2].split()[0],
                    '上映时间': item[3].strip(),
                    '地点': item[4],
                    '评分': item[5],
                }
                time.sleep(3)
        except IndexError:
            pass

    def run(self):
        movies_html = self.get_html()
        movies_content = self.find(movies_html)
        for i in movies_content:
            print(i)
            f.write("电影名:{},导演:{},主演:{},上映时间:{},地点:{},评分:{}\n".format(i['电影名'], i['导演'], i['主演'], i['上映时间'], i['地点'],
                                                                      i['评分']))


if __name__ == '__main__':
    f = open("./豆瓣.csv", "w", encoding="utf-8")
    for i in range(1, 3):
        pa = DouBan(25 * i)
        pa.run()
        time.sleep(3)
    f.close()
