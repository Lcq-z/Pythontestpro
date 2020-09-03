from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestQiYeWeiXin:

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
        desired_caps['appPackage'] = 'com.tencent.wework'
        # 测试android设备中雪球app的欢迎页
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        # 用于保留上次登录数据，默认登录状态（这里的作用是：如果有软件更新弹窗，点击关闭后下次不再提示）
        desired_caps['noReset'] = 'true'
        # 执行测试用例之后，不停止app，停留在执行完毕页面可接着往下操作（可以在调试或者运行的时候提升运行速度）
        # desired_caps['dontStopAppOnReset'] = 'true'

        # 等待页面空闲的时间为1(主要解决动态画面加载过慢的问题)
        desired_caps['settings[waitForIdleTimeout]'] = 1

        # 跳过安装、权限设置等操作（可以在调试或者运行的时候提升运行速度）
        desired_caps['skipDeviceInitialization'] = 'true'

        # 用于识别到在输入框内输入的中文
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        # 一般来说，定位toast需要先设置以下 安卓工作引擎为：uiautomator2，但是在安卓中，此引擎是默认的，可以不写出来
        desired_caps['automationName'] = 'uiautomator2'

        # 固定写法：pycharm连接到appium的地址
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        # 隐式等待4秒，（很重要！待页面加载完毕，再进行定位操作）
        self.driver.implicitly_wait(4)

    def teardown(self):
        # back返回上一层的意思
        # self.driver.back()
        self.driver.quit()

    def test_Clock_in(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/ghc").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "次外出")]').click()
        result = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/mn").text
        assert "外出打卡成功" == result
