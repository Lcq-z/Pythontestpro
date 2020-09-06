from appium import webdriver

# 标定要测试的机型信息
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
# desired_caps['dontStopAppOnReset'] = 'true'
# 跳过安装、权限设置等操作（可以在调试或者运行的时候提升运行速度）
desired_caps['skipDeviceInitialization'] = 'true'
# 固定写法：pycharm连接到appium的地址
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 隐式等待10秒
driver.implicitly_wait(10)

def test_get_arr():
    # 在模拟器上的操作：
    # 获取到元素后点击
    driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
    # 获取到元素后赋值给变量ar
    ar = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
    # 通过get_attribute方法获取到元素的content-desc属性并打印  content-desc可以理解为by_accessibility_id
    print(ar.get_attribute("content-desc"))
    # 通过get_attribute方法获取到元素的resource-id属性并打印  resource-id：id
    print(ar.get_attribute("resource-id"))
    # 通过get_attribute方法获取到元素的enabled属性并打印  enabled：判断是否可用，返回 True 和 False
    print(ar.get_attribute("enabled"))
    # 通过get_attribute方法获取到元素的clickable属性并打印  clickable：判断是否被点击，返回 True 和 False
    print(ar.get_attribute("clickable"))
    # 通过get_attribute方法获取到元素的bounds属性并打印  bounds：坐标
    print(ar.get_attribute("bounds"))
