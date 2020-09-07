from appium.webdriver.common.mobileby import MobileBy
from Python_testing.Work8.pages.Member_information_page import MemberInformationPage
from Python_testing.Work8.pages.base_page import BasePage

"""
添加成员按钮界面
"""

class AddMemberPage(BasePage):
    # 定义只在此类中使用的私有变量
    _manual_input = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    _gettoast = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def go_to_Member_information(self):
        self.find_and_click(self._manual_input)
        # 跳转至添加成员页面，对MemberInformationPage类进行实例化，表示业务逻辑的转换关系
        return MemberInformationPage(self.driver)

    def get_toast(self):
        # 获取到元素的text值后，return到返回值用于断言
        mytoast = self.find(self._gettoast).text
        return mytoast
