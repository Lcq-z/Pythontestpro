"""
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
"""
# 创建类：猴
class Monkey:
    # 猴的属性：
    Thick = "hair"      # 浓密的毛发
    tail = 1            # 有1条尾巴
    brain = "develop"   # 大脑发达

    #  使用def关键字定义方法
    def playing(self,buddy):  # 定义方法：玩耍
        print(f"小猴子在和{buddy}玩耍")    # 通过字面量插值的方法，拼接字符串，打印输出

    #  使用def关键字定义方法
    def eating(self,banana):   # 定义方法：吃
        print(f"小猴子在吃{banana}")      # 通过字面量插值的方法，拼接字符串，打印输出

    #  使用def关键字定义方法
    def louse(self):    # 定义方法：抓虱子
        print("小猴子在抓虱子")    # 打印输出

# 实例化类
monkey = Monkey()
print("小猴子有",monkey.Thick)           # 调用小猴子的属性，打印输出属性
print("小猴子有",monkey.tail,"条尾巴")   # 调用小猴子的属性，打印输出属性
print("小猴子的",monkey.brain)         # 调用小猴子的属性，打印输出属性
monkey.eating("香蕉")          # 调用小猴子的方法，传入参数：香蕉
monkey.playing("小伙伴们")     # 调用小猴子的方法，传入参数：小伙伴
monkey.louse()               # 调用小猴子的方法，打印输出






# 创建类：兔子
class Rabbit:
    # 定义兔子的属性：
    def __init__(self,colour,body,eyes):
        self.colour = colour  # 颜色
        self.body = body      # 身体
        self.eyes = eyes      # 眼睛

    #  使用def关键字定义方法
    def Clean_hair(self):  # 定义方法：清洁毛发
        print("兔子在清洁毛发")

    #  使用def关键字定义方法
    def jump(self):   # 定义方法：跳跃
        print("兔子在跳") # 打印输出

    #  使用def关键字定义方法
    def Circle(self):    # 定义方法：绕圈
        print("兔子在绕圈") # 打印输出

# 类实例化并传入三个参数："白色的","身体很灵活","眼睛是红色的"
rabbit = Rabbit("白色的","身体很灵活","的眼睛是红色的")
print(f"兔子的毛发是{rabbit.colour}")  # 调用兔子的属性，通过字面量插值的方法，拼接字符串，打印输出
print(f"兔子的{rabbit.body}")       # 调用兔子的属性，通过字面量插值的方法，拼接字符串，打印输出
print(f"兔子{rabbit.eyes}")       # 调用兔子的属性，通过字面量插值的方法，拼接字符串，打印输出
rabbit.Clean_hair()       # 调用兔子的方法，打印输出
rabbit.jump()            # 调用兔子的方法，打印输出
rabbit.Circle()         # 调用兔子的方法，打印输出







# 创建类：外星物种(毒液)
class Alien_Species:
    # 构造方法，外星物种毒液的属性：
    def __init__(self,attribute1,attribute2,attribute3):
        self.attribute1 = attribute1    # 属性1：强大的防御力
        self.attribute2 = attribute2    # 属性2：极强的自愈能力力
        self.attribute3 = attribute3    # 属性3：弱点：害怕噪音和高温

    #  使用def关键字定义方法
    def looking_for_hosts(self):     # 定义方法：寻找宿主
        print("毒液正在寻找宿主")      # 打印输出

    #  使用def关键字定义方法
    def punish_bad_people(self):     # 定义方法：制裁换人
        print("毒液在制裁坏人")       # 打印输出

    #  使用def关键字定义方法
    def transformation(self):        # 定义方法：变身为武器
        print("毒液将四肢变为武器")    # 打印输出

# 类的实例化
alien_Species = Alien_Species("强大的防御力","极强的自愈能力力","弱点：害怕噪音和高温")   # 调用毒液的属性，打印输出
print(f"毒液拥有{alien_Species.attribute1}和{alien_Species.attribute2}")          # 调用毒液的属性，通过字面量插值的方法，拼接字符串，打印输出
print("毒液的",alien_Species.attribute3)         # 调用毒液的属性，打印输出
alien_Species.looking_for_hosts()              # 调用毒液的方法，打印输出
alien_Species.punish_bad_people()             # 调用毒液的方法，打印输出
alien_Species.transformation()               # 调用毒液的方法，打印输出






