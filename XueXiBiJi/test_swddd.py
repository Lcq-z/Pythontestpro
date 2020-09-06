import pytest


@pytest.fixture(params=[1,2,3],ids=['结果1','结果2','结果3'])
def login1(request):
   data = request.param
   print(request.param)
   print("获取测试数据")
   return data + 1


def test_case1(login1):
    print(login1)
    print("xxx")

def test_case2():
    print("xxx")

