from Python_testing.Work5.pages.BasePage import BasePage


# 创建类：通讯录页面



class ContactPage(BasePage):

    # 创建方法：点击添加成员
    def go_to_add_member(self):
        # 解决循环导入问题
        from XueXiBiJi.zhong_yao_lian_xi_PO.add_member_page import AddMemberPage

        # 跳转至添加成员页面，对AddMemberPage类进行实例化，表示业务逻辑的转换关系
        return AddMemberPage(self.driver)


    def get_member_list(self):
        # 定位到企业微信通讯录中已添加成员的列表后赋值给liebiao
        liebiao = self.driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")

        # 列表推导式写法，因为定位到内容后打印出来是js代码格式，所以使用此方法来提取出已添加部门的字符串格式
        return [name.text for name in liebiao]
        # 与上方列表推导式作用一样，只不过列表推导式更简洁
        # list1 = []
        # for name in liebiao:
        #     list1.append(name.text)
        # print(list1)
