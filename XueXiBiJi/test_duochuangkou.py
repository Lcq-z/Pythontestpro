from time import sleep
import pytest
from selenium import webdriver


class TestDuoChuangKou:

    def setup(self):
        # 定义全局变量，使用webdriver方法获取到Chrome浏览器
        self.driver = webdriver.Chrome()
        # 每次打开窗口，将窗口最大化
        self.driver.maximize_window()
        # 隐式等待，动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_duochuangkou(self):
        # 访问百度网址URL
        self.driver.get("https://www.baidu.com/")
        # 通过文本定位，定位到 '登录' 并点击
        self.driver.find_element_by_link_text("登录").click()
        sleep(1)
        # 通过文本定位，定位到 '立即注册' 并点击
        self.driver.find_element_by_link_text("立即注册").click()
        # 获取到当前的窗口句柄id并打印
        print(self.driver.current_window_handle)
        # 获取到所有打开的窗口的 句柄id后，赋值给 'window' 变量
        window = self.driver.window_handles

        # 强制等待3秒，便于观看
        sleep(3)

        # 切换至浏览器上最后一个窗口，因为下方要点击的内容在最后一个窗口，所以才切换（注意：如果不切换窗口，直接在定位后操作，100%报错）
        self.driver.switch_to_window(window[-1])
        sleep(2)

        # 定位到id元素后输入username
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("122287318")
        self.driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys("1111111111")
        sleep(3)

        # 切换至浏览器上第一的窗口，因为下方要点击的内容在第一个窗口，所以才切换（注意：如果不切换窗口，直接在定位后操作，100%报错）
        self.driver.switch_to_window(window[0])

        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        sleep(3)
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("qwerttyyyuy")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("122287318")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_duochuangkou.py'])
