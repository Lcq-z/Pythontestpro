import pytest

# 创建一个登录的fixture方法，yield 关键字激活了 fixture 的 teardown方法
@pytest.fixture()
def login():
    print("需要登录")
    print("登陆验证")
    username = "lili"
    password = "112233"
    # yield关键字，激活了 fixture 的 teardown方法
    yield [username,password]
    print("登出操作")

# 需要提前登录
# 在执行测试用例之前先执行传入的fixture方法
def test_case1(login):
    print(f"username and password: {login}")
    print("测试用例1")

# 不需要提前登录
def test_case2():
    print("测试用例1")

# 需要提前登录
def test_case3(login):
    print("测试用例1")


if __name__ == '__main__':
    pytest.main(['-v','test_fixturess.py'])




