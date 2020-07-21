# 状态模式

class State:

    def __init__(self):
        pass

    def write_program(self, w):
        pass


class Work:

    def __init__(self):
        self.hour = 9
        self.curr = ForenoonState()

    def set_state(self, s):
        self.curr = s

    def write_program(self):
        self.curr.write_program(self)


class ForenoonState(State):

    def write_program(self, w: Work):
        if w.hour < 12:
            print(f'当前时间{w.hour}点,精神百倍')
        else:
            w.set_state(AfternoonState())
            w.write_program()

class AfternoonState(State):

    def write_program(self, w: Work):
        if w.hour < 21:
            print(f'当前时间{w.hour},状态还行,继续努力')
        else:
            w.set_state(SleepState())
            w.write_program()

class SleepState(State):

    def write_program(self, w):
        print(f'当前时间为{w.hour}点,不行了,睡了')


if __name__ == '__main__':
    w = Work()
    w.hour = 9
    w.write_program()
    w.hour = 15
    w.write_program()
    w.hour = 22
    w.write_program()
