# 以雪球app交易页面的A股开户webview（H5）页面为例
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
    def setup(self):
        des_caps = {
            'plptformName': 'android',
            'platformVersion': '6.0',
            'appPackage': 'com.xueqiu.android',
            'appActivity': 'com.xueqiu.android.common.MainActivity',
            # browserName':'Chrome',
            'deviceName': '192.168.56.101:5555',
            'noReset': 'true',
            # 'deviceName':lemulator-5554',

            # 意思得问老师
            'skipServerInstallation': 'true',

            # 指定driver存在的本地路径（在安装appium时，会有一个默认存放driver的路径，如果此路径下的driver版本过老，或者没有的话，就必须得新指定）
            'chromedriverExecutable': '本地存放的driver路径(例：/Users/chromedriver)'
        }
        # 语法结构：连接appium server的端口
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):

        # 点击交易
        self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']").click()
        A_locator = (MobileBy.XPATH, '//*[@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]/h1')

        # 打印一下切换的webview页面
        # print(self.driver.contexts)
        # 通过qppium提供的switch_to方法将原生切换到webview(H5)页面，切换上下文，固定写法
        self.driver.switch_to.context(self.driver.contexts[-1]) # 一般来说，新打开的webview页面，都是最后一位，所以这里切换到-1，也就是最后一位
                                                                # 如果是乱的，就可以使用遍历的方法来找到新打开的webview页面

        # 打印当前页面
        # print(self.driver.window_handles)

        # 显示等待10秒，配合until(expected_conditions.element_to_be_clickable(元素名))判断元素是否可被点击
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(A_locator))

        # 上面条件判断完成之后再点击'A股开户'
        self.driver.find_element(*A_locator).click()

        B_locator = (MobileBy.ID, 'phone-number')
        # 显示等待20秒，配合until(expected_conditions.element_to_be_clickable(元素名))判断元素是否可被点击
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(B_locator))

        # 输入用户名和验证码，点击立即开户
        self.driver.find_element(*B_locator).send_keys("13810100202")
        self.driver.find_element(MobileBy.ID, 'code').send_keys("1234")
        self.driver.find_element(MobileBy.XPATH, "/html/body/div/div/div[2]/div/div[2]/h1").click()

