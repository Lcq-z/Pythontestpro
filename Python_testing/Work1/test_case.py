# 导入需要使用的库
import pytest
import yaml
from Python_testing.Work1.Calc import Calculator

# 打开yCalculator.yaml文件，对测试用例参数化，因yaml文件中有中文字符串，所以设置中文编码UTF-8
with open("Calculator.yaml", encoding='UTF-8') as f:
    # 将打开的yaml文件内容赋值给变量datas
    datas = yaml.safe_load(f)

    # 获取测试用例加法的参数
    add_datas = datas['add']['add_datas']
    print(add_datas)

    # 获取测试用例加法的id
    add_ids = datas['add']['add_ids']
    print(add_ids)

    # 获取测试用例除法的参数
    div_datas = datas['div']['div_datas']
    print(div_datas)

    # 获取测试用例除法的id
    div_ids = datas['div']['div_ids']
    print(div_ids)


# 定义测试计算器的类
class TestCalc:

    # 定义setup_class方法，在类中,运行代码之前，执行打印开始计算，对类实例化，调用Calculator类
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 定义teardown_class方法，在类中,运行代码结尾，打印结束计算
    def teardown_class(self):
        print("计算结束")

    # 在每条测试用例前执行
    def setup(self):
        print("开始执行测试用例")

    # 在每条测试用例后执行
    def teardown(self):
        print("测试用例执行完毕")

    # 对定义的test_add方法进行参数化
    @pytest.mark.parametrize('a,b,expect', add_datas, ids=add_ids)
    def test_add(self, a, b, expect):
        # 调用计算器的add方法
        result = self.calc.add(a, b)
        # 判断result为小数的时,使用round函数进行四舍五入并保留小数点后两位
        if isinstance(result, float):
            result = round(result, 2)
        # 判断a或b的类型为字符串时，抛出异常信息
        elif isinstance(a, str) or isinstance(b, str):
            raise ValueError("计算器的值不能使用字符串，或为空")
        # 断言
        assert expect == result

    # 对定义的test_div方法进行参数化
    @pytest.mark.parametrize('a,b,expect', div_datas, ids=div_ids)
    def test_div(self, a, b, expect):

        try:
            # 调用计算器的div方法
            result = self.calc.div(a, b)
            # 判断result为小数的时,使用round函数进行四舍五入并保留小数点后两位
            if isinstance(result, float):
                result = round(result, 2)
        except:
            # 判断a或b的类型为字符串时，抛出异常信息
            if isinstance(a, str) or isinstance(b, str):
                raise ValueError("计算器的值不能使用字符串，或为空")
            # 判断b的类型为0时，抛出异常信息
            elif b == 0:
                raise ValueError("被除数不能为0")
        else:
            # 断言:
            assert result == expect
