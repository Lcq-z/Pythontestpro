from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction:

    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_huadong(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element_by_css_selector('#kw')
        ele_search = self.driver.find_element_by_css_selector('#su')

        ele.send_keys("霍格沃兹测试学院")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()

        action.scroll_from_element(ele, 0, 10000).perform()
        sleep(2)


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_touch_acition.py'])
