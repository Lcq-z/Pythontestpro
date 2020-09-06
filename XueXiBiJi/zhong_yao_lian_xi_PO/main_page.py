from Python_testing.Work5.pages.BasePage import BasePage
from Python_testing.Work5.pages.add_member_page import AddMemberPage
from Python_testing.Work5.pages.contact_page import ContactPage


# 创建类：企业微信首页
class MainPage(BasePage):
    # 参考BasePage模块中的第二个if
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # 创建方法：点击通讯录
    def go_to_contact(self):
        # self.driver.find_element_by_xpath("//*[@id='menu_contacts']/span")

        # 跳转至通讯录页面，对ContactPage类进行实例化，表示业务逻辑的转换关系
        return ContactPage(self.driver)

    # 创建方法：点击添加成员
    def go_to_add_meber(self):
        # self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap").click()

        # 跳转至添加成员页面，对AddMemberPage类进行实例化，表示业务逻辑的转换关系
        return AddMemberPage(self.driver)
