from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class BasePage7:
    _appium_port = ""

    def __init__(self, driver_base=None):
        if driver_base is None:
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
            desired_caps['dontStopAppOnReset'] = 'true'

            # 等待页面空闲的时间为1(主要解决动态画面加载过慢的问题)
            desired_caps['settings[waitForIdleTimeout]'] = 1

            # 跳过安装、权限设置等操作（可以在调试或者运行的时候提升运行速度）
            desired_caps['skipDeviceInitialization'] = 'true'

            # 用于识别到在输入框内输入的中文
            desired_caps['unicodeKeyBoard'] = 'true'
            desired_caps['resetKeyBoard'] = 'true'

            # 一般来说，定位toast需要先设置以下 安卓工作引擎为：uiautomator2，但是在安卓中，此引擎是默认的，可以不写出来
            desired_caps['automationName'] = 'uiautomator2'

            if self._appium_port != "":
                # 固定写法：pycharm连接到appium的地址
                self.driver = webdriver.Remote(self._appium_port, desired_caps)

            # 隐式等待10秒，（很重要！等页面加载完毕，再进行定位操作）
            self.driver.implicitly_wait(10)

        else:
            # 加的注解，为了在其他页面模块中调用到self.driver
            self.driver: WebDriver = driver_base  # 注意：测试用例中是调用不到self.driver的，可以重新封装一个方法，专门用于存放app启动退出操作

    # 对find_element进行封装，实现PO实际模式，并且让代码的可读性更高、更加美观
    def find(self, by, value):
        return self.driver.find_element(by, value)

    # 对find_elements进行封装，现PO实际模式，并且让代码的可读性更高、更加美观
    def finds(self, by, value):
        return self.driver.find_elements(by, value)

    # 定义退出方法
    def quit_page(self):
        return self.driver.quit()
