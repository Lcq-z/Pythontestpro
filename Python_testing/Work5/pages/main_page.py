from Python_testing.Work5.pages.BasePage import BasePage
from Python_testing.Work5.pages.contact_page import ContactPage


# 创建类：企业微信首页
class MainPage(BasePage):
    # 参考BasePage模块中的第二个if
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    # 创建方法：点击通讯录
    def go_to_contact(self):
        # 跳转至通讯录页面，对ContactPage类进行实例化，表示业务逻辑的转换关系
        return ContactPage(self.driver)
