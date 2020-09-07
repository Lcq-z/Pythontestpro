from appium.webdriver.common.mobileby import MobileBy
from Python_testing.Work8.pages.base_page import BasePage
from Python_testing.Work8.pages.contact_page import ContactPage

"""
首页
"""

class MainPage(BasePage):
    # 定义只在此类中使用的私有变量
    _contact_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def go_to_cantact(self):
        self.find_and_click(self._contact_element)
        # 跳转至添加成员页面，对ContactPage类进行实例化，表示业务逻辑的转换关系
        return ContactPage(self.driver)
