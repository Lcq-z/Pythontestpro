from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


from selenium.webdriver.support.wait import WebDriverWait


class TestwXMicro:
    # 为了演示方便，未使用page object模式
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "测试人社区 ceshiren.comt"
        caps["appPackage"] = "com.tencent.mm"
        caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
        caps["noReset"] = True
        caps['unicodekeyboard'] = True
        caps['resetKeyboard'] = True

        # 指定driver存在的本地路径（在安装appium时，会有一个默认存放driver的路径，如果此路径下的driver版本过老，或者没有的话，就必须得新指定）
        caps ['chromedriverExecutable'] = \
        '/Users/seveniruby/projects/chromedriver/chromedrivers/chromedriver_78.0.3904.11'

        # options=ChromeOptions()
        # options.add_experimental_option('androidProcess','com.tenceat.mm:appbrande')
        caps['chromeOptions'] = {
            'androidProcess':'com.tencent.mm:appbrand0'
        }  # 将微信的小程序进程写到androidProcess内

        caps['adbPort'] = 5038
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 为了加载元素的完整，第一次隐式等待时间加长
        self.driver.implicitly_wait(30)

        self.driver.find_element(By.XPATH, "//*[@text='通讯录‘]")
        # 缩短隐式等待时间
        self.driver.implicitly_wait(10)

    def test_search(self):
        # 原生自动化测试

        size = self.driver.get_window_size()
        self.driver.swipe(size['width'] * 0.5, size['height'] * 0.4, size['width']*0.5,size)
        self.driver.find_element(By.CLASS_NAME, 'android.widget.EditTex').click()
        self.driver.find_element(By.XPATH, "//*[@text='取消‘]")
        self.driver.find_element(By.CLASS_NAME, "android.widget.EditText").send_keys("雪球")
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button')
        self.driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()
        self.driver.find_element(By.XPATH, "//*[@text='自选‘]")

        print(self.driver.contexts)
        # 转换到webview(h5)页面
        self.driver.switch_to.context('WEBVIEW_Xweb')
        self.driver.implicitly_wait(10)
        self.find_top_window()
        # Css定位
        self.driver.find_element(By.CSS_SELECTOR, "[src*=stock_add]").click()
        # 等待新窗口
        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 2)
        self.find_top_window()
        self.driver.find_element(By.CSS_SELECTOR, "._input").click()
        # 输入
        self.driver.switch_to.context("NATIVE_APP")

        # 无法直接在小程序上直接输入内容，这里直接调用原生的方法ActionChains进行输入
        ActionChains(self.driver).send_keys("alibaba").perform()
        # 点击
        self.driver.switch_to.context('WEBVIEW_Xweb')
        self.driver.find_element(By.CSS_SELECTOR, ".stock__item")
        self.driver.find_element(By.CSS_SELECTOR, ".stock__item").click()

    # 找到小程序最新的可视化窗口（因为每一次点击小程序的元素，都会产生一个新的窗口）
    def find_top_window(self, driver=None):
        # 对每一个windows窗口做遍历
        for window in self.driver.window_handles:
            print(window)
            # 判断哪个窗口为可视化的
            if ":VISIBLE" in self.driver.title:
                # 打印出来
                print(self.driver.title)
                return True
            else:
                self.driver.switch_to.window(window)
        return False