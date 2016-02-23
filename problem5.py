# -*- coding: utf-8 -*-
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?
'''
import doctest
from functools import reduce


def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1


def problem(start,end):
    '''
    >>> problem(1,10)
    2520
    '''
    seed = reduce(lambda x,y:x*y, [n for n in range(start,end) if is_prime(n)])
    return int(seed)


if __name__ == "__main__":
    '''
    >>> problem(1,20)
    232792560
    '''
    doctest.testmod()
    #print((problem(1,20)))
