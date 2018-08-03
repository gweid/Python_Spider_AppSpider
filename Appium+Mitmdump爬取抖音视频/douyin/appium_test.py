from appium import webdriver


class Douyin():
    def __init__(self):
        """
        初始化参数
        """
        self.server = 'http://localhost:4723/wd/hub'
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "MI_5",
            "appPackage": "com.ss.android.ugc.aweme",
            "appActivity": ".main.MainActivity"
        }
        self.driver = webdriver.Remote(self.server, self.desired_caps)

    def enter(self):
        """
        进入抖音，循环向上滑动
        :return:
        """
        # 点击一下屏幕，确保页面显示
        self.driver.tap([(300, 500)], 500)
        # 循环向上滑动
        while True:
            self.driver.swipe(300, 500, 300, 1100, 5000)

    def main(self):
        self.enter()


if __name__ == '__main__':
    main = Douyin()
    main.main()
