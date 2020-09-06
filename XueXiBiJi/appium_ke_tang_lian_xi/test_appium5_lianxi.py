from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from XueXiBiJi.appium_ke_tang_lian_xi.Appium_BasePage import Appium_BasePage


# 练习1：在雪球app内实现往上滑动（获取到应用窗口的宽和高以及坐标x、y值来设置滑动）
# 创建类：继承于Appium_BasePage
class Test_shoushi(Appium_BasePage):

    def test_huadong(self):
        # 调用TouchAction方法，传入self.driver赋值给变量action
        action = TouchAction(self.driver)

        # 获取应用窗口的宽和高以及坐标x、y值
        window_rect = self.driver.get_window_rect()
        # 使用width变量拿到window_rect中的width值
        width = window_rect['width']
        # 使用height变量拿到window_rect中的height值
        height = window_rect['height']
        # 将width的值除以2并转换为整数赋值给x1
        x1_start = int(width / 2)
        # 将height的值乘以5分之4 并转换为整数赋值给y_start
        y_start = int(height * 4 / 5)
        # 将height的值乘以5分之1 并转换为整数赋值给y_end
        y_end = int(height * 1 / 5)

        # 实现滑动屏幕
        # press：点击  wait：等待，单位毫秒  move_to：移动  release：释放，松开  perform：TouchAction方法的语法结构，执行时的必要参数
        action.press(x=x1_start, y=y_start).wait(200).move_to(x=x1_start, y=y_end).release().perform()


# 练习2：打开木木模拟器的手势锁应用，滑动手势（仅作练习，不推荐直接使用坐标定位）
class Test_jiesuo:

    def setup(self):
        # 定义字典
        desired_caps = {}
        # 测试的设备为android系统
        desired_caps['platformName'] = 'android'
        # android系统版本为6.0
        desired_caps['platformVersion'] = '6.0'
        # 连接设备的ip地址
        desired_caps['deviceName'] = '127.0.0.1:7555'
        # 测试android设备中的手势锁app
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        # 测试android设备中手势锁app主页面
        desired_caps['appActivity'] = 'com.samsung.ui.FlashActivity'
        # 用于保留上次登录数据，默认登录状态（这里的作用是：如果有软件更新弹窗，点击关闭后下次不再提示）
        desired_caps['noReset'] = 'true'
        # 执行测试用例之后，不停止app，停留在执行完毕页面可接着往下操作（可以在调试或者运行的时候提升运行速度）
        # desired_caps['dontStopAppOnReset'] = 'true'

        # 跳过安装、权限设置等操作（可以在调试或者运行的时候提升运行速度）
        desired_caps['skipDeviceInitialization'] = 'true'

        # 用于识别到在输入框内输入的中文
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        # 固定写法：pycharm连接到appium的地址
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        # 隐式等待10秒，（很重要！等页面加载完毕，再进行定位操作）
        self.driver.implicitly_wait(10)

    def teardown(self):
        # back返回上一层的意思
        # self.driver.back()
        # self.driver.back()

        self.driver.quit()

    def test_shoushi(self):
        # 定位到元素后点击
        self.driver.find_element_by_id("cn.kmob.screenfingermovelock:id/lockerCheckBox").click()
        # 调用TouchAction方法，传入self.driver赋值给变量action1
        action1 = TouchAction(self.driver)
        sleep(2)
        # 在mumu模拟器上创建手势锁
        action1.press(x=355, y=171).wait(200).press(x=355, y=410).wait(200).press(x=355, y=647).wait(200).press(x=600,
                                                                                                                y=653).release().perform()
