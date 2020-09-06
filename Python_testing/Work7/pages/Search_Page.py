from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Python_testing.Work7.pages.Base_Page7 import BasePage7
from Python_testing.Work7.pages.Member_Information_Page import Member_Information_Page


class Search_Page(BasePage7):
    # 定义只在此类中使用的私有变量
    _send_search = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/fk1'and@text='搜索']")
    _click_member = (MobileBy.ID, "com.tencent.wework:id/d2f")

    def go_to_Member_Information_Page(self, member_name):
        # 1. 在输入框搜索成员姓名  2. 点击成员姓名
        self.find(*self._send_search).send_keys(member_name)
        # 显示等待：当搜索成员后，加载需要时间，这时需要等搜索框到的结果可点击时,再进行下面的操作
        WebDriverWait(self.driver, 6).until(expected_conditions.element_to_be_clickable(self._click_member))
        # 点击搜索到的内容
        self.find(*self._click_member).click()

        # 跳转至成员信息页面，对Member_Information_Page类进行实例化，表示业务逻辑的转换关系
        return Member_Information_Page(self.driver)
