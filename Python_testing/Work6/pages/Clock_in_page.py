from appium.webdriver.common.mobileby import MobileBy
from Python_testing.Work6.pages.BasePage6 import BasePage6


class ClochIn_Page(BasePage6):
    # 定义只在此类中使用的私有变量
    _waichu_daka = (MobileBy.ID, "com.tencent.wework:id/ghc")
    _kaishi_daka = (MobileBy.ID, "com.tencent.wework:id/alq")
    _jieguo = (MobileBy.XPATH, "//*[contains(@text, '外出打卡成功')]")
    # 创建方法：点击外出打卡
    def Clock_in(self):
        # 1. 点击外出打卡按钮  2. 点击外出打卡按钮
        self.find(*self._waichu_daka).click()
        self.find(*self._kaishi_daka).click()
        return self

    # 获取到打卡后的信息
    def get_Expected_results(self):
        result = self.finds(*self._jieguo)
        return [e_name.text for e_name in result]
