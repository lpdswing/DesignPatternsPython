# 工厂方法

# 形状基类,所有形状继承与该类
class Shape:
    '''形状工厂类'''
    def get_shape(self):
        return self.shape_name

    def draw(self):
        raise NotImplementedError


# 圆形类
class Circle(Shape):

    def __init__(self):
        self.shape_name = 'Circle'

    def draw(self):
        print('draw circle.')


# 四边形
class Rectangle(Shape):

    def __init__(self):
        self.shape_name = 'Rectangle'

    def draw(self):
        print('draw Rectangle.')


# 形状工厂基类
class ShapeFactory:
    '''接口基类'''

    def create(self):
        '''把要创建的工厂装配进来'''
        raise NotImplementedError


# 圆形工厂
class CircleFactory(ShapeFactory):

    def create(self):
        return Circle()


# 四边形工厂
class RectangleFactory(ShapeFactory):

    def create(self):
        return Rectangle()


if __name__ == '__main__':
    cf = CircleFactory()
    obj = cf.create()
    print(obj.get_shape())
    obj.draw()
    rf = RectangleFactory()
    obj = rf.create()
    obj.get_shape()
    obj.draw()