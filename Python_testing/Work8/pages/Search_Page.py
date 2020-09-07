from appium.webdriver.common.mobileby import MobileBy
from Python_testing.Work8.pages.base_page import BasePage
from Python_testing.Work8.pages.personal_information_page import PersonalInformationPage

"""
搜索界面
"""
class Search_Page(BasePage):
    # 定义只在此类中使用的私有变量
    _send_search = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/fk1'and@text='搜索']")
    _click_member = (MobileBy.ID, "com.tencent.wework:id/d2f")

    def go_to_Member_Information_Page(self, member_name):
        # 在输入框搜索成员姓名
        self.find_and_sendkys(self._send_search, member_name)

        # 显示等待：当搜索成员后，加载需要时间，这时需要等搜索框到的结果可点击时,再进行下面的操作
        self.show_wait(self._click_member)

        # 点击搜索到的内容
        self.find_and_click(self._click_member)

        # 跳转至成员信息页面，对Member_Information_Page类进行实例化，表示业务逻辑的转换关系
        return PersonalInformationPage(self.driver)
