from appium.webdriver.common.mobileby import MobileBy
from Python_testing.Work8.pages.base_page import BasePage

"""
添加成员页面
"""

class MemberInformationPage(BasePage):
    # 定义只在此类中使用的私有变量
    _name_element = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']")
    _gender_element = (MobileBy.XPATH, "//*[@text='男']")
    _female_element = (MobileBy.XPATH, "//*[@text='女']")
    _male_element = (MobileBy.XPATH, "//*[@text='男']")
    _phonenum_element = (MobileBy.XPATH,
                         "//*[contains(@text, '手机') and @class='android.widget.TextView']/..//*[@class='android.widget.EditText']")
    _save_element = (MobileBy.XPATH, "//*[@text='保存'and@resource-id='com.tencent.wework:id/gur']")

    # 输入姓名
    def edit_name(self, name):
        # 定位到元素后输入传入的值
        self.find_and_sendkys(self._name_element, name)
        # return self是为了实现返回当前页面时依然可以实现链式调用
        return self

    # 选择年龄
    def edit_gender(self, gender):
        self.find_and_click(self._gender_element)
        # 如果传入的变量等于女，就选择性别：女
        if gender == "女":
            # 因为页面切换太快导致元素未加载，无法获取到元素，所以调用显示等待，当self._female_element元素可被点击时，再执行下发操作
            self.show_wait(self._female_element)
            # 定位到元素后点击
            self.find_and_click(self._female_element)
        # 如果没满足if中的条件，就执行else，也就是选择性别：男
        else:
            # 因为页面切换太快导致元素未加载，无法获取到元素，所以调用显示等待，当self._female_element元素可被点击时，再执行下发操作
            self.show_wait(self._male_element)
            # 定位到元素后点击
            self.find_and_click(self._male_element)
        # return self是为了实现返回当前页面时依然可以实现链式调用
        return self

    # 输入电话号码
    def edit_phonenum(self, phonenum):

        self.find_and_sendkys(self._phonenum_element, phonenum)
        # return self是为了实现返回当前页面时依然可以实现链式调用
        return self

    def save_and_click(self):
        # 解决循环导入问题
        from Python_testing.Work8.pages.add_member_page import AddMemberPage
        self.show_wait(self._save_element)
        self.find_and_click(self._save_element)
        # 跳转至添加成员页面，对AddMemberPage类进行实例化，表示业务逻辑的转换关系
        return AddMemberPage(self.driver)
