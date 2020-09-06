'''
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟，救我！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''
# 定义一个天山童姥类
class TongLao:
    # 构造方法
    def __init__(self,hp,power,defense):
        # 定义天山童姥的属性：
        self.hp = hp        # 血量
        self.power = power  # 武力值
        self.defense = defense  # 防御值

    # 定义see_people方法：传入name参数
    def see_people(self,name):
        # 如果传入的值 name =="WYZ"（无崖子），则打印，“师弟，快来救我！！！！”
        if name == "无崖子":
            print("师弟,快来救我！！！")
        # 如果传入“李秋水”，则打印“呸，贱人”
        elif name == "李秋水":
            print("呸，贱人，还不快滚！")
        # 如果传入“丁春秋”，打印“叛徒！我杀了你”
        elif name == "丁春秋":
            print("你这个叛徒！忘恩负义的东西，我杀了你！")

    # 定义fight_zms方法：天山折梅手会将天山童姥的武力值提升10倍，但血量缩减2倍
    def fight_zms(self,enemy_hp,enemy_power,enemy_defense): # 敌人的hp，power，进行一回合制对打

        self.power = int(self.power * 10) # 武力值提升10倍
        self.hp = int(self.hp / 2)        # 血量缩减2倍

        # 天山童姥的血量 = 天山童姥的血量 + 天山童姥的防御值 - 敌人武力值
        self.hp = self.hp +self.defense - enemy_power
        # 敌人的血量 = 敌人的血量 + 敌人的防御值 - 天山童姥武力值
        enemy_hp = enemy_hp +enemy_defense  - self.power

        # 比较双方血量,血量多的一方获胜。
        if self.hp > enemy_hp:      # 如果天山童姥的血量 > 敌人的血量 打印天山童姥获胜！
            print("天山童姥获胜！")
            print("天山童姥剩余血量：",self.hp)      # 打印天山童姥剩余血量
            print("敌人血量：",enemy_hp)           # 打印天敌人剩余血量

        elif self.hp < enemy_hp:    # 如果天山童姥的血量 < 敌人的血量 打印天山童姥也不过如此
            print("天山童姥也不过如此")
            print("天山童姥剩余血量：", self.hp)     # 打印天山童姥剩余血量
            print("敌人血量：", enemy_hp)          # 打印天山童姥剩余血量

        else:
            print("平局")      # 如果天山童姥的血量 > 敌人的血量 打印平局
            print("天山童姥剩余血量：", self.hp)     # 打印天山童姥剩余血量
            print("敌人血量：", enemy_hp)          # 打印天山童姥剩余血量


# 天山童姥类实例化,传入天山童姥的血量、武力值， 防御值
fight = TongLao(1000,1000,200)
fight.see_people("丁春秋")    # 调用see_people的方法 name参数为：丁春秋
fight.fight_zms(1000,1000,1000)  # 调用天山折梅手的方法，传入敌人的血量、武力值，防御值











