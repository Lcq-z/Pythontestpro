from time import sleep
from selenium.webdriver import ActionChains

from XueXiBiJi.Base_jichu import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切换至id为'iframeResult'的frame标签
        self.driver.switch_to_frame('iframeResult')  # 因为要操作的是frame标签，直接定位不到，需切换后再定位

        # 定位到id后赋值
        drag = self.driver.find_element_by_id('draggable')
        # 定位到id后赋值
        drop = self.driver.find_element_by_id('droppable')
        sleep(2)

        # 需求是把drag挪到drop位置，所以得调用ActionChains方法
        action = ActionChains(self.driver)  # 将上面定位到的drag和drop传入ActionChains方法内赋值给action
        # 调用ActionChains内的挪动方法并传入定位赋值好的变量
        action.drag_and_drop(drag, drop).perform()  # .perform()属于ActionChains方法的语法结构，必须添加

        # 挪动完成后有alert弹框，在弹框上操作需切换至alert弹框
        self.driver.switch_to_alert()
        sleep(2)

        # 调用alert弹框的方法accept，接受现有弹框
        self.driver.switch_to_alert().accept()
        sleep(2)

        # 因为上面切换到了frame标签，所以得切换回默认网页
        self.driver.switch_to_default_content()  # 不切换的话，同样也会定位不到原网页上的元素
        # 定位到元素后点击
        self.driver.find_element_by_id('submitBTN').click()
        sleep(2)
