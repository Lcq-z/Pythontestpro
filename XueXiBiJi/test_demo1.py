#
# import random
#
#
#
# a = int(input("请输入您要出的拳： 1.石头 2.剪刀 3.布"))
# b = random.randint(1,3)
# print("玩家的出拳选择是： %d  电脑出拳是： %d" % (a,b))
#
# if ((a == 1 and b == 2)
#         or(a == 2 and b == 3)
#         or(a == 3 and b == 1)):
#     print("看来我还是很强的嘛")
# elif a == b:
#     print("哎哟，这么巧，竟然平局，再来！")
# else:
#     print("不愧是电脑，果然强大")
#
#
#
# print("游戏结束")
#
#
#
#
#
#
# import random
#
# # a = int(input("请输入你猜的数字"))   #人猜的
# b = random.randint(1,101)  #计算机猜的
# while True:
#     a = int(input("请输入你猜的数字"))
#     if a > b:
#         print("小一点")
#         break
#     elif b > a:
#         print("大一点")
#         break
#     elif a == b:
#         print("猜对了")
#         break
# print("游戏结束")
#
#
#
#
#
#
#
#
#
#
#
# """
# 题目：
# 一个回合制游戏，每个角色都有hp 和power，
# hp代表血量，power代表攻击力，hp的初始值为1000，
# power的初始值为200。打斗多个回合
# 定义一个fight方法：
# my_hp = hp - enemy_power
# enemy_final_hp = enemy_hp - my_power
# 谁的hp先为0，那么谁就输了
# """
# import random
# # 定义一个函数 fight
# def fight():
#     # 定义4个变量，my_hp：我的血量，my_power：我的攻击力，your_hp：对手血量，your_power：对手攻击力
#     my_hp = 1000
#     my_power = 200
#     your_hp = 1000
#     your_power = 188
#     # 循环进行多次对打
#     while True:
#         # 我的血量 = 我的血量 - 对手攻击力
#         my_hp = my_hp - your_power
#         # 对手血量 = 对手血量 - 我的攻击力
#         your_hp = your_hp - my_power
#         #  多次对打后，谁的血量先小于零，谁就输了
#         if my_hp <= 0:
#             print("我输了")
#             print("我的血量还剩：",my_hp)
#             print("你的血量还剩：",your_hp)
#             break       # 结束整个循环
#         elif your_hp <= 0:
#             print("你输了")
#             print("我的血量还剩：", my_hp)
#             print("你的血量还剩：",your_hp)
#             break       # 结束整个循环
# fight()
#
# print("游戏结束")
#
#
#
#
#
#
#
#
#
#
#
# def manthe(**a):
#     print(a)
#     """
#
#     :param a:
#     :return:
#     """
#
# manthe(a=1,b=2,c=3)
# def mac(*a):
#     print(a[0])
#     print(a[1])
#     print(a[2])
#     print(a[3])
#
# print(mac(1,23,3,4))
#
#
# #
# abc = []
# for i in range(1,4):
#     for j in range(1,4):
#         abc.append(i*j)
# print(abc)
#
#
#
# list_a = [i*j for i in range(1,4) for j in range(1,4)]
# print(list_a)
#
# a = "天气不错"
# b = 12
# c = [1,2,3]
# dict1 = {'name':'tom','age':'20'}
# print(f"list {c[0]}，{dict1['name']}")
# #
#
#
# print("num is %.2f"%3.1415)
#
#
# list1 = ['tom','jerry','sqp']
# print('we name is {}、{}、{}'.format(*list1))
#
#
#
#
# list_a = []
# for i in range(1,4):
#     for j in range(1.4):
#         list_a.append(i*j)
# print(list_a)
#
#
#
#
#
#
#
#
#
#
#
#
# print("今天 {}, 年龄 {}".format(a,b))
# print('list: {} 字典: {}'.format(c,dict1))
#
#
# list2 = [1,3,4,6,8,2]
# print('ss {},aa {}'.format(*list2))
#
# dict2 = {'aaa':'bbb','ccc':'ddd'}
#
#
#
#
# import time
# print(time.asctime())       # 国外格式的时间格式：星期，月份，日子，小时，分钟，秒数，年份
# print(time.time())          # 时间戳，从1970年1月1日0点0分0秒到目前的秒数总和，可以在百度找装换工具
# print(time.localtime())     # 生成了元组的格式：年份，月份，日，小时，分钟，秒，星期，一年之中的天数
#
# # 使用time.strftime方法将time.localtime生成的元组格式转化为指定的标准时间格式
# print(time.strftime("%Y年%m月%d日 %H点%M分%S秒", time.localtime()))
#
#
# # 例:获取两天前的时间(2天前的时间)
# now_time = time.time() # 获取当前的时间戳
# two_day = now_time - 60*60*48    # 用当前的时间戳 - 60秒 * 60分钟 * 24小时 * 2天
# time_aa = time.localtime(two_day) # 转换成time.localtime格式，赋值给time_aa
# print(time.strftime("%Y年%m月%d日 %H点%M分%S秒", time_aa)) # 打印







