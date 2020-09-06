# 导入TongLao类
from Python_testing.Work0.TianShanTongLao import TongLao
# 定义一个XuZhu类，继承于TongLao
class XuZhu(TongLao):
    # 构造方法
    def __init__(self):       # 为了在实例化XuZhu类时，不传入参数，直接输出
        pass
    # 虚竹宅心仁厚不打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印”阿弥陀佛，罪过罪过，望各位施主不要以命搏命。“
    def read_Scriptures(self):
        print("阿弥陀佛，罪过罪过，望各位施主不要以命搏命")

#实例化XuZhu类
xu = XuZhu()
xu.read_Scriptures()    # 调用read_Scriptures方法，打印输出



print("游戏结束")