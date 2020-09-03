from appium.webdriver.common.mobileby import MobileBy
from Python_testing.Work6.pages.BasePage6 import BasePage6


class WorkBench_Page(BasePage6):
    # 定义只在此类中使用的私有变量
    _dianji_daka = (MobileBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector()'
                    '.scrollable(true).instance(0))'
                    '.scrollIntoView(new UiSelector()'
                    '.text("打卡").instance(0));')
    _waichu_daka = (MobileBy.ID, "com.tencent.wework:id/ghc")
    _kaishi_daka = (MobileBy.ID, "com.tencent.wework:id/alq")
    _jieguo = (MobileBy.XPATH, "//*[contains(@text, '外出打卡成功')]")

    # 创建方法：点击打卡
    def Clock_in(self):
        # 1. 在工作台页面中下滑动查找"打卡"元素后点击  2. 点击外出打卡按钮  3. 点击打卡按钮
        self.find(*self._dianji_daka).click()
        self.find(*self._waichu_daka).click()
        self.find(*self._kaishi_daka).click()

        # return self是为了实现返回当前页面时依然可以实现链式调用
        return self

    # 获取到打卡后的信息
    def get_Expected_results(self):
        result = self.finds(*self._jieguo)
        return [e_name.text for e_name in result]

