from Python_testing.Work7.pages.Message_Contact_Page import Message_Contact_Page


class TestDeleteMember:
    # 定义setup方法，每次方法执行前先执行setup内的实例化
    def setup(self):
        self.message = Message_Contact_Page()

    # 定义teardown方法,每次方法执行完毕后,调用退出方法
    def teardown(self):
        self.message.quit_page()

    def test_delete_member(self):
        # 1.从企业微信消息,通讯录页面跳转到搜索页面
        # 2.搜索页面输入内容跳转到成员信息页面
        # 3.成员信息页面跳转至编辑成员页面
        # 4.编辑成员页面删除成员
        # 5.获取到删除成员成功后的信息
        result = self.message.go_to_Search_Page().go_to_Member_Information_Page("骚磊").go_to_Edit_Members_Page().edit_member().get_member_list()
        # 断言:
        assert "骚磊" not in result
