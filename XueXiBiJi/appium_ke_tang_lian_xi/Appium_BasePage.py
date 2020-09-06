from time import sleep

import pytest
from appium import webdriver


class Appium_BasePage:

    def setup(self):
        # 定义字典
        desired_caps = {}
        # 测试的设备为android系统
        desired_caps['platformName'] = 'android'
        # android系统版本为6.0
        desired_caps['platformVersion'] = '6.0'
        # 连接设备的ip地址
        desired_caps['deviceName'] = '127.0.0.1:7555'
        # 测试android设备中的雪球app
        desired_caps['appPackage'] = 'com.xueqiu.android'
        # 测试android设备中雪球app的欢迎页
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        # 用于保留上次登录数据，默认登录状态（这里的作用是：如果有软件更新弹窗，点击关闭后下次不再提示）
        desired_caps['noReset'] = 'true'
        # 执行测试用例之后，不停止app，停留在执行完毕页面可接着往下操作（可以在调试或者运行的时候提升运行速度）
        desired_caps['dontStopAppOnReset'] = 'true'

        # 跳过安装、权限设置等操作（可以在调试或者运行的时候提升运行速度）
        desired_caps['skipDeviceInitialization'] = 'true'

        # 用于识别到在输入框内输入的中文
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        # 固定写法：pycharm连接到appium的地址
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        # 隐式等待10秒，（很重要！等页面加载完毕，再进行定位操作）
        self.driver.implicitly_wait(10)

        # 仅为进入雪球app提供点击跳过广告页，进入其他应用可注释掉
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_skip").click()

    def teardown(self):
        # back返回上一层的意思
        # self.driver.back()
        # self.driver.back()

        self.driver.quit()