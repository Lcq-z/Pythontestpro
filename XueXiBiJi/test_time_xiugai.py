from time import sleep
import pytest
from selenium import webdriver
from XueXiBiJi.Base_jichu import Base


class TestJavaScript(Base):

    def test_timexg(self):
        # 访问12306首页
        self.driver.get("https://www.12306.cn/index/")
        sleep(2)
        # 调用selenium的execute_script方法，运行js代码
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        sleep(2)
        self.driver.execute_script("a.value='2020-10-25'")
        sleep(2)

        print(self.driver.execute_script("return document.getElementById('train_date').value"))


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_time_xiugai.py'])
