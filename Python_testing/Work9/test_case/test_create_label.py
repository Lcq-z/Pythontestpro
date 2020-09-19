from Python_testing.Work9.api.label import Label
from Python_testing.Work9.api.wework import Wework
from jsonpath import jsonpath

"""
业务流程：创建标签 -> 修改标签名字 —> 删除标签
"""


class TestLabel_anagement:
    # 定义setup方法，每次方法执行前先执行setup内的实例化
    def setup(self):
        wework = Wework()
        self.label = Label()
        self.token = wework.get_token()


    def test_create_label(self):
        # 调用创建标签方法，传入token值与标签id
        self.label.create_label(self.token, 3)
        list = self.label.get_label_memberlist(self.token)

        # 使用jsonpath方法，断言list中所有tagname字段下的第一个值是否等于 "测试"
        assert jsonpath(list, '$..tagname')[0] == "测试"


    def test_update_label(self):
        # 调用修改标签方法，传入token值与标签id
        self.label.update_label(self.token, 3)
        list = self.label.get_label_memberlist(self.token)

        # 使用jsonpath方法，断言list中所有tagname字段下的第一个值是否等于 "开发"
        assert jsonpath(list, '$..tagname')[0] == "开发"


    def test_delete_label(self):
        # 调用删除标签方法，传入token值与标签id
        self.label.delete_label(self.token, 3)
        list = self.label.get_label_memberlist(self.token)

        # 断言删除标签列表后，获取到的标签列表长度是否等于0（此断言需要优化）
        assert len(list["taglist"]) == 0


    # 获取标签列表
    def test_get_label_member_list(self):
        self.label.get_label_memberlist(self.token)
