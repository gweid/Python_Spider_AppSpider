import time
import pymongo
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Jingdong():

    def __init__(self):
        """
        初始化数据
        """
        self.server = 'http://localhost:4723/wd/hub'
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "MI_5",
            "appPackage": "com.jingdong.app.mall",
            "appActivity": "main.MainActivity",
            "unicodeKeyboard": "True",
            "resetKeyboard": "True"
        }
        self.driver = webdriver.Remote(self.server, self.desired_caps)
        self.wait = WebDriverWait(self.driver, 30)
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.client.Jingdong
        self.collection = self.db.content

    def open(self):
        """
        打开京东app，进入界面
        :return:
        """
        # 点击同意
        el1 = self.driver.find_element_by_id("com.jingdong.app.mall:id/btp")
        el1.click()
        # 刷新一下页面，确保进入京东界面
        el2 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jingdong.app.mall:id/fz')))
        el2.clear()
        # 点击叉掉广告
        el3 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jingdong.app.mall:id/l7')))
        el3.click()

    def comments(self):
        """
        点击搜索商品
        :return:
        """
        # 点击一下搜索框进入搜索界面
        el4 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jingdong.app.mall:id/rd')))
        el4.click()
        # 输入搜索内容
        el5 = self.driver.find_element_by_id("com.jd.lib.search:id/search_text")
        el5.set_text("固态硬盘")
        # 点击搜索按钮
        el6 = self.driver.find_element_by_id("com.jingdong.app.mall:id/awc")
        el6.click()
        # 点击商品进入详情页
        el7 = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                      'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                      'android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/'
                                                      'android.widget.RelativeLayout/'
                                                      'android.support.v7.widget.RecyclerView/'
                                                      'android.widget.RelativeLayout[1]/android.widget.RelativeLayout/'
                                                      'android.widget.RelativeLayout[1]')))
        el7.click()

    def crawl(self):
        """
        爬取评论并保存
        :return:
        """
        time.sleep(3)
        # 下拉一小段距离，是评论字眼出现
        self.driver.swipe(300, 1350, 300, 300, 1500)
        # 点击进入评论页面
        el8 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.jd.lib.productdetail:id/pd_tab3')))
        el8.click()
        time.sleep(3)
        # 一直下拉
        while True:
            self.driver.swipe(300, 1300, 300, 300, 1000)
            try:
                nickname = self.wait.until(
                    EC.presence_of_element_located((By.ID, 'com.jd.lib.shareorder:id/tv_name'))).get_attribute('text')
                times = self.wait.until(
                    EC.presence_of_element_located((By.ID, 'com.jd.lib.shareorder:id/tv_pub_time'))).get_attribute(
                    'text')
                content = self.wait.until(
                    EC.presence_of_element_located(
                        (By.ID, 'com.jd.lib.shareorder:id/tv_expand_content'))).get_attribute(
                    'text')
                data = {
                    'nickname': nickname,
                    'time': times,
                    'content': content
                }
                print(data)
                self.collection.update({'nickname': nickname, 'content': content}, {'$set': data}, True)
            except:
                print('继续下拉')

    def main(self):
        # 进入京东
        self.open()
        # 搜索并进入商品界面
        self.comments()
        # 抓取数据
        time.sleep(5)
        self.crawl()


if __name__ == '__main__':
    main = Jingdong()
    main.main()
