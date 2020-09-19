import requests


class Wework:
    def get_token(self):
        """
        获取token
        """
        # 定义获取token的关键参数：企业ID，通讯录凭证密钥
        corpid = "wwe760e5b2c1333a36"
        corpsecret = "EE78xI4xl3UjxA6VYzoYD5x8d6_--NBgxo35J3pGBEQ"
        # 在url中传入上方定义的关键参数，才可以获取到token
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 请求参数
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        # 发送get请求并追加参数
        r = requests.get(url=url, params=params)
        # 将请求中josn字段下的access_token字段赋值给全局变量token
        self.token = r.json()["access_token"]
        # return token，实现链式调用
        return self.token
