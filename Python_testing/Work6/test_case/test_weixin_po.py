from Python_testing.Work6.pages.message_page import Message_Page


class TestWeiXin:
    # 定义setup方法，每次方法执行前先执行setup内的实例化
    def setup(self):
        self.message = Message_Page()

    def test_weixin_daka(self):
        # 1.从企业微信消息页面跳转到工作台页面 2.工作台页面跳转到打卡页面  3.点击打卡按钮  3.打卡  4.获取到打卡成功后的信息
        result = self.message.go_to_WorkBench_Page().go_to_ClochIn_Page().Clock_in().get_Expected_results()
        # 断言：
        assert "外出打卡成功" in result

    def test_weixin_daka_fail(self):
        # 1.从企业微信消息页面跳转到工作台页面 2.工作台页面跳转到打卡页面  3.点击打卡按钮  3.打卡  4.获取到打卡后的信息
        result1 = self.message.go_to_WorkBench_Page().go_to_ClochIn_Page().Clock_in().get_Expected_results()
        # 断言：
        assert "外出打卡失败" not in result1

