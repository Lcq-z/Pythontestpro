from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Python_testing.Work7.pages.Base_Page7 import BasePage7


class Edit_Members_Page(BasePage7):
    # 定义只在此类中使用的私有变量
    _delete_button = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/duq'and@text='删除成员']")
    _ok_button = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b_4'and@text='确定']")
    _cancer = (MobileBy.ID, "com.tencent.wework:id/gu_")

    def edit_member(self):
        # 解决循环导入问题
        from Python_testing.Work7.pages.Message_Contact_Page import Message_Contact_Page
        # 1. 点击编辑成员界面内的删除成员按钮-弹出提示框  2. 点击提示框内的确定按钮
        self.find(*self._delete_button).click()

        self.find(*self._ok_button).click()
        # 显示等待：当删除成员后，会返回到搜索框，这时需要等搜索框内的返回按钮加载完成后,再进行下面的操作
        WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(self._cancer))

        # 点击搜索框旁边的返回按钮
        self.find(*self._cancer).click()

        # return Message_Contact_Page是为了实现返回到通讯录页面获取到成员列表
        return Message_Contact_Page()
