import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Bilibili():

    def __init__(self):
        """
        初始化数据
        """
        self.server = 'http://localhost:4723/wd/hub'
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "MI_5",
            "appPackage": "tv.danmaku.bili",
            "appActivity": ".ui.splash.SplashActivity"
        }
        self.driver = webdriver.Remote(self.server, self.desired_caps)
        self.wait = WebDriverWait(self.driver, 20)

    def open(self):
        """
        打开B站
        :return:
        """
        # 随便找个元素输入点什么来刷新界面
        el0 = self.wait.until(EC.presence_of_element_located((By.ID, 'android:id/content')))
        el0.send_keys('110')
        # 点击跳过选项
        el1 = self.driver.find_element_by_id("tv.danmaku.bili:id/tv_skip")
        el1.click()
        # 随便输入点什么确保页面刷新
        el2 = self.driver.find_element_by_id("android:id/content")
        el2.send_keys("110")

    def run(self):
        """
        执行一系列操作
        :return:
        """
        # 点击频道选项
        el3 = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                      'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                      'android.widget.FrameLayout/android.widget.FrameLayout/'
                                                      'android.support.v4.widget.DrawerLayout/'
                                                      'android.widget.FrameLayout/android.view.ViewGroup/'
                                                      'android.widget.FrameLayout[2]/android.widget.LinearLayout/'
                                                      'android.widget.FrameLayout[2]')))
        el3.click()
        # 点击番剧选项
        el4 = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                      'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                      'android.widget.FrameLayout/android.widget.FrameLayout/'
                                                      'android.support.v4.widget.DrawerLayout/'
                                                      'android.widget.FrameLayout/android.view.ViewGroup/'
                                                      'android.widget.FrameLayout[1]/android.view.ViewGroup/'
                                                      'android.support.v7.widget.RecyclerView/'
                                                      'android.widget.LinearLayout[1]')))
        el4.click()
        # 点击连载动画选项
        el5 = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                      'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                      'android.widget.FrameLayout/android.widget.FrameLayout/'
                                                      'android.widget.FrameLayout/android.view.ViewGroup/'
                                                      'android.widget.LinearLayout/android.widget.HorizontalScrollView/'
                                                      'android.widget.LinearLayout/android.widget.TextView[2]')))
        el5.click()
        # 循环下滑
        time.sleep(2)
        num = 0
        while True:
            self.driver.swipe(300, 1200, 300, 300, 2000)
            num += 1
            if num >= 160:
                break
        # 点击完结动画
        el6 = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/'
                                                      'android.widget.LinearLayout/android.widget.FrameLayout/'
                                                      'android.widget.FrameLayout/android.widget.FrameLayout/'
                                                      'android.widget.FrameLayout/android.view.ViewGroup/'
                                                      'android.widget.LinearLayout/android.widget.HorizontalScrollView/'
                                                      'android.widget.LinearLayout/android.widget.TextView[3]')))
        el6.click()
        # 循环下拉
        time.sleep(2)
        num_1 = 0
        while True:
            time.sleep(0.8)
            self.driver.swipe(300, 1900, 300, 300, 1000)
            num_1 += 1
            if num_1 >= 300:
                break

    def main(self):
        """
        执行
        :return:
        """
        # 打开B站
        self.open()
        # 执行一系列操作
        self.run()


if __name__ == '__main__':
    main = Bilibili()
    main.main()
