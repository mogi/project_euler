# -*- coding: utf-8 -*-
'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
import doctest
from functools import reduce


def problem(start, end):
    '''
    >>> problem(10,99)
    9009
    '''
    def calc(start,end):
        for i in range(end, int(end-start), -1):
            for j in range(i, start, -1):
                n = i*j
                if str(n) == str(n)[::-1]:
                    yield n
                    break

    sequence = [o for o in calc(start,end)]
    sequence.sort()
    return sequence[-1]


if __name__ == "__main__":
    doctest.testmod()
    print((problem(100,999)))
