import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
from XueXiBiJi.appium_ke_tang_lian_xi.Appium_BasePage import Appium_BasePage



class TestCanshuhua:


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
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/action_close").click()

        # self.driver.quit()

    @pytest.mark.parametrize('name,weizhi,piaojia',[

        ('阿里巴巴','BABA', 290)

    ])
    def test_chuan_can(self,name,weizhi,piaojia):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/name']").click()
        gp = self.driver.find_element(MobileBy.XPATH,f"//*[@text={weizhi}]/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        piaojia = float(gp.text)

        print(f"这只股票的价格是{piaojia}")

        assert_that(piaojia,close_to(piaojia,piaojia*0.1))


