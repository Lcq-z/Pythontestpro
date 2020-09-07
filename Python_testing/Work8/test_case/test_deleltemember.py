from Python_testing.Work8.pages.app import AppPage


class TestAddMember:
    # 每次执行测试用例前先执行setup中的操作
    def setup(self):
        # 对AppPage()进行实例化
        self.app = AppPage()
        # 调用self.app中的跳转首页再赋值给self.main
        self.main = self.app.start_app().go_to_main()

    # 每次执行测试用例后再执行teardown中的操作
    def teardown(self):
        self.app.stop_app()

    def test_delete_member(self):
        name = "骚磊"
        # 1.从企业微信首页跳转到通讯录页面  2.从通讯录页面跳转到搜索页面 3.从搜索页面输入内容跳转到个人信息页面 4.从个人信息页面跳转到编辑成员页面 5.编辑成员页面删除成员
        result = self.main.go_to_cantact().go_to_search().go_to_Member_Information_Page(
            name).go_to_Edit_Members_Page().edit_member()
        # 将result.get_member_list()获取到删除成员成功的成员列表 赋值给my_toast，用于断言
        member_list = result.get_member_list()
        # 断言:
        assert "骚磊" not in member_list
