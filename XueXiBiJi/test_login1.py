from time import sleep
from selenium import webdriver
"""
测试用例步骤：
1.打开testerhome登录地址
http://testerhome.com/account/sign_in
2.输入用户名
3.输入密码
4.点击’记住’标签
5.点击登录，提交表单"""

class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()



    def test_from(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        sleep(1)
        self.driver.find_element_by_css_selector('#user_login').send_keys("12345")
        self.driver.find_element_by_id("user_password").send_keys("passswd")
        self.driver.find_element_by_id("user_remember_me").click()
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()
        sleep(5)