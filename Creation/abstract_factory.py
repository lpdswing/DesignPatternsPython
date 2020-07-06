# 抽象工厂设计模式

# 青蛙类
class Frog:

    def __init__(self, name):
        self.name = name

    def interact_with(self, obstacle):
        '''描述青蛙遇到障碍'''
        print(f'青蛙遇到{obstacle},然后{obstacle.action()}')


# 虫子类
class Bug:

    def __str__(self):
        return '一条虫子'

    def action(self):
        return '吃了它'


# 抽象工厂,创建游戏主人公和障碍物
class FrogWorld:

    def __init__(self, name):
        self.player_name = name

    def create(self):
        return Frog(self.player_name)

    def create_obstacle(self):
        return Bug()


# 巫师类
class Wizard:

    def __init__(self, name):
        self.name = name

    def interact_with(self, obstacle):
        print(f'巫师大战{obstacle},然后{obstacle.action()}')


# 兽人类
class Ork:

    def __str__(self):
        return '一个兽人'

    def action(self):
        return '杀了他'


# 抽象工厂
class WizardWorld:

    def __init__(self, name):
        self.player_name = name

    def create(self):
        return Wizard(self.player_name)

    def create_obstacle(self):
        return Ork()


class GameEnvironment:
    '''
    游戏入口,接收factory作为输入,创建游戏世界
    '''

    def __init__(self, factory):
        self.hero = factory.create()
        self.obstacle = factory.create_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


if __name__ == '__main__':
    g1 = GameEnvironment(FrogWorld('青蛙王子'))
    g1.play()
    g2 = GameEnvironment(WizardWorld('巫师王'))
    g2.play()
