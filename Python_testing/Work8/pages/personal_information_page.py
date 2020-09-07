from appium.webdriver.common.mobileby import MobileBy
from Python_testing.Work8.pages.Edit_Members_Page import EditMembersPage
from Python_testing.Work8.pages.base_page import BasePage

"""
成员个人信息页面
"""

class PersonalInformationPage(BasePage):
    # 定义只在此类中使用的私有变量
    _geng_duo = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/guk']")
    _bian_ji_cheng_yuan = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/azd'and@text='编辑成员']")

    def go_to_Edit_Members_Page(self):
        # 1. 点击成员信息内的更多按钮  2. 点击编辑成员
        self.find_and_click(self._geng_duo)
        self.find_and_click(self._bian_ji_cheng_yuan)

        # 跳转至编辑成员页面，对EditMembersPage类进行实例化，表示业务逻辑的转换关系
        return EditMembersPage(self.driver)













