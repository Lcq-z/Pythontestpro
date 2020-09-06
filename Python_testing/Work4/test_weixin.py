import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeixin:

    def setup(self):
        # 复用浏览器的代码步骤：
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()

        # 隐式等待，动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(5)

    def teradown(self):
        self.driver.quit()

    def test_wx(self):
        # sleep(2)
        # 通过复用浏览器获取已登录企业微信的cookie再赋值给cookies
        # cookies = self.driver.get_cookies()
        # print(cookies)

        # 打开企业微信主页面，这时候需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        # shelve python内置的模块，相当于小型的数据库
        db = shelve.open('./mydbs/cookies')
        # 将带有登录信息的cookies存入mydbs目录cookies下
        # db['cookie'] = cookies
        # db.close()
        # 将带有登录信息的cookie赋值给cookies
        cookies = db['cookie']

        # 遍历一下cookie，可以把cookie看成 cookies列表 的内容（好理解一些）
        for cookie in cookies:
            # 在遍历cookie之后，添加一层判断，如果expiry在cookie中，就删除它（expiry不重要，可删除）
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            # 因为添加cookie的语法：add_cookie(要求必须是字典)，所以遍历后再添加
            self.driver.add_cookie(cookie)

        # 再次打开企业微信主页面，因为已经获取到带有登录信息的cookie了，此时不需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]/div/span[2]').click()
        sleep(2)
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys(r'‪C:\Users\XiaoRongYiJiu\ass.xlsx')
        sleep(2)
        assert 'demo.xlsx' == self.driver.find_element_by_id('upload_file_name').text
        sleep(4)
