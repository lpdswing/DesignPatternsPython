# 组合模式

class Store(object):
    '''店面基类'''

    # 添加店面
    def add(self, store):
        pass

    # 删除店面
    def remove(self, store):
        pass

    def pay_by_card(self):
        pass


class BranchStore(Store):

    def __init__(self, name):
        self.name = name
        self.my_store_list = []

    def pay_by_card(self):
        print("店面[%s]的积分已累加进该会员卡" % self.name)
        for s in self.my_store_list:
            s.pay_by_card()

    # 添加店面
    def add(self, store):
        self.my_store_list.append(store)

    # 删除店面
    def remove(self, store):
        self.my_store_list.remove(store)


class JoinStore(Store):
    '''加盟店'''

    def __init__(self, name):
        self.name = name

    def pay_by_card(self):
        print("店面[%s]的积分已累加进该会员卡" % self.name)

    def add(self, store):
        print("无添加子店权限")

    def remove(self, store):
        print("无删除子店权限")


if __name__ == '__main__':
    store = BranchStore("朝阳总店")
    branch = BranchStore("海滨分店")
    join_branch = JoinStore("昌平加盟1店")
    join_branch2 = JoinStore("昌平加盟2店")

    branch.add(join_branch)
    branch.add(join_branch2)

    store.add(branch)

    store.pay_by_card()
    print(store.my_store_list)