import shelve
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

    def teradown(self):
        self.driver.quit()

    # def test_cookie(self):
        # get_cookie 获取当前页面的一个cookie
        # cookies = self.driver.get_cookies()
        # print(cookies)

    # shelve python 内置模块，相当于小型的数据库
    def test_shelve(self):
        # # 打开微信页面需要登录
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")


        # # 带有登录信息的cookies
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850212828538'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325011154881'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850212828538'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'pVaD3QIj7bj62y_yUwh83xqpProRS6_YGzB6GZC7BfYNFL235F1K-Y6lUJtIZy6D'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a1264880'}, {'domain': 'work.weixin.qq.com', 'expiry': 1597937949, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '6bavaq'}, {'domain': '.qq.com', 'expiry': 1597993111, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.2062240196.1597906415'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '1374566037'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629442628, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597300476,1597471399,1597906414'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1660978711, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.223888743.1597300477'}, {'domain': '.work.weixin.qq.com', 'expiry': 1628836475, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'S0zPQnhQV7M1M6wd9lAWh8nc3hSlFg-Vw-HXuE_IrfvF_pqNhoaTKG9ELRf7PMkGdK7t_jrmfJ4yhKpyC-wDFzgZV0Gdr_ORHuiAH4Y4x8_4h9b78yXUn2QuOLEvMnKKJJw41CGrxVzBGWG-2Svmwfg4z1L7uDMzXbHi68OQP3CB6LEV2xXsRq-9SzriK3YFiZJLd7-tBmnvtdKa_jXtbYdgD-Nxlo8oJA1yVCYdC9Cdprbb_4S1i4-5VsGAmhx4xRbfz6eRwZstaZcX0AR0Vg'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600498714, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1597906629'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '16763835273217610'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '7501569024'}]

        #带有登录信息的cookies
        db = shelve.open('./mydbs/cookies')
        # db['cookie'] = cookies
        # db.close()
        cookies = db['cookie']
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")


        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)

        # 重新打开  已带有cookie 信息 的微信界面
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(1)

        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[2]').click()
        self.driver.find_element_by_id("js_upload_file_input").send_keys(r"‪C:\Users\XiaoRongYiJiu\Desktop\Microsoft Excel 工作表.xlsx")
        assert "cxl.xlsx" == self.driver.find_element_by_id("upload_file_name").text
        sleep(5)

if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_delete_member_po.py'])