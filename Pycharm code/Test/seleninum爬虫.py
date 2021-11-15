#!/Users/env python
# -*- coding:utf-8 -*-
# @author：麟听 WeChat:15019763969
from selenium import webdriver

import time

url = "https://www.58.com/zufang/"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)
driver.find_element_by_link_text("佛山").click()
windows_handles = driver.window_handles
driver.switch_to.window(windows_handles[1])
data_list=driver.find_elements_by_xpath("/html/body/div[6]/div[2]/ul/li")
for data in data_list:
    print(data.text)
    print("="*50)
time.sleep(2)
driver.quit()
