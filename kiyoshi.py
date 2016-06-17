# -*- coding: utf-8 -*-
from doctest import testmod
from random import getrandbits
RULE = ['zun','zun','zun','zun','doko',]


def execute():
    '''
    >>> r = execute()
    >>> r[-1]
    'kiyoshi'
    >>> r[-2]
    ['zun', 'zun', 'zun', 'zun', 'doko']
    '''
    result = []
    n = None
    while n != RULE:
        n = ['zun' if int(x)==0 else 'doko' for x in list(str('{0:05b}'.format(getrandbits(5),'b')))]
        result.append(n)
    else:
        result.append('kiyoshi')
    return result


if __name__ == "__main__":
    testmod()
    for o in execute():
        print(o)
