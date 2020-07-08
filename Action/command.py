# 命令模式

import os


class MoveFileCommand:

    def __init__(self, src, dist):
        self.src = src
        self.dist = dist

    def execute(self):
        self()

    def __call__(self, *args, **kwargs):
        print(f'rename {self.src} to {self.dist}')
        # os.rename(self.src, self.dist)

    def undo(self):
        print(f'rename from {self.dist} to {self.src}')
        # os.rename(self.dist, self.src)


if __name__ == '__main__':
    command_stack = []

    command_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
    command_stack.append(MoveFileCommand('bar.txt', 'foo.txt'))

    for cmd in command_stack:
        cmd.execute()

    for cmd in reversed(command_stack):
        cmd.undo()
