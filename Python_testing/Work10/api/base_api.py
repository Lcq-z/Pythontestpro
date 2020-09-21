import requests
from jsonpath import jsonpath


class BaseApi:

    # 封装requests方法，实现代码更高的可维护性（如果不封装，基本上外面的所有界面都需要导入request方法，封装后调用即可）
    def send_requests(self,req:dict):
        """
        对requests进行二次封装
        :req: 字典格式，调用此方法时，需关键字传参
        :return:requests中的request方法，因req为字典格式，所以在req前面加两个*来解包字典（不解包，无法使用关键字传参）
        """
        return requests.request(**req)

    # 封装jsonpath方法，调用时需传入json格式参数，jsonpath表达式
    def send_jsonpath(self,element,expression):
        return jsonpath(element, expression)