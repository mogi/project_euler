# -*- coding: utf-8 -*-
from doctest import testmod
from random import getrandbits
RULE = [True,True,True,True,False]


def execute(rule):
    '''
    >>> r = execute([True,True,True,True,False])
    >>> r[-5:]
    [True, True, True, True, False]
    '''
    is_loop = True;
    res = []
    while is_loop:
        n = [x == '1' for x in list(str('{0:0100b}'.format(getrandbits(100))))]
        for i in range(100):
            if not n[i:i+5] == rule:
                continue
            is_loop = False
            res.extend(n[:i+5])
            break
        else:
            if is_loop:
                res.extend(n)
    return res


if __name__ == "__main__":
    testmod()
    for o in execute(RULE):
        print(("zun" if o else "doko"))
    else:
        print('kiyoshi')
