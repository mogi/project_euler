# -*- coding: utf-8 -*-
'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not exceed four million.
'''
import doctest
from functools import reduce


def fib(i,j,limit):
    '''
    >>> fib(1,2,90)
    [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    '''
    sequence = [i,j]
    calc = lambda l:int(l[-1] + l[-2])
    x = calc(sequence)
    while x < limit:
        sequence.append(x)
        x = calc(sequence)
    return sequence


def problem(i, j, limit):
    return reduce(lambda x,y:x+y, [n for n in fib(i,j,limit) if n%2==0])


if __name__ == "__main__":
    doctest.testmod()
    print((problem(1,2,4000000)))