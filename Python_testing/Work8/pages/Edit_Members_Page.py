from appium.webdriver.common.mobileby import MobileBy
from Python_testing.Work8.pages.base_page import BasePage

"""
编辑成员页面
"""

class EditMembersPage(BasePage):
    # 定义只在此类中使用的私有变量
    _delete_button = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/duq'and@text='删除成员']")
    # _delete_button1 = "删除成员"
    _ok_button = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b_4'and@text='确定']")
    _cancer = (MobileBy.ID, "com.tencent.wework:id/gu_")

    def edit_member(self):
        from XueXiBiJi.pytest_zhibo.app.page_object_zhibo.pages.contact_page import ContactPage
        # 解决循环导入问题

        # 1. 点击编辑成员界面内的删除成员按钮-弹出提示框  2. 点击提示框内的确定按钮
        self.find_and_click(self._delete_button)
        # self.find_swipe_click(self._delete_button1)
        self.find_and_click(self._ok_button)
        # 显示等待：当删除成员后，会返回到搜索框，这时需要等搜索框内的返回按钮加载完成后,再进行下面的操作
        self.show_wait(self._cancer)

        # 点击搜索框旁边的返回按钮
        self.find_and_click(self._cancer)
        # return Message_Contact_Page是为了实现返回到通讯录页面获取到成员列表
        return ContactPage(self.driver)
