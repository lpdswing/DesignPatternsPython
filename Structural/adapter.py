# 适配器模式

# 将一个类的接口转换成客户希望的另外一个接口。使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
# 应用场景：希望复用一些现存的类，但是接口又与复用环境要求不一致。

class Player:
    '''球员基类'''
    name = ''


    def __init__(self, name):
        self.name = name

    def attack(self):
        pass

    def defense(self):
        pass


class Forwards(Player):
    '''前锋类'''


    def __init__(self, name):
        super(Forwards, self).__init__(name)

    def attack(self):
        print(f'前锋{self.name}进攻')

    def defense(self):
        print(f'前锋{self.name}防守')


class Center(Player):
    '''中锋类'''


    def __init__(self, name):
        super(Center, self).__init__(name)

    def attack(self):
        print(f'中锋{self.name}进攻')

    def defense(self):
        print(f'中锋{self.name}防守')


class Guards(Player):
    '''后卫类'''


    def __init__(self, name):
        super(Guards, self).__init__(name)

    def attack(self):
        print(f'后卫{self.name}进攻')

    def defense(self):
        print(f'后卫{self.name}防守')


# 外籍中锋（待适配类）
# 中锋
class ForeignCenter(Player):
    name = ''

    def __init__(self, name):
        Player.__init__(self, name)

    # 不同的成员方法，需要适配成Attack方法
    def foreign_attack(self):
        print("外籍中锋%s 进攻" % self.name)

    # 不同的成员方法，需要适配成Defense方法
    def foreign_defense(self):
        print("外籍中锋%s 防守" % self.name)


# 翻译类
class Translator(Player):
    foreign_center = None

    def __init__(self, name):
        self.foreign_center = ForeignCenter(name)

    def attack(self):
        self.foreign_center.foreign_attack()

    def defense(self):
        self.foreign_center.foreign_defense()


def main():
    b = Forwards('巴蒂尔')
    m = Guards('姚明')
    fm = Translator('mike')

    b.attack()
    m.defense()
    fm.attack()
    fm.defense()

if __name__ == '__main__':
    main()
