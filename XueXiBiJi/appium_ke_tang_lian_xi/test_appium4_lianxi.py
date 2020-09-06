import pytest
from appium import webdriver


class TestLainXi:

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

    def test_ceshi_lian_xi(self):
        """
        打开【雪球】应用首页  (在上面的setup中以完成)
        定位首页的搜索框
        判断搜索框的是否可用，并查看搜索框text属性值
        打印搜索框这个元素的左上角坐标和它的宽高
        向搜索框输入：alibaba
        判断【阿里巴巴】是否可见
        如果可见，打印“搜索成功“点击，如果不可见，打印“搜索失败”

        """
        # 定位首页的搜索框并赋值给ssk
        ssk = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        # 将ssk.is_enabled()赋值给element1，然后放一边，等下面需要使用时再调用
        element1 = ssk.is_enabled()
        # 打印ssk的text属性
        print(ssk.text)
        # 打印ssk的左上角坐标
        print(ssk.location)
        # 打印ssk的宽高
        print(ssk.size)
        # 如果element1可用并返回为True的话，执行if中的代码
        if element1 == True:
            # 点击搜索框
            ssk.click()
            # 接着在搜索框中输入alibaba
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            # 定位到元素后赋值给panduan
            suosou = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # 这里拆分一下：1. 先获取到变量suosou的displayed属性  2. 如果获取到的属性为'true'的话就执行if下方的操作
            if suosou.get_attribute("displayed") == 'true':
                print(suosou.get_attribute("displayed"))
                print("搜索成功")
            else:
                print("搜索失败")
