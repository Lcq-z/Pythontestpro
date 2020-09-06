from time import sleep

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestLiulan:
    def setup(self):
        # 复用浏览器的代码步骤：
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        # 隐式等待，动态的等待元素，最好在实例化driver之后立刻去设置
        self.driver.implicitly_wait(5)
        # 窗口最大化
        self.driver.maximize_window()

    def teradown(self):
        self.driver.quit()

    def test_cookie(self):
        # get_cookies() 获取当前页面的cookies，因为已经获取到cookie并且复制下来了，所以可以直接注释掉
        # cookies = self.driver.get_cookies()
        # print(cookies)

        # 打开index页面，这时候需要登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 带有登录信息的cookie
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688853202183050'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'k4gcDaDDZPlZlnTbitl7CFN2snzk-9bbjdcFgyZJJ5jB9ELobaBNCLV3sCrWHg47hBJiIzSDl9E-C5QfNF1MLQoV-g_v6d6HNUdHNlaKizJfgXmOQv0cWsH72qbv70-mTzzd7iA2s_UYpIcmEcoCFdlfWZvgfuMcuYFWAsCQehbMPQ50sexGl77Ct9st4ZjzjnBkSGG2McVk2mNy-ZuqzKiovMzwB6IV9wtB8uYYKPl5ZPiozdbzsARAxfKZ1s4OnjMjt6bqcXpav_a3kXoR7g'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688853202183050'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325115155144'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'uJp5O2bOOOov_hXF3y6ISpd8Jfltmnk6xoZGiEb2cNxi9AW5Qoz7f6kEUSu3_iUQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a746668'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1597905904'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '20137808562702791'},
            {'domain': '.qq.com', 'expiry': 1660977918, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1317438837.1597235591'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1628771589, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.qq.com', 'expiry': 1627983194, 'httpOnly': False, 'name': 'LW_uid', 'path': '/',
             'secure': False, 'value': 'c1P5N956c4G4X7S1f9b406E1N4'},
            {'domain': '.qq.com', 'expiry': 1628071898, 'httpOnly': False, 'name': 'LW_sid', 'path': '/',
             'secure': False, 'value': 'Q195c9D6H5S3f598o948y95785'},
            {'domain': '.qq.com', 'expiry': 1627983195, 'httpOnly': False, 'name': 'eas_sid', 'path': '/',
             'secure': False, 'value': '91y559W6h4h4Q7m1C9S5r9O8z1'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '8cb785427dabea1c151d2769191e22d33c4c9f3f5dc05b59527a2f71f4b0564d'},
            {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'PcLdAwDS4H'},
            {'domain': '.qq.com', 'expiry': 1597992318, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.739478373.1597893395'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1597924930, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '65e20m9'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '3281075200'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600497920, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629441903, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1597893395,1597905272,1597905464,1597905904'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '8736951020'}]

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        # 重新打开已带有cookie信息的index页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_weixin_login.py'])
