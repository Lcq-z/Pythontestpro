from Work10.api.wework import Wework


class Label(Wework):
    """
    标签管理
    """

    def create_label(self, tagid):
        """
        创建标签
        """

        # 请求的url
        create_label_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        # 请求信息
        req = {
            # 请求方式
            "method": "post",
            # 请求地址
            "url": create_label_url,
            # 请求参数
            "json": {
                "tagname": "测试",
                "tagid": tagid
            }
        }
        # 因为企业微信所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。接口说明格式如下：
        # 所以在传请求体的时候 尽量使用json参数
        r = self.send_requests(req)
        # return 请求体中的json字段，实现链式调用
        return r.json()

    def update_label(self, tagid):
        """
        修改标签名字
        """

        # 请求的url
        update_label_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        # 请求信息
        req = {
            # 请求方式
            "method": "post",
            # 请求地址
            "url": update_label_url,
            # 请求参数
            "json": {
                "tagname": "开发",
                "tagid": tagid
            }
        }
        # 因为企业微信所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。接口说明格式如下：
        # 所以在传请求体的时候 尽量使用json参数
        r = self.send_requests(req)
        # return 请求体中的json字段，实现链式调用
        return r.json()

    def delete_label(self, tagid):
        """
        删除标签
        """

        # 请求的url
        delete_label_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tagid}"
        # 请求信息
        req = {
            # 请求方式
            "method": "get",
            # 请求地址
            "url": delete_label_url
        }
        r = self.send_requests(req)
        # return 请求体中的json字段，实现链式调用
        return r.json()

    def get_label_memberlist(self):
        """
        获取标签列表
        """

        # 请求的url
        get_label_memberlist_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        # 请求信息
        req = {
            # 请求方式
            "method": "get",
            # 请求地址
            "url": get_label_memberlist_url,
        }
        r = self.send_requests(req)
        print(r.json())
        # return 请求体中的json字段，实现链式调用
        return r.json()
