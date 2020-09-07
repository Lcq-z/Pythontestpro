from appium import webdriver
from Python_testing.Work8.pages.base_page import BasePage
from Python_testing.Work8.pages.main_page import MainPage

"""
存放app的启动、退出、重启
"""

class AppPage(BasePage):
    def start_app(self):
        """
        启动app

        """
        # 这里解释一下为什么要使用if，别的模块每次return到其他页面都算一次类的实例化，子类继承父类后每次实例化都会调用BasePage中的init构造方法
        # 如果不加if的话，类实例化时就会一直区打开app，导致用例执行失败，加上if，第一次实例化打开app之后，因为其他子，类不等于None了，就会执行下面的else
        if self.driver == None:
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

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

            # 隐式等待10秒，（很重要！等页面加载完毕，再进行定位操作）
            self.driver.implicitly_wait(5)

        else:
            # launch_app() 启动 desirecap 里面设置的appActivity
            self.driver.launch_app()
        # return self是为了实现返回当前页面时依然可以实现链式调用
        return self

    def stop_app(self):
        self.driver.quit()

    def restart(self):

        self.driver.close_app()
        self.driver.launch_app()

    # ->代表添加一个返回值的类型，这里的意思是返回到MainPage页面
    def go_to_main(self) -> MainPage:
        # 跳转至通讯录页面，对MainPage类进行实例化，表示业务逻辑的转换关系
        return MainPage(self.driver)
