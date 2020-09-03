from appium.webdriver.common.mobileby import MobileBy
from Python_testing.Work6.pages.BasePage6 import BasePage6
from Python_testing.Work6.pages.Clock_in_page import ClochIn_Page


class WorkBench_Page(BasePage6):
    # 定义只在此类中使用的私有变量
    _dianji_daka = (MobileBy.ANDROID_UIAUTOMATOR,
                    'new UiScrollable(new UiSelector()'
                    '.scrollable(true).instance(0))'
                    '.scrollIntoView(new UiSelector()'
                    '.text("打卡").instance(0));')
    # 创建方法：跳转至打卡页面
    def go_to_ClochIn_Page(self):
        # 1. 在工作台页面中下滑动查找"打卡"元素后点击  2. 点击外出打卡按钮  3. 点击打卡按钮
        self.find(*self._dianji_daka).click()

        # return self是为了实现返回当前页面时依然可以实现链式调用
        return ClochIn_Page(self.driver)



