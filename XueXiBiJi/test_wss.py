# # testsum(self, a, b, result):
# #     # if isinstance(a, (
# #     # int, float)) and isinstance(b,
# #     #                             (int, float)):
# #     #     r = round(self.calcu.add(a, b), 2)
# #     #     assert result == r
# #     #
# #     # else:
# #     #     pass
# #     # 当传入值有误时做相应处理,无误时对数据正常操作且与预期结果做比较
# #     try:
# #         r = (a, b)
# #     except TypeError:
# #         print("字符类型类型错误")
# #     else:
# #         if isinstance(r, float):
# #             r1 = round(r, 2)
# #             assert result == r1
# #         else:
# #             assert result == r
#
#
# # 定义测试除法的参数以及方法
# import pytest
#
#
# @pytest.mark.parametrize('a,b,result',[(1,0,0)])
# def testdiv(self, a, b, result):
#     try:
#         r = self.calcu.div(a, b)
#     except ZeroDivisionError:
#         print("被除数不能为0")
#     except TypeError:
#         print('输入有误，只能输入整数和小数')
#     else:
#         assert result == r



from time import sleep
import pytest
from selenium import webdriver


class TestFrame:

    def setup(self):
        # 定义全局变量，使用webdriver方法获取到Chrome浏览器
        self.driver = webdriver.Chrome()
        # 每次打开窗口，将窗口最大化
        self.driver.maximize_window()
        # 隐式等待，动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_frame(self):
        #
    	self.driver.get("https://ww.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResuLt")
        # self.driver,switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)