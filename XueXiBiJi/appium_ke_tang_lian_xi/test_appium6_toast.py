from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class Test_toast:

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
        desired_caps['appPackage'] = 'io.appium.android.apis'
        # 测试android设备中雪球app的欢迎页
        desired_caps['appActivity'] = 'io.appium.android.apis.view.PopupMenu1'
        # 用于保留上次登录数据，默认登录状态（这里的作用是：如果有软件更新弹窗，点击关闭后下次不再提示）
        desired_caps['noReset'] = 'true'
        # 执行测试用例之后，不停止app，停留在执行完毕页面可接着往下操作（可以在调试或者运行的时候提升运行速度）
        # desired_caps['dontStopAppOnReset'] = 'true'

        # 跳过安装、权限设置等操作（可以在调试或者运行的时候提升运行速度）
        desired_caps['skipDeviceInitialization'] = 'true'

        # 用于识别到在输入框内输入的中文
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        # 一般来说，定位toast需要先设置以下 安卓工作引擎=为：uiautomator2，但是在安卓中，此引擎是默认的，可以不写出来
        desired_caps['automationName'] = 'uiautomator2'


        # 固定写法：pycharm连接到appium的地址
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

        # 隐式等待10秒，（很重要！等页面加载完毕，再进行定位操作）
        self.driver.implicitly_wait(10)

    def teardown(self):
        # back返回上一层的意思
        # self.driver.back()
        # self.driver.back()
        self.driver.quit()


    def test_toast1(self):
        # 使用 MobileBy.ACCESSIBILITY_ID 方法定位到元素后点击
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"Make a Popup!").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/title']").click()

        # page_source参数可以打印出当前页面的dom树结构,将打印的内容复制到 toast1.xml文件内查看其属性
        # print(self.driver.page_source)

        # 获取到toast属性的两种方法：（作用：获取之后可做toast文案断言）
        # 使用MobileBy.XPATH定位到toast的class属性后，再提取text的值
        print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        # 意思同上，contains：模糊搜索
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'Clicked popup')]").text)
