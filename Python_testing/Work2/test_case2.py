# 定义测试计算器的类
class TestCalc:

    # 在每条测试用例前执行
    def setup(self):
        print("开始执行测试用例")

    # 在每条测试用例后执行
    def teardown(self):
        print("测试用例执行完毕")

    # 对定义的test_add方法进行参数化
    def test_add(self,get_calc,get_adddatas):
        # 调用计算器的add方法
        result = get_calc.add(get_adddatas[0],get_adddatas[1])

        # 判断result为小数的时,使用round函数进行四舍五入并保留小数点后两位
        if isinstance(result, float):
            result = round(result, 2)

        # 断言
        assert get_adddatas[2] == result


    # 对定义的test_sub方法进行参数化
    def test_sub(self,get_calc,get_subdatas):
        # 调用计算器的sub方法
        result = get_calc.sub(get_subdatas[0],get_subdatas[1])

        # 判断result为小数的时,使用round函数进行四舍五入并保留小数点后两位
        if isinstance(result, float):
            result = round(result, 2)

        # 断言
        assert get_subdatas[2] == result


    # 对定义的test_mul方法进行参数化
    def test_mul(self,get_calc,get_muldatas):
        # 调用计算器的mul方法
        result = get_calc.mul(get_muldatas[0],get_muldatas[1])

        # 判断result为小数的时,使用round函数进行四舍五入并保留小数点后两位
        if isinstance(result, float):
            result = round(result, 2)

        # 断言
        assert get_muldatas[2] == result


    # 对定义的test_div方法进行参数化
    def test_div(self,get_calc,get_divdatas):
            # 调用计算器的div方法
            result = get_calc.div(get_divdatas[0], get_divdatas[1])

            # 判断result为小数的时,使用round函数进行四舍五入并保留小数点后两位
            if isinstance(result, float):
                result = round(result, 2)
            # 断言:
            assert result == get_divdatas[2]


    # 判断加法数值类型为字符串时，抛出异常信息
    def test_add_str(self,get_adddatas):
        if isinstance(get_adddatas[0], str) or isinstance(get_adddatas[1], str):
            raise ValueError("计算器的值不能使用字符串，或为空")

    # 判断减法数值类型为字符串时，抛出异常信息
    def test_sub_str(self,get_subdatas):
        if isinstance(get_subdatas[0], str) or isinstance(get_subdatas[1], str):
            raise ValueError("计算器的值不能使用字符串，或为空")

    # 判断乘法数值类型为字符串时，抛出异常信息
    def test_mul_str(self,get_muldatas):
        if isinstance(get_muldatas[0], str) or isinstance(get_muldatas[1], str):
            raise ValueError("计算器的值不能使用字符串，或为空")

    # 判断除法数值类型为字符串时，抛出异常信息
    def test_div_str(self,get_divdatas):
        if isinstance(get_divdatas[0], str) or isinstance(get_divdatas[1], str):
            raise ValueError("计算器的值不能使用字符串，或为空")

    # 判断被除数的类型为0时，抛出异常信息
    def test_divisor0(self,get_divdatas):
        if get_divdatas[1] == 0:
                raise ValueError("被除数不能为0")


