# 控制器模式

quotes = (
    'a man is not complete until he is married',
    'as i said before, i never repeat myself',
    'behind a successful man is an exhausted woman',
    'Black holes really suck ...'
)

class QuoteModel:


    def get_quotes(self, n):
        try:
            value = quotes[n]
        except IndexError as e:
            value = 'Not Found'
        return value

class QuoteTerminalView:


    def  show(self, quote):
        print(f'and the quote is: {quote}')

    def error(self, msg):
        print(f'Error: {msg}')

    def select_quote(self):
        return input('which quote number would you like to see?')


class QuoteTerminalController:


    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                index = int(n)
                valid_input = True
            except ValueError as e:
                self.view.error(f'Incorrect index {n}')
            quote = self.model.get_quotes(index)
            self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()