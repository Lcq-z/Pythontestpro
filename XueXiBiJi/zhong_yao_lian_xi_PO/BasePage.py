# 复用浏览器的代码步骤：
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

# 定义类：BasePage，只给其他模块提供一个公共方法的封装
class BasePage:

    # 为第二if的_base_url做条件。在base_url变量前面加上下划线，让其作为本模块私有的变量，不在其他模块中显示
    _base_url = ""
    def __init__(self, driver_base=None):

        # 这里解释一下为什么要使用if，别的模块每次return到其他页面都算一次类的实例化，子类继承父类后每次实例化都会调用BasePage中的init构造方法
        # 如果不加if的话，类实例化时就会一直获取网址，导致用例执行失败，加上if，第一次实例化获取到网址之后，因为其他子
        # 类已经拿到值了，就会执行下面的else，然后使用self driver的值传入用例中
        if driver_base is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)


        else:
            # 加上:WebDriver注解（pycharm比较傻，不加注解的话其他模块中无法联想到self.driver后面的方法）
            self.driver:WebDriver = driver_base

        # 如果按照PO设计模式来看：获取到测试web端的url是跟目前这个BasePage模块无关的
        # 所以设置if条件后，就可以把与BasePage模块无关的都分离出来
        if self._base_url != "":
            self.driver.get(self._base_url)

        self.driver.implicitly_wait(3)
