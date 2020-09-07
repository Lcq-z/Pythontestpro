from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
BasePage 基类
最基本的方法，初始化driver,  find , finds , 显式等待 , 滑动点击.....
"""

class BasePage:


    # 定义init方法，其他类继承时，每次都执行
    # # 加上 ":WebDriver" 注解（pycharm比较傻，不加注解的话，其他模块中无法联想到self.driver后面的方法）
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 定义find方法，对find_element方法进行封装，调用时需传入：定位到的元素，*用于解元组
    def find(self, element):
        return self.driver.find_element(*element)

    # 定义finds方法，对find_elements方法进行封装，调用时需传入：定位到的元素，*用于解元组
    def finds(self, element):
        return self.driver.find_elements(*element)

    # 定义find_and_click方法，对find_element和click同时进行封装，调用时需传入：定位到的元素，没有加*，是因为上方的find已经解过了
    def find_and_click(self, element):
        self.find(element).click()

    # 定义find_and_sendkys方法，对find_element和send_keys同时进行封装，调用时需传入：定位到的元素和需要输入的元素
    def find_and_sendkys(self, element, name):
        self.find(element).send_keys(name)

    # 定义find_swipe_click方法，用于滑动查找，先将滑动屏幕过程赋值给变量ele，再调
    # 用上方已封装的find_and_click方法，传入ele，调用此方法时只需传入：text
    def find_swipe_click(self, text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
               'new UiScrollable(new UiSelector()'
               '.scrollable(true).instance(0))'
               '.scrollIntoView(new UiSelector()'
               f'.text("{text}").instance(0));')
        return self.find_and_click(ele)

    # 定义show_wait方法，对显示等待（当传入的元素可被点击时，再执行其他操作）进行封装，调用时需传入：定位到的元素即可
    def show_wait(self, element):
        return WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(element))
