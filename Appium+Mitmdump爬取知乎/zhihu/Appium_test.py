import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Zhihu():

    def __init__(self):
        """
        初始化参数
        """
        self.server = 'http://localhost:4723/wd/hub'
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "MI_5",
            "appPackage": "com.zhihu.android",
            "appActivity": ".app.ui.activity.MainActivity"
        }
        self.driver = webdriver.Remote(self.server, self.desired_caps)
        self.wait = WebDriverWait(self.driver, 20)

    def open(self):
        """
        打开知乎界面
        :return:
        """
        # 通过账号和密码登录
        el1 = self.driver.find_element_by_id("com.zhihu.android:id/go_to_btn")
        el1.click()
        # 输入账号
        el2 = self.driver.find_element_by_id("com.zhihu.android:id/email_input_view")
        el2.send_keys("13570773719")
        # 输入密码
        el3 = self.driver.find_element_by_id("com.zhihu.android:id/password")
        el3.send_keys("a6387578")
        # 点击登录
        el4 = self.driver.find_element_by_id("com.zhihu.android:id/btn_progress")
        el4.click()
        # 进行必要的刷新
        el5 = self.wait.until(EC.presence_of_element_located((By.ID, 'com.zhihu.android:id/main_tab_container')))
        el5.clear()
        # 由于刷新后页面不在首页，所以调回首页
        el6 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
            "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/"
            "android.support.v7.widget.LinearLayoutCompat/android.widget.HorizontalScrollView/"
            "android.widget.LinearLayout/android.support.v7.app.a.c[1]/android.support.v7.widget.LinearLayoutCompat")
        el6.click()

    def swipe(self):
        while True:
            # 注意，下拉后面的y值比前面的小，最后一个是时间，注意单位毫秒
            self.driver.swipe(300, 700, 300, 300, 1000)

    def main(self):
        # 打开知乎
        self.open()
        # 循环下拉
        time.sleep(5)
        self.swipe()


if __name__ == '__main__':
    main = Zhihu()
    main.main()
