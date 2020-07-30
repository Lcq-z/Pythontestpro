import random


a = int(input("请输入您要出的拳： 1.石头 2.剪刀 3.布"))
b = random.randint(1,3)
print("玩家的出拳选择是： %d  电脑出拳是： %d" % (a,b))

if ((a == 1 and b == 2)
        or(a == 2 and b == 3)
        or(a == 3 and b == 1)):
    print("看来我还是很强的嘛")
elif a == b:
    print("哎哟，这么巧，竟然平局，再来！")
else:
    print("不愧是电脑，果然强大")



print("游戏结束")





