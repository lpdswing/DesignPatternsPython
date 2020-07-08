# 解释器模式

class AbstractExpression:
    '''抽象解释器'''

    def interpreter(self, context):
        pass


class TerminalExpression(AbstractExpression):
    '''继承抽象解释器,具体解释器终端'''

    def interpreter(self, context):
        print(f'终端解释器:{context}')


class NotTerminalExpression(AbstractExpression):

    def interpreter(self, context):
        print(f'非终端解释器:{context}')


class Context:

    def __init__(self):
        self.name = ''

if __name__ == '__main__':
    context = Context()
    context.name = 'alex'
    arrs = [NotTerminalExpression(),TerminalExpression(),TerminalExpression()]
    for entry in arrs:
        entry.interpreter(context)
