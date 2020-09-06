# 从selenium导入webdriver模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 定义一个测试类
class TestHome:
    # 定义setup方法，在执行用例之前，使用self.driver变量获取到Chrome浏览器的驱动，也可以firefox，IE等浏览器
    def setup(self):
        self.driver = webdriver.Chrome()

        # 使用self.driver变量将获取到的浏览器最大化
        self.driver.maximize_window()

        # 隐式等待（全局的）在5秒内，程序的每一个步骤执行完毕之后，动态等待跳转（也就是全部加载完毕）再往下执行因指定时间在5秒内，所以加载
        # 时间超过5秒就会报错，比sleep更加灵活，tips：页面加载过程中隐式等待只能查找到元素，却不能判断查找到的元素是否可点击
        self.driver.implicitly_wait(5)

    # 定义teardown方法，在用例全部执行之后退出测试（关闭浏览器）
    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        # 使用定义好的变量获取测试社区的URL
        self.driver.get("https://ceshiren.com/top/yearly")
        # 定位到括号内的内容（内容代码/字符串可通过selenium IDE获取），注意：如果获取的是中文字符串，就得使用find_element_by_link_text命令，.click():进行点击操作
        self.driver.find_element_by_link_text("最新").click()

        # 定义方法，也就是显示等待的条件，自定义函数必须传入参数，此为语法结构
        def wait(x):
            # return括号内容的长度是否>=1，因使用的是find_elements（查找多个元素），所以可以有多个内容，有多少return多少
            return len(self.driver.find_elements(By.XPATH,
                                                 '//*[@class="active ember-view"]')) >= 1  # >=1 代表代表查找的元素找到>=1，满足后执行下方代码

        # WebDriverWait为语法结构，传入需要等待的时间:4秒，until()传参时注意：wait后面不能有括号，有括号就成调用了，而不是传参
        WebDriverWait(self.driver, 4).until(wait)



        self.driver.find_element_by_link_text("「金羽毛」有奖征文 | 记录测试开发技术进阶之路的点滴").click()
        # 定位到下方括号内的内容（内容代码可通过selenium IDE获取），注意：如果获取的是CSS格式，就得使用find_element_by_css_selector命令
        self.driver.find_element_by_css_selector(".d-icon-d-unliked").click()


