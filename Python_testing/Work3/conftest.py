from typing import List
import pytest


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
    # 更改测试用例的编码为UTF-8，使测试用例可显示为中文
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# parser：用户命令行参数与ini文件值的解析器
def pytest_addoption(parser):
    # 定义分组hogwarts
    mygroup = parser.getgroup("hogwarts")  # group将下面所有的option都展示在这个group下
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 没有传递参数就使用默认值，传递参数会取代默认值
                      dest='env',  # 存储的变量
                      help='env测试环境'  # 参数说明
                      )
    mygroup.addoption("--dev",  # 注册一个命令行选项
                      default='dev',  # 没有传递参数就使用默认值，传递参数会取代默认值
                      dest='dev',  # 存储的变量
                      help='dev测试环境'  # 参数说明
                      )
    mygroup.addoption("--st",  # 注册一个命令行选项
                      default='st',  # 没有传递参数就使用默认值，传递参数会取代默认值
                      dest='st',  # 存储的变量
                      help='st测试环境'  # 参数说明
                      )


# 获取参数
@pytest.fixture(scope='session')
def cmdoption(request):
    return request.config.getoption("--env", default='test')


@pytest.fixture(scope='session')
def cmdoption1(request):
    return request.config.getoption("--dev", default='dev')


@pytest.fixture(scope='session')
def cmdoption2(request):
    return request.config.getoption("--st", default='st')
