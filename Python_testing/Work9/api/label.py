import requests


class Label:
    """
    标签管理
    """
    def create_label(self, access_token, tagid):
        """
        创建标签
        """
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={access_token}"
        data = {
            "tagname": "测试",
            "tagid": tagid
        }
        # 因为企业微信所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。接口说明格式如下：
        # 所以在传请求体的时候 尽量使用json参数
        r = requests.post(url=create_url, json=data)
        # return 请求体中的json字段，实现链式调用
        return r.json()

    def update_label(self, access_token, tagid):
        """
        修改标签名字
        """
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={access_token}"
        data = {
            "tagname": "开发",
            "tagid": tagid
        }
        # 因为企业微信所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。接口说明格式如下：
        # 所以在传请求体的时候 尽量使用json参数
        r = requests.post(url=update_url, json=data)
        # return 请求体中的json字段，实现链式调用
        return r.json()

    def delete_label(self, access_token, tagid):
        """
        删除标签
        """
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={access_token}&tagid={tagid}"
        r = requests.get(url=delete_url)
        # return 请求体中的json字段，实现链式调用
        return r.json()

    def get_label_memberlist(self, access_token):
        """
        获取标签列表
        """
        label_memberlist_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={access_token}"
        r = requests.get(url=label_memberlist_url)
        print(r.json())
        # return 请求体中的json字段，实现链式调用
        return r.json()
