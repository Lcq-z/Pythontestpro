import pytest

# 方法一：
class TestCalc:

    @pytest.mark.run(order=1)
    def test_add(self):
        assert True

    @pytest.mark.run(order=4)
    def test_div(self):
        assert True

    @pytest.mark.run(order=2)
    def test_sub(self):
        assert True

    @pytest.mark.run(order=3)
    def test_mul(self):
        assert True

# 方法二：
class TestCalc1:

    @pytest.mark.first
    def test_add(self):
        assert True

    @pytest.mark.fourth
    def test_div(self):
        assert True

    @pytest.mark.second
    def test_sub(self):
        assert True

    @pytest.mark.third
    def test_mul(self):
        assert True
