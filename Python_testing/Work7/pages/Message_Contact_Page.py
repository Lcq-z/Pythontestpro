from appium.webdriver.common.mobileby import MobileBy
from Python_testing.Work7.pages.Base_Page7 import BasePage7
from Python_testing.Work7.pages.Search_Page import Search_Page


class Message_Contact_Page(BasePage7):
    # 定义appium server端口ip地址
    _appium_port = "http://127.0.0.1:4723/wd/hub"
    # 定义只在此类中使用的私有变量
    _click_contact = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/dqn'and@text='通讯录']")
    _click_search = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/guu']")
    _result = (MobileBy.XPATH, "//*[@resource-id='com.tencent.wework: id / b00']")

    # 创建方法：从消息通讯录页跳转至搜索页面
    def go_to_Search_Page(self):
        # 1. 点击通讯录  2. 点击通讯录内的搜索按钮
        self.find(*self._click_contact).click()
        self.find(*self._click_search).click()

        # 跳转至搜索页面，对Search_Page类进行实例化，表示业务逻辑的转换关系
        return Search_Page(self.driver)

    def get_member_list(self):
        # 拿到通讯录内的成员列表
        result1 = self.finds(*self._result)
        # 列表表达式
        return [member_list.text for member_list in result1]
