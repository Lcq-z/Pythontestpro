from appium.webdriver.common.mobileby import MobileBy
from Python_testing.Work6.pages.BasePage6 import BasePage6
from Python_testing.Work6.pages.workbench_page import WorkBench_Page


class Message_Page(BasePage6):
    # 定义appium server端口ip地址
    _appium_port = "http://127.0.0.1:4723/wd/hub"
    # 定义只在此类中使用的私有变量
    _dianji_workbench = (MobileBy.XPATH, "//*[@text='工作台']")

    # 创建方法：跳转至工作台页面
    def go_to_WorkBench_Page(self):
        # 点击工作台
        self.find(*self._dianji_workbench).click()
        # 跳转至工作台页面，对WorkBench_Page类进行实例化，表示业务逻辑的转换关系
        return WorkBench_Page(self.driver)
