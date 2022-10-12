import random
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Driver(object):
    def __init__(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.option.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                                    {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
        self.url = ""
        # self.d = {10: [["能不能让保安别抓外卖了", "保安可以不抓外卖吗", "外卖追逐战", "除了抓外卖，其余都还可以", "还行吧，现在疫情有点严重，抓外面可以理解"],
        #                ["能不能让保安别抓外卖了", "保安可以不抓外卖吗", "外卖追逐战", "除了抓外卖，其余都还可以", "还行吧，现在疫情有点严重，抓外面可以理解"],
        #                ["能不能让保安别抓外卖了", "保安可以不抓外卖吗", "外卖追逐战", "除了抓外卖，其余都还可以", "还行吧，现在疫情有点严重，抓外面可以理解"],
        #                ["能不能让保安别抓外卖了", "保安可以不抓外卖吗", "哎"], ["外卖追逐战", "除了抓外卖，其余都还可以", "还行吧，现在疫情有点严重，抓外面可以理解"]],
        #           11: [0, 0, 0, ["挺好", "食堂卫生还可以", "给的量还行"], ["很好", "还挺好吃的，特别是二饭", "卫生做的不错"]],
        #           12: [0, 0, 0, ["挺好", "速度还挺快", "还不错"], ["很好", "速度挺快的", "挺好的"]],
        #           13: [0, 0, 0, ["挺好", "挺好", "挺好"], ["很好", "工作挺辛苦的", "厕所清理的挺干净的"]],
        #           14: [0, 0, 0, ["挺好", "一般般", "还行"], ["很好", "服务还挺好的", "很好"]],
        #           15: [0, 0, 0, ["挺好", "还行", "还行"], ["很好", "护士挺关心人的", "very good"]],
        #           16: [0, 0, 0, ["挺好", "还行，等车的时候不会很久", "挺好"], ["很好", "车挺快的", "不错"]],
        #           17: [0, 0, 0, ["挺好", "服务挺多的", "挺好"], ["很好", "吃的挺多的，打印配眼镜等服务也应有尽有", "挺好的，服务的多的"]], }
        # 10:保安 11:食堂员工 12:维修工人 13:环卫工人 14:邮政服务员工 15:医护员工 16:环校车服务 17:商务服务

    def set_url(self, url):
        self.url = url

    def run(self):
        self.driver.get(self.url)
        time.sleep(2)
        i = 1
        while i <= 22:
            if i == 7:
                c = random.randint(2, 6)
                j = random.sample(range(1, 8), k=c)
                for jj in j:
                    base_xpath = '#div7 > div.ui-controlgroup.column1 > div:nth-child({}) > div'.format(jj)
                    self.driver.find_element(By.CSS_SELECTOR, base_xpath).click()
                    time.sleep(0.6)
            elif i == 11:
                c = random.randint(3, 8)
                j = random.sample(range(1, 10), k=c)
                for jj in j:
                    base_xpath = '#div11 > div.ui-controlgroup.column1 > div:nth-child({}) > div'.format(jj)
                    self.driver.find_element(By.CSS_SELECTOR, base_xpath).click()
                    time.sleep(0.6)
            elif i in [2, 12, 13, 16, 20]:
                j = random.randint(1, 2)
                base_xpath = '#div{} > div.ui-controlgroup.column1 > div:nth-child({}) > div'.format(i, j)
                self.driver.find_element(By.CSS_SELECTOR, base_xpath).click()
                time.sleep(0.5)
            elif i in [8, 9, 15, 18, 19, 21, 22]:
                j = random.randint(1, 3)
                base_xpath = '#div{} > div.ui-controlgroup.column1 > div:nth-child({}) > div'.format(i, j)
                self.driver.find_element(By.CSS_SELECTOR, base_xpath).click()
                time.sleep(0.5)
            else:
                j = random.randint(1, 4)
                base_xpath = '#div{} > div.ui-controlgroup.column1 > div:nth-child({}) > div'.format(i, j)
                self.driver.find_element(By.CSS_SELECTOR, base_xpath).click()
                time.sleep(0.5)
            i += 1
        try:
            self.driver.find_element(By.CSS_SELECTOR, "#ctlNext").click()
            time.sleep(0.5)
            self.driver.find_element(By.CSS_SELECTOR,
                                     '#alert_box > div:nth-child(2) > div:nth-child(2) > button').click()
            time.sleep(0.5)
            self.driver.find_element(By.CSS_SELECTOR, '#rectMask').click()

        except:
            pass


if __name__ == '__main__':
    n = 100
    cnt = 0
    driver = Driver()
    driver.set_url('https://www.wjx.cn/vm/midVyK4.aspx')
    while n:
        n -= 1
        cnt += 1
        print(cnt)
        driver.run()
        time.sleep(7)
