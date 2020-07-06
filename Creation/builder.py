# 建造者模式
# 以人为例

class Person:
    '''产品类,最终产出的东西'''

    def __init__(self):
        self.head = ''
        self.body = ''
        self.arm = ''
        self.leg = ''

    def get_person_info(self):
        print(
            f'head:{self.head},body:{self.body},arm:{self.arm},leg:{self.leg}')


class PersonBuilder:
    '''建造者基类'''

    def build_head(self):
        pass

    def build_body(self):
        pass

    def build_arm(self):
        pass

    def build_leg(self):
        pass


class FatPersonBuilder(PersonBuilder):
    '''胖子建造者'''
    type = '胖子'

    def __init__(self):
        self.person = Person()

    def build_head(self):
        self.person.head = f'构建{self.type}的头'

    def build_body(self):
        self.person.body = f'构建{self.type}的身体'

    def build_arm(self):
        self.person.arm = f'构建{self.type}的手'

    def build_leg(self):
        self.person.leg = f'构建{self.type}的腿'

    def get_person(self):
        return self.person


class ThinPersonBuilder(PersonBuilder):
    '''瘦子建造者'''
    type = '瘦子'

    def __init__(self):
        self.person = Person()

    def build_head(self):
        self.person.head = f'构建{self.type}的头'

    def build_body(self):
        self.person.body = f'构建{self.type}的身体'

    def build_arm(self):
        self.person.arm = f'构建{self.type}的手'

    def build_leg(self):
        self.person.leg = f'构建{self.type}的腿'

    def get_person(self):
        return self.person


class PersonDirector:
    '''指挥官'''

    def __init__(self, pb):
        self.pb = pb

    def create_person(self):
        # 调用建造者各部位方法来创建人
        self.pb.build_head()
        self.pb.build_body()
        self.pb.build_arm()
        self.pb.build_leg()
        return self.pb.get_person()


def client():
    pb = ThinPersonBuilder()
    pd = PersonDirector(pb)
    thin = pd.create_person()
    thin.get_person_info()

    pb = FatPersonBuilder()
    pd = PersonDirector(pb)
    fat = pd.create_person()
    fat.get_person_info()


if __name__ == '__main__':
    client()
