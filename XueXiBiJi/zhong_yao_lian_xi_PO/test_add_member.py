from Python_testing.Work5.pages.BasePage import BasePage
from Python_testing.Work5.pages.main_page import MainPage


class TestAddMember:

    # 定义setup方法，每次方法执行前先执行setup内的实例化
    def setup(self):
        self.main = MainPage()


    def test_add_menmber(self):

        # 1.从首页跳转到添加成员页面  2.添加成员  3.点击保存按钮  4.获取到企业微信通讯录下的text元素
        name_list = self.main.go_to_add_meber().add_menmber("zed","124123","12455555555").save_member().get_member_list()
        # 断言已添加的ace是在测试用例当中（断言需要和其他模块分离，不需要和用例分离）
        assert "zed" in name_list  # 问：如果添加了100个成员，那100个都要做断言，写100个assert语句吗？
                                   # 答：可以将所有zed换成变量name， 使用pytest的fixture方法来传参


    def test_cancel(self):
        # 1.从首页跳转到添加成员页面  2.添加成员  3.点击取消保存按钮  4.获取到企业微信通讯录下的text元素
        name_list1 = self.main.go_to_add_meber().add_menmber("zed2","124123","12455555555").cancel_member().get_member_list()
        # 断言已添加的ace2 不在测试用例当中（断言需要和其他模块分离，不需要和用例分离）
        assert "zed2" not in name_list1


    def test_contact_member(self):

        # 1.从首页跳转到通讯录页面  2.从通讯录页面跳转到添加成员页面  3.添加成员  4.点击保存按钮
        self.main.go_to_add_meber().add_menmber("zed","124123","12455555555").save_member().get_member_list()
