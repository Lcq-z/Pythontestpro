import random

# a = int(input("请输入你猜的数字"))   #人猜的
b = random.randint(1,101)  #计算机猜的
while True:
    a = int(input("请输入你猜的数字"))
    if a > b:
        print("小一点")
    elif b > a:
        print("大一点")
    elif a == b:
        print("猜对了")
        break
print("游戏结束")
















