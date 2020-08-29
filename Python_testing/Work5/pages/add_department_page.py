from selenium.webdriver.common.by import By
from Python_testing.Work5.pages.BasePage import BasePage
from Python_testing.Work5.pages.contact_page import ContactPage


class AddDepartmentPage(BasePage):
    # 定义只在此类中使用的私有变量
    _department_name = (By.CSS_SELECTOR, ".ww_inputText:nth-child(2)")
    _click_department = (By.CSS_SELECTOR, ".js_toggle_party_list")
    _choice_department = (By.CSS_SELECTOR, "[class ='qui_dropdownMenu ww_dropdownMenu member_colLeft js_party_list_container']")
    _determine_button = (By.CSS_SELECTOR, "#__dialog__MNDialog__ [d_ck='submit']")
    _Cancel_button = (By.CSS_SELECTOR, "#__dialog__MNDialog__ [d_ck='cancel']")

    # 创建方法：添加部门
    def add_department(self, name):
        # 上面已经定义变量了，这里直接传入变量名并加上*号对定义的元组进行解包
        self.find(*self._department_name).send_keys(name)
        self.find(*self._click_department).click()
        dep = self.find(*self._choice_department).click()

        # 因为添加部门列表列表后，位置会发生变动，所以加了一层判断
        # 当dep非空的时候，点击dep中的第一个元素
        if dep is not None:
            dep[0].click()

        # return self是为了实现返回当前页面时依然可以实现链式调用
        return self

    # 创建方法：点击添加部门界面的确定按钮
    def save_department(self):
        # 上面已经定义变量了，这里直接传入变量名并加上*号对定义的元组进行解包
        self.find(*self._determine_button).click()

        # 跳转至通讯录页面，对ContactPage类进行实例化，表示业务逻辑的转换关系
        return ContactPage(self.driver)

    # 创建方法：点击添加部门界面的取消按钮
    def cancel_department(self):
        # 上面已经定义变量了，这里直接传入变量名并加上*号对定义的元组进行解包
        self.find(*self._Cancel_button).click()

        # 跳转至通讯录页面，对ContactPage类进行实例化，表示业务逻辑的转换关系
        return ContactPage(self.driver)
