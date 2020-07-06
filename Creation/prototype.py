# 原型模式
import copy
from collections import OrderedDict

class Book:


    def __init__(self, name, authors, price, **rest):
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append(f'{i}:{ordered[i]}')
        return ','.join(mylist)


class Prototype:


    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(f'Incorrect object identifier: {identifier}')
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


if __name__ == '__main__':
    b1 = Book('Java从入门到放弃',('bw','wm', 'kk'),115,data='1999-01-01',length=223)
    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)

    b2 = prototype.clone(cid,price=223)
    for i in (b1,b2):
        print(i)
    print(id(b1))
    print(id(b2))