#!/Users/env python
# -*- coding:utf-8 -*-
# @author：麟听 WeChat:15019763969
import random
import re
import requests


class MaoYan(object):
    def __init__(self, offset):
        self.url = 'https://maoyan.com/board/4?offset=' + str(offset)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62"}

    def get_html(self):
        response = requests.get(self.url, headers=self.headers)
        response.encoding = "utf-8"
        return response.text

    def find(self, content):
        pattern = re.compile(r'<dd>'
                             r'.*?board-index.*?>(\d+)</i>'
                             r'.*?title="(.*?)"'
                             r'.*?star">(.*?)</p>'
                             r'.*?releasetime">(.*?)</p>.*?'
                             r'(</dd>)', re.S)

        for item in pattern.findall(content):
            yield {
                '排名': item[0],
                '电影名': item[1],
                '主演': item[2].strip()[3:],
                '上映时间': item[3].strip()[5:]
            }

    def run(self):
        movies_html = self.get_html()
        movies_content = self.find(movies_html)
        for i in movies_content:
            print(i)


if __name__ == '__main__':
    for num in range(10):
        movies = MaoYan(num * 10)
        movies.run()
