import yaml

from Work10.api.base_api import BaseApi
from Work10.api.label import Label

"""
业务流程：创建标签 -> 修改标签名字 —> 删除标签
"""

class TestLabel_anagement(BaseApi):

    # 定义setup方法，每次方法执行前先执行setup内的实例化
    def setup(self):
        # 实例化label并设为全局变量
        self.label = Label()
        # 调用yaml方法打开yaml文件赋值给变量config_secret
        config_secret = yaml.safe_load(open("config.yaml")) # config.yaml文件用于存放企业微信中不同接口的secret
        # 这里调用label中的get_token方法（传入上方yaml文件对应的字段）获取到企业微信的token值
        self.label.get_token(config_secret["token"]["corp_secret"])


    def test_create_label(self):
        # 调用创建标签方法，传入token值与标签id
        self.label.create_label(3)
        list = self.label.get_label_memberlist()
        # 调用封装jsonpath方法，传入对应的参数（json格式参数，jsonpath表达式）后，赋值给name
        name = self.send_jsonpath(list, '$..tagname')
        # 断言字符串"测试"是否在name当中
        assert "测试" in name


    def test_update_label(self):
        # 调用修改标签方法，传入token值与标签id
        self.label.update_label(3)
        list = self.label.get_label_memberlist()
        # 调用封装jsonpath方法，传入对应的参数（json格式参数，jsonpath表达式）后，赋值给name
        name = self.send_jsonpath(list, '$..tagname')
        # 使用jsonpath方法，断言list中所有tagname字段下的第一个值是否等于 "开发"
        assert  "开发" in name


    def test_delete_label(self):
        # 调用删除标签方法，传入token值与标签id
        self.label.delete_label(3)
        list = self.label.get_label_memberlist()
        # 调用封装jsonpath方法，传入对应的参数（json格式参数，jsonpath表达式）后，赋值给label_list
        label_list = self.send_jsonpath(list, '$..taglist')
        # 断言tagid 是否在label_list当中
        assert 3 not in label_list


    # 获取标签列表
    def test_get_label_member_list(self):
        self.label.get_label_memberlist()
