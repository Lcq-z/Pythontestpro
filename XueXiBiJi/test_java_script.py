from time import sleep

from selenium import webdriver


class TestJavaScript:

    def setup(self):
        # 定义全局变量，使用webdriver方法获取到Chrome浏览器
        self.driver = webdriver.Chrome()
        # 每次打开窗口，将窗口最大化
        self.driver.maximize_window()
        # 隐式等待，动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def testjs(self):
        self.driver.get("https://www.baidu.com/")
        # 定位到百度输入框后，输入selenium 测试
        self.driver.find_element_by_id("kw").send_keys("selenium 测试")
        # 调用Selenium的execute_script方法来执行js代码后return，赋值给element变量（赋值时必须return，不然报错）
        element = self.driver.execute_script('return document.getElementById("su")')  # js代码：定位到id为su的
        # 调用点击方法
        element.click()
        sleep(2)
        # 调用Selenium的execute_script方法来执行js代码
        self.driver.execute_script("document.documentElement.scrollTop=10000")  # 页面滑动，数值越大，往下滑的位置越多
        sleep(3)
        # 使用Xpath定位到元素后点击
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(2)
