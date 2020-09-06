from appium.webdriver.common.mobileby import MobileBy
from Python_testing.Work7.pages.Base_Page7 import BasePage7
from Python_testing.Work7.pages.Edit_Members_Page import Edit_Members_Page


class Member_Information_Page(BasePage7):
    # 定义只在此类中使用的私有变量
    _geng_duo = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/guk']")
    _bian_ji_cheng_yuan = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/azd'and@text='编辑成员']")

    def go_to_Edit_Members_Page(self):
        # 1. 点击成员信息内的更多按钮  2. 点击编辑成员
        self.find(*self._geng_duo).click()
        self.find(*self._bian_ji_cheng_yuan).click()

        # 跳转至编辑成员页面，对Edit_Members_Page类进行实例化，表示业务逻辑的转换关系
        return Edit_Members_Page(self.driver)
