# 导入需要使用的包
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains():

    # 定义setup方法，在每个方法执行之前执行
    def setup(self):
        # 定义全局变量，使用webdriver方法获取到Chrome浏览器
        self.driver = webdriver.Chrome()
        # 设定全局隐式等待,5秒内轮询查找
        self.driver.implicitly_wait(5)
        # 每次打开窗口，将窗口最大化
        self.driver.maximize_window()

    # 定义teardown方法，在方法执行后执行
    def teardown(self):
        # 执行完毕后退出
        self.driver.quit()

    # pytest解释器：在方法上面添加后，跳过此方法，不运行
    @pytest.mark.skip
    # 定义一个方法，在获取到的网页中模拟鼠标的单击、右击、双击操作
    def test_case_click(self):
        # 使用全局变量获取到测试的网址URL
        self.driver.get("http://sahitest.com/demo/clicks.htm")

        # 使用Xpath方法定位到对应网址需要点击的内容，赋值给变量elemenet_click
        elemenet_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")

        # 使用Xpath方法定位到对应网址需要点击的内容，赋值给变量elemenet_double_click
        elemenet_double_click = self.driver.find_element_by_xpath("/html/body/form/input[2]") # 定位内容方式与下方不同，但都是一个意思

        # 使用Xpath方法定位到对应网址需要点击的内容，赋值给变量elemenet_right_click
        elemenet_right_click = self.driver.find_element_by_xpath("//input[@value='right click me']")

        # 调用动作链接ActionChains方法，传入self.driver变量，赋值给action变量
        action = ActionChains(self.driver)
        # 使用action变量调用 鼠标左键点击方法，传入要点击的内容：elemenet_click
        action.click(elemenet_click)
        # 使用action变量调用 鼠标右键点击方法，传入要点击的内容：elemenet_right_click
        action.context_click(elemenet_right_click)
        # 使用action变量调用鼠标双击方法，传入要点击的内容：elemenet_double_click
        action.double_click(elemenet_double_click)
        sleep(2)
        # 动作链接ActionChains语法结构，必须调用perform()方法之后，队列中的事件会依次执行
        action.perform()
        sleep(2)

    # pytest解释器：在方法上面添加后，跳过此方法，不运行
    @pytest.mark.skip
    # 定义方法，在获取到的网页中模拟鼠标悬浮在定位的地方
    def test_moveto(self):
        # 使用全局变量获取到测试百度的网址URL
        self.driver.get("https://www.baidu.com/")
        # 使用CSS_SELECTOR方法定位到对应网址需要悬浮的位置，赋值给变量ele
        ele = self.driver.find_element(By.CSS_SELECTOR,"#s-usersetting-top")
        # 调用动作链接ActionChains方法，传入self.driver变量，赋值给action变量
        action = ActionChains(self.driver)
        # 使用action变量调用鼠标悬浮方法，传入要点击的内容：ele
        action.move_to_element(ele)
        # 动作链接ActionChains语法结构，必须调用perform()方法之后，队列中的事件会依次执行
        action.perform()
        sleep(3)

    @pytest.mark.skip
    # 定义方法，在获取到的网页中，模拟将一个元素挪动到其他位置
    def test_draqdrop(self):
        # 使用全局变量获取到测试的网址URL
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        # 使用CSS_SELECTOR方法定位到对应网址中要挪动的元素，赋值给变量nuodong
        nuodong = self.driver.find_element_by_css_selector('#dragger')
        # 使用CSS_SELECTOR方法定位到对应元素要挪到的位置，赋值给变量nuodongweizhi
        nuodongweizhi = self.driver.find_element_by_css_selector('body > div:nth-child(4)')
        # 调用动作链接ActionChains方法，传入self.driver变量，赋值给action变量
        action = ActionChains(self.driver)

        # 此时有三种方法可以实现挪动元素到指定位置后调用perform方法（不论使用哪一种都可以，自我理解：先使用简单的，由简入繁）：
        # 第一种：
        action.drag_and_drop(nuodong,nuodongweizhi).perform()
        # 第二种：
        # action.click_and_hold(nuodong).release(nuodongweizhi).perform()
        # 第三种：
        # action.click_and_hold(nuodong).move_to_element(nuodongweizhi).release().perform()

    # 定义方法，在获取到的网页中，定位到输入框，模拟点击、输入内容、键盘空格、删除
    def test_keys1(self):
        # 使用全局变量获取到测试的网址URL
        self.driver.get("http://sahitest.com/demo/label.htm")
        # 使用Xpath方法定位到对应网址中的输入框，赋值给变量ele
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        # 调用click方法：点击输入框
        ele.click()
        # 调用动作链接ActionChains方法，传入self.driver变量，赋值给action变量
        action = ActionChains(self.driver)
        # 调用send_keys方法，在输入框中输入username后，等待1秒：pause(1)
        action.send_keys("username").pause(1)
        # 调用send_keys方法，在输入框中输入空格后，等待1秒：pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        # 调用send_keys方法，在输入框中输入tom后，等待1秒：pause(1)
        action.send_keys("tom").pause(1)
        # 调用send_keys方法，在输入框中删除一个字母，在调用perform方法
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)


# 调用pytest方法，使用python解释器运行上方代码，也可通过命令行运行
if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_acition_chains.py'])

