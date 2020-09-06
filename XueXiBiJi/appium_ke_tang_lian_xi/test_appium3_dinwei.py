import pytest
from appium import webdriver


class TestDw:

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
        self.driver.back()
        self.driver.back()

        self.driver.quit()

    def test_ceshi_din_wei(self):
        # 定位到元素后点击
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        # 定位到元素后输入"阿里巴巴"
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        # 定位到元素后点击
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        # 1.获取到元素的text属性  2.将获取到的元素text属性转换为float类型  3.赋值给gujia
        gujia = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        # 断言gujia是否大于200
        assert gujia > 200
