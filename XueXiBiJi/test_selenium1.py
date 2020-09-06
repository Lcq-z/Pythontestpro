import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestLiulan:
    def setup(self):
        # 复用浏览器的代码步骤：
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        # self.driver = webdriver.Chrome()
        # 隐式等待，动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(5)

    def teradown(self):
        self.driver.quit()

    def testcase(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.set_window_size(1536, 960)
        self.driver.find_element(By.LINK_TEXT, "所有分类").click()
        categoryele = self.driver.find_element(By.LINK_TEXT, "所有分类")
        assert 'active' == categoryele.get_attribute("class")
















    # def testwait(self):
    #     # self.driver.get("https://www.baidu.com/")
    #     # 通过获取到Chrome浏览器的变量，使用CSS_SELECTOR定位到id=kw的搜索框并在输入框中输入：霍格沃兹测试学院
    #     # self.driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("霍格沃兹测试学院")
    #
    #     # 与上面表达方式不一样，但是意思一样，结果一样
    #     # self.driver.find_element(By.ID,'kw').send_keys("霍格沃兹测试学院")
    #
    #     # 使用Pycharm自带的定位方式定位到id=su的搜索按钮并点击
    #     self.driver.find_element(By.ID, 'su').click()