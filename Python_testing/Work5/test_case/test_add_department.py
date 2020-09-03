from Python_testing.Work5.pages.main_page import MainPage


class TestAddDepartment:
    # 定义setup方法，每次方法执行前先执行setup内的实例化
    def setup(self):
        self.main = MainPage()

    def test_add_department(self):
        # 1.从首页跳转到添加部门页面  2.添加部门  3.点击保存按钮  4.获取到企业微信通讯录下的部门元素
        department_list = self.main.go_to_contact().go_to_add_department().add_department("人事部").save_department().get_department_list()
        # 断言已添加的ace是在测试用例当中（断言需要和其他模块分离，不需要和用例分离）
        assert "人事部" in department_list  # 问：如果添加了100个成员，那100个都要做断言，写100个assert语句吗？
                                            # 答：可以将所有zed换成变量name， 使用pytest的fixture方法来传参

    def test_cancel_department(self):
        # 1.从首页跳转到添加部门页面  2.添加部门  3.点击取消按钮  4.获取到企业微信通讯录下的部门元素
        department_list = self.main.go_to_contact().go_to_add_department().add_department("人事部").cancel_department().get_department_list()
        # 断言已添加的ace是在测试用例当中（断言需要和其他模块分离，不需要和用例分离）
        assert "人事部-1" not in department_list
