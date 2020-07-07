# 外观模式

class Stock:
    name = '股票'

    def buy(self):
        print(f'买{self.name}')

    def sell(self):
        print(f'卖{self.name}')


class ETF:
    name = '基金'

    def buy(self):
        print(f'买{self.name}')

    def sell(self):
        print(f'卖{self.name}')


class Future:
    name = '期货'

    def buy(self):
        print(f'买{self.name}')

    def sell(self):
        print(f'卖{self.name}')



class Facade:
    '''外观'''


    def __init__(self):
        self.stock = Stock()
        self.etf = ETF()
        self.future = Future()

    def buy_found(self):
        self.stock.buy()
        self.etf.buy()
        self.future.buy()

    def sell_found(self):
        self.stock.sell()
        self.etf.sell()
        self.future.sell()



if __name__ == '__main__':
    f = Facade()
    f.buy_found()
    f.sell_found()
