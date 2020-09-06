from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from XueXiBiJi.Base_jichu import Base


class TestSc(Base):

    def setup(self):
        # 复用浏览器的代码步骤：
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)

        # 隐式等待，动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(5)
    def test_sc(self):

        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        self.driver.find_element(By.XPATH,"//*[@id='menu_contacts']/span").click()
        self.driver.find_element(By.XPATH,"//*[@id='js_contacts129']/div/div[1]/div/div[1]/a").click()

