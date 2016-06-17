# -*- coding: utf-8 -*-
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import doctest
from functools import reduce
from math import sqrt


def factor(n):
    '''
    >>> factor(13195)
    [5, 7, 13, 29]
    '''
    def calc(n):
        i = 2
        while i <= sqrt(n):
            if n % i != 0:
                i += 1
                continue
            yield int(i)
            n = n / i
        if n > 1:
            yield int(n)
    return [i for i in calc(n)]


def problem(n):
    '''
    >>> problem(13195)
    29
    '''
    return factor(n)[-1]


if __name__ == "__main__":
    doctest.testmod()
    print((problem(600851475143)))
