# 修饰器模式
from timeit import Timer
import functools


def memoize(fn):
    known = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    return memoizer


@memoize
def nsum(n):
    '''返回前n个数字的和'''
    assert n>=0,'n must be >=0'
    return 0 if n==0 else n+nsum(n-1)

@memoize
def fibnacci(n):
    '''返回fib第n个数'''
    assert n>=0,'n must be >=0'
    return n if n in(0,1) else fibnacci(n-1)+fibnacci(n-2)


if __name__ == '__main__':
    measure = [{'exec': 'fibnacci(100)', 'import': 'fibnacci',
                'func': fibnacci}, {'exec': 'nsum(200)', 'import': 'nsum',
                                     'func': nsum}]
    for m in measure:
        t = Timer(f'{m["exec"]}',f'from __main__ import {m["import"]}')
        print(t.timeit())