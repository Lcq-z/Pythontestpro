# 导入需要使用的库
from typing import List

import pytest
import yaml
from Python_testing.Work2.Calc_2 import Calculator


# 使用fixture，对类实例化，调用Calculator类
@pytest.fixture(scope='class')
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")


# 打开yCalculator.yaml文件，对测试用例参数化，因yaml文件中有中文字符串，所以设置中文编码UTF-8
with open("Calculator_2.yaml", encoding='UTF-8') as f:
    # 将打开的yaml文件内容赋值给变量datas
    datas = yaml.safe_load(f)

    # 获取测试用例加法的参数
    add_datas = datas['add']['add_datas']
    print(add_datas)
    # 获取测试用例加法的id
    add_ids = datas['add']['add_ids']
    print(add_ids)

    # 获取测试用例减法的参数
    sub_datas = datas['sub']['sub_datas']
    print(sub_datas)
    # 获取测试用例减法的id
    sub_ids = datas['sub']['sub_ids']
    print(sub_ids)

    # 获取测试用例乘法的参数
    mul_datas = datas['mul']['mul_datas']
    print(mul_datas)
    # 获取测试用例乘法的id
    mul_ids = datas['mul']['mul_ids']
    print(mul_ids)

    # 获取测试用例除法的参数
    div_datas = datas['div']['div_datas']
    print(div_datas)
    # 获取测试用例除法的id
    div_ids = datas['div']['div_ids']
    print(div_ids)


# 参数传递
@pytest.fixture(params=add_datas, ids=add_ids)
def get_adddatas(request):
    adddatas = request.param
    print(f"加法的测试数据：{adddatas}")
    return adddatas


@pytest.fixture(params=sub_datas, ids=sub_ids)
def get_subdatas(request):
    subdatas = request.param
    print(f"减法的测试数据：{subdatas}")
    return subdatas


@pytest.fixture(params=mul_datas, ids=mul_ids)
def get_muldatas(request):
    muldatas = request.param
    print(f"乘法的测试数据：{muldatas}")
    return muldatas


@pytest.fixture(params=div_datas, ids=div_ids)
def get_divdatas(request):
    divdatas = request.param
    print(f"除法的测试数据：{divdatas}")
    return divdatas


# 钩子函数，也就是hook函数
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.
    :param _pytest.main.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[_pytest.nodes.Item] items: List of item objects.
    """
    print("items")
    print(items)
    # 更改测试用例的编码为UTF-8，使用例结果的id可显示为中文
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
