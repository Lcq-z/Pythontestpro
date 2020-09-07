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

    def test_add_member(self):
        name = "骚磊"
        gender = "男"
        phonenum = "12339112849"
        # 1.从首页跳转到通讯录 2.从通讯录跳转到添加成员页面 3.从添加成员页面跳转到编辑页面 4.输入姓名 5.选择年龄 6.输入电话号码 7.点击保存按钮后回到添加成员页面
        my_page = self.main.go_to_cantact().go_to_addmember().go_to_Member_information().edit_name(name).edit_gender(
            gender).edit_phonenum(phonenum).save_and_click()
        # 将my_page.get_toast()获取到添加成员成功的toast信息 赋值给my_toast，用于断言
        my_toast = my_page.get_toast()
        # 断言
        assert "添加成功" == my_toast