# 创建子类，继承于外星物种(屠杀,毒液的儿子)
class Carnage(Alien_Species):
    # 继承父类的构造方法
    def __init__(self,attribute1,attribute2,attribute3,character1,character2):
        # 继承父类的属性
        super().__init__(attribute1,attribute2,attribute3)
        self.character1 = character1    # 屠杀的属性：暴戾
        self.character2 = character2    # 屠杀的属性：疯狂

    # 使用def关键字定义方法
    def insane(self):
        print("屠杀：”父亲他变了，我不再认同他，它将是我的死敌“")  # 打印输出，表示屠杀它会与它的父亲毒液为敌

    # 使用def关键字定义方法
    def overbearing(self):
        print("屠杀：”我需要找到那个对人类慈爱的父亲与蜘蛛侠，然后杀掉他们，屠尽一切！”")   # 打印输出，表示屠杀为超级大反派，和它的父亲毒液与蜘蛛侠为敌


# 类的实例化，传入5个参数，分别是父亲毒液的三个属性和’屠杀‘自己的两个属性。
carnage = Carnage("强大的防御力","极强的自愈能力力","弱点：害怕噪音和高温","暴戾的","疯狂的")
# 调用继承的父类属性，通过字面量插值的方法，拼接字符串，打印输出
print(f"屠杀也具有父亲毒液的属性：{carnage.attribute1},{carnage.attribute2},{carnage.attribute3}")
# 调用’屠杀‘自己的属性，通过字面量插值的方法，拼接字符串，并打印输出
print(f"屠杀的性格（属性）：{carnage.character1}，{carnage.character2}")
carnage.insane()         # 调用屠杀的方法，打印输出
carnage.overbearing()   # 调用屠杀的方法，打印输出








# 创建类：屠杀和毒液战斗
class Fight:
    # 构造方法，定义屠杀的属性：
    def __init__(self,hp,power,defense,anger):
        self.hp = hp  # 血量
        self.power = power  # 攻击力
        self.anger = anger  # 怒气值
        self.defense = defense  # 防御值

    # 定义battle方法：定义毒液的属性，分别是：血量，攻击力，防御力
    def battle(self,venom_hp,venom_power,venom_defense):
        if self.power > 100:       # 如果屠杀的怒气值大于100时，屠杀的攻击力暴涨10倍，血量降低2倍，同时防御力降低2倍
            self.power *= 10
            self.hp /= 2
            self.defense /= 2
        elif self.power < 100:     # 如果屠杀的怒气值小于100时，屠杀的血量增长2倍
            self.hp *= 2

        # 屠杀的血量 = 屠杀的血量 + 屠杀的防御力 - 毒液的攻击力
        self.hp = self.hp + self.defense - venom_power
        # 毒液的血量 = 毒液的血量 + 毒液的防御力 - 屠杀的攻击力
        venom_hp = venom_hp + venom_defense - self.power

        # 如果屠杀的血量 > 毒液的血量  打印内容，屠杀的血量，毒液的血量
        if self.hp > venom_hp:
            print("哦，我亲爱的父亲，你输了，我将吞掉你，然后再干掉蜘蛛侠！")
            print(f"屠杀的血量：{self.hp}")   # 通过字面量插值的方法，拼接字符串，打印输出
            print(f"毒液的血量：{venom_hp}")  # 通过字面量插值的方法，拼接字符串，打印输出
        # 如果毒液的血量 > 屠杀的血量  打印内容
        elif venom_hp > self.hp:
            print("孩子，我们之前都错了，不能随意造杀戮，之前的错事，我会弥补也会重新教导你")
            print(f"屠杀的血量：{self.hp}")   # 通过字面量插值的方法，拼接字符串，打印输出
            print(f"毒液的血量：{venom_hp}")  # 通过字面量插值的方法，拼接字符串，打印输出

# 类实例化,传入屠杀血量、武力值、怒气值，防御值
fight = Fight(10000,5000,10,4000)
# 调用battle方法，传入毒液的血量、攻击力，防御值
fight.battle(20000,100000,10000)


