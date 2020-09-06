# # 导入pytest
# import pytest
# import yaml
# # 创建一个pytest命名规则的类
# class TestData:
#     # 参数化：使用yaml.safe_load命令，(open("./YML_data.yaml"))打开目录下的./YML_data.yaml
#     @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./YML_data.yaml")))   # 严格按照格式书写代码
#     def test_data(self,a,b):
#         print(a + b)
#
#     # 参数化：
#     @pytest.mark.parametrize(["a","b"],[(10,20),(10,23)])
#     def test_data1(self,a,b):
#         print(a + b)
#     # 参数化：
#     @pytest.mark.parametrize(("a","b"),[(10,20),(10,23)])
#     def test_data2(self,a,b):
#         print(a + b)
#
#
import os

import pytest
from selenium import webdriver

from Python_testing.Work1.Calc import Calculator


class TestCalc:

    @pytest.mark.parametrize('a,b,expect'[
        (1,1,2)
    ])
    def test_add(self,a,b,expect):
        calc = Calculator()
        result = calc.test_add1(a,b)
        # 判断result为小数的时,使用round函数保留小数点后两位
        if isinstance(result, float):
            result = round(result, 2)
            # 断言
        assert expect == result










#
#
# import pytest
#
# def func(x):
#     return x + 1

@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,20),
    ('a','a1'),
    (3,4),
    (5,6)
])
def test_xx(a,b):
    assert func(a) == b
#
# def test_xy():
#     assert func(3)==4




if __name__ == '__main__':
    pytest.main(['test_a.py'])


