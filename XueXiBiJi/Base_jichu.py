from selenium import webdriver


class Base:
    def setup(self):
        # 定义全局变量，使用webdriver方法获取到Chrome浏览器
        self.driver = webdriver.Chrome()
        # 每次打开窗口，将窗口最大化
        self.driver.maximize_window()
        # 隐式等待，动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()