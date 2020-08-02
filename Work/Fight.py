"""
题目：
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""
# 定义一个函数 fight
def fight():
    # 定义4个变量，my_hp：我的血量，my_power：我的攻击力，your_hp：对手血量，your_power：对手攻击力
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 188
    # 循环进行多次对打
    while True:
        # 我的血量 = 我的血量 - 对手攻击力
        my_hp = my_hp - your_power
        # 对手血量 = 对手血量 - 我的攻击力
        your_hp = your_hp - my_power
        #  多次对打后，谁的血量先小于零，谁就输了
        if my_hp <= 0:
            print("我输了")
            print("我的血量还剩：",my_hp)
            print("你的血量还剩：",your_hp)
            break       # 结束整个循环
        elif your_hp <= 0:
            print("哈哈，我赢了")
            print("我的血量还剩：", my_hp)
            print("你的血量还剩：",your_hp)
            break       # 结束整个循环
# 调用fight函数
fight()

print("游戏结束")