# -*- coding: utf-8 -*-
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
import doctest
from functools import reduce

def problem(i,j):
    '''
    >>> problem(1,10)
    23
    '''
    return reduce(lambda x,y:x+y, [i for i in range(i,j) if not i % 5 or not i % 3])


if __name__ == "__main__":
    doctest.testmod()
    print(problem(1,1000))
