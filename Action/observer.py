# 观察者模式

class ObserverBase:
    '''观察者基类,类似大v账户'''

    def __init__(self):
        self._observerd_list = [] # 粉丝列表

    def attach(self, observe_subject):
        '''添加粉丝'''
        if observe_subject not in self._observerd_list:
            self._observerd_list.append(observe_subject)
            print(f'{self.name}已经将{observe_subject.name}加入观察队列...')

    def detach(self, observe_subject):
        '''解除观察者关系,删除粉丝'''
        try:
            self._observerd_list.remove(observe_subject)
            print(f'不再观察{observe_subject}')
        except ValueError:
            pass

    def notify(self):
        '''通知粉丝'''
        for fun in self._observerd_list:
            fun.by_notified(self)


class Observer(ObserverBase):
    '''观察者,实际的大v'''
    def __init__(self,name):
        super(Observer,self).__init__()
        self.name = name
        self._msg = ''

    @property
    def msg(self):
        '''当前状态'''
        return self._msg

    @msg.setter
    def msg(self, content):
        '''当msg被设置的时候执行的方法'''
        self._msg = content
        self.notify()


class FansViewer:
    '''粉丝'''
    def __init__(self, name):
        self.name = name

    def by_notified(self, big_v):
        print(f'粉丝{self.name}收到{big_v.name}消息{big_v.msg}')


if __name__ == '__main__':
    bigv1 = Observer('大v1')
    bigv2 = Observer('大v2')

    f1 = FansViewer('fans1')
    f2 = FansViewer('fans2')

    bigv1.attach(f1)
    bigv1.attach(f2)

    bigv2.attach(f2)

    bigv1.msg = '官宣...'
    bigv2.msg = '广告推荐...'
