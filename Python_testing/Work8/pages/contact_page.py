from appium.webdriver.common.mobileby import MobileBy
from Python_testing.Work8.pages.Search_Page import Search_Page
from Python_testing.Work8.pages.add_member_page import AddMemberPage
from Python_testing.Work8.pages.base_page import BasePage

"""
通讯录页面
"""

class ContactPage(BasePage):
    # 定义只在此类中使用的私有变量
    _addmember_element = "添加成员"
    _click_search = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/guu']")
    _result = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework: id / b00']")
    def go_to_addmember(self):
        self.find_swipe_click(self._addmember_element)
        # 跳转至添加成员页面，对AddMemberPage类进行实例化，表示业务逻辑的转换关系
        return AddMemberPage(self.driver)

    def go_to_search(self):
        self.find_and_click(self._click_search)
        return Search_Page(self.driver)

    def get_member_list(self):
        # 拿到通讯录内的成员列表
        result1 = self.finds(self._result)
        # 列表表达式
        return [member_list.text for member_list in result1]