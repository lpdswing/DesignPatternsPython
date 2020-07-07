# 享元模式
# 有点像单例, 有的资料也用这种共享内存的方式作为单例的模式的一种实现

import weakref

class Card:
    # 弱引用值的映射类。 当不再有对键的强引用时字典中的条目将被丢弃
    _CardPool = weakref.WeakValueDictionary()


    def __new__(cls, value, suit):
        obj = Card._CardPool.get(value +suit, None)
        if not obj:
            obj = object.__new__(cls)
            Card._CardPool[value + suit] = obj
            obj.value, obj.suit = value, suit
        return obj

    def __str__(self):
        return f'{self.value,self.suit}'


if __name__ == '__main__':
    c1 = Card('8', 'h')
    c2 = Card('8', 'h')
    print(c1, c2)
    print(c1 == c2)
    print(id(c1),id(c2))