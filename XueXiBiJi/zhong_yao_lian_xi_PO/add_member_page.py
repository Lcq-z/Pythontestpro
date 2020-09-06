from selenium.webdriver.common.by import By
from Python_testing.Work5.pages.BasePage import BasePage
from Python_testing.Work5.pages.contact_page import ContactPage


# 创建类：添加成员页面
class AddMemberPage(BasePage):
    # 变量名前面加上下划线，让其作为本模块私有的变量，不在其他模块中显示
    _username = (By.ID, "username")
    _memberAdd_acctid = (By.ID, "memberAdd_acctid")
    _memberAdd_phone = (By.ID, "memberAdd_phone")
    _js_btn_save = (By.CSS_SELECTOR, ".js_btn_save")
    _js_btn_cancel = (By.CSS_SELECTOR, ".js_btn_cancel")
    _js_btn_likai = (By.CSS_SELECTOR, "[node-type='cancel']")

    # 创建方法：添加成员
    def add_menmber(self, name, acctid, phone):
        # 上面已经定义变量了，这里直接传入变量名并加上*号对定义的元组进行解包
        self.driver.find_element(*self._username).send_keys(name)
        self.driver.find_element(*self._memberAdd_acctid).send_keys(acctid)
        self.driver.find_element(*self._memberAdd_phone).send_keys(phone)

        # return self是为了实现返回当前页面时依然可以实现链式调用
        return self

    # 创建方法：点击保存按钮
    def save_member(self):
        # 上面已经定义变量了，这里直接传入变量名并加上*号对定义的元组进行解包
        self.driver.find_element(*self._js_btn_save).click()

        # 跳转至通讯录页面，对ContactPage类进行实例化，表示业务逻辑的转换关系
        return ContactPage(self.driver)

    # 创建方法：点击取消按钮
    def cancel_member(self):
        # 上面已经定义变量了，这里直接传入变量名并加上*号对定义的元组进行解包
        self.driver.find_element(*self._js_btn_cancel).click()
        self.driver.find_element(*self._js_btn_likai).click()

        # 跳转至通讯录页面，对ContactPage类进行实例化，表示业务逻辑的转换关系
        return ContactPage(self.driver)

