from Work10.api.base_api import BaseApi


class Wework(BaseApi):

    def get_token(self,corpsecret):
        """
        获取token
        """

        # 定义获取token的关键参数：企业ID，通讯录凭证密钥
        corpid = "wwe760e5b2c1333a36"
        # corpsecret = "EE78xI4xl3UjxA6VYzoYD5x8d6_--NBgxo35J3pGBEQ"

        # get_token的请求信息
        req = {
            # 请求方式
            "method": "get",
            # 请求地址
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            # 请求参数
            "params": {"corpid": corpid, "corpsecret": corpsecret}
        }

        # 调用封装的requests.ruquest方法发送get请求
        r = self.send_requests(req)
        # 将请求中josn字段下的access_token字段赋值给全局变量token
        self.token = r.json()["access_token"]
        # return token，实现链式调用
        return self.token
