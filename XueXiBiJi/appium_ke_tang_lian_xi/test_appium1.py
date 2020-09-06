# from appium import webdriver
#
# desired_caps={}
# desired_caps['platformName']='Android'
# desired_caps['platformVersion']='6.0'
# desired_caps['deviceName']='emulator-5554'
# desired_caps ['appPackage']='com.android.settings'
# desired_caps['appActivity']='com.android.settings.Settings'
# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# driver.quit()


from appium import webdriver

# 定义字典
desired_caps = {}
# 测试的设备为android系统
desired_caps['platformName'] = 'android'
# android系统版本为6.0
desired_caps['platformVersion'] = '6.0'
# 连接设备的ip地址
desired_caps['deviceName'] = '127.0.0.1:7555'
# 测试android设备中的雪球app
desired_caps['appPackage'] = 'com.xueqiu.android'
# 测试android设备中雪球app的欢迎页
desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
# 用于保留上次登录数据，默认登录状态（这里的作用是：如果有软件更新弹窗，点击关闭后下次不再提示）
desired_caps['noReset'] = 'true'
# 执行测试用例之后，不停止app，停留在执行完毕页面可接着往下操作（可以在调试或者运行的时候提升运行速度）
desired_caps['dontStopAppOnReset'] = 'true'
# 跳过安装、权限设置等操作（可以在调试或者运行的时候提升运行速度）
desired_caps['skipDeviceInitialization'] = 'true'

# 固定写法：pycharm连接到appium的地址
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 与上面写法不同，但意思一样
# ceshi_lianjie = {
#
#   "platformName": "android",
#   "deviceName": "127.0.0.1:7555",
#   "appPackage": "com.xueqiu.android",
#   "appActivity": ".view.WelcomeActivityAlias",
#   "noReset": True # 用于保留上次登录数据，默认登录状态（这里的作用是：如果有软件更新弹窗，点击关闭后下次不再提示）
# }
# 固定写法：pycharm连接到appium的地址
# driver= webdriver.Remote("http://127.0.0.1:4723/wd/hub",ceshi_lianjie)

# 隐式等待10秒，（很重要！等页面加载完毕，再进行定位操作）
driver.implicitly_wait(5)

el3 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el3.click()
el4 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el4.send_keys("alibab")
el5 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el5.click()

# driver.back返回的意思
driver.back()
driver.back()
driver.quit()
