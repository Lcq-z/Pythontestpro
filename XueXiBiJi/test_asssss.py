import pytest
import selenium

@pytest.fixture(params=[1,2,3,4],ids="分数")
def lianjieDB():
    print("链接数据库")
    yield
    print("断开数据库")



class TestDemo:


    def test_case1(self,lianjieDB):
        print("测试用例1")

    def test_case2(self,lianjieDB):
        print("测试用例2")

    def test_case3(self,lianjieDB):
        print("测试用例3")