from time import sleep
from selenium.webdriver.common.by import By
from Python_testing.Work5.pages.BasePage import BasePage


# 创建类：通讯录页面
class ContactPage(BasePage):
    # 定义只在此类中使用的私有变量
    _tong_xun_lu = (By.XPATH, '//*[@id="menu_contacts"]//span')
    _dian_ji_jia_hao = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    _add_department = (By.CSS_SELECTOR, ".js_create_party")
    _bu_men_lie_biao = (By.CSS_SELECTOR, ".jstree-anchor")

    def go_to_add_department(self):
        # 解决循环导入问题
        from Python_testing.Work5.pages.add_department_page import AddDepartmentPage

        # 1.点击通讯录  2. 点击添加部门的加号icon  3. 点击添加部门
        self.find(*self._tong_xun_lu).click()
        self.find(*self._dian_ji_jia_hao).click()
        self.find(*self._add_department).click()

        # 跳转至添加成员页面，对AddMemberPage类进行实例化，表示业务逻辑的转换关系
        return AddDepartmentPage(self.driver)

    def get_department_list(self):
        # 因为页面切换太快导致元素未加载，无法提取到部门列表，所以加入强制等待
        sleep(2)
        # 定位到企业微信通讯录中已添加部门的列表后赋值给dep_liebiao
        dep_liebiao = self.finds(*self._bu_men_lie_biao)

        # 列表推导式写法，因为定位到内容后打印出来是js代码格式，所以使用此方法来提取出已添加部门的字符串格式
        return [dep_name.text for dep_name in dep_liebiao]
        # 与上方列表推导式作用一样，只不过列表推导式更简洁
        # list1 = []
        # for name in liebiao:
        #     list1.append(name.text)
        # print(list1)
