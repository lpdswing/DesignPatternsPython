# 策略模式
class TravelStrategy:
    '''出行策略'''

    def travel(self):
        pass

class AirStrategy(TravelStrategy):

    def travel(self):
        print('坐飞机出行')


class TrainStrategy(TravelStrategy):

    def travel(self):
        print('坐高铁出行')


class CarStrategy(TravelStrategy):

    def travel(self):
        print('开车出行')


class TravelInterface:

    def __init__(self, ts):
        self.ts = ts

    def set_strategy(self, ts):
        self.ts = ts

    def travel(self):
        return self.ts.travel()

if __name__ == '__main__':
    t = TravelInterface(AirStrategy())
    t.travel()
    t.set_strategy(TrainStrategy())
    t.travel()