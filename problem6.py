# -*- coding: utf-8 -*-
'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import doctest
from functools import reduce


def sum_of_squares(limit):
    '''
    >>> sum_of_squares(10)
    385
    '''
    return sum([n**2 for n in range(1,limit+1)])


def square_of_sum(limit):
    '''
    >>> square_of_sum(10)
    3025
    '''
    return sum(range(1,limit+1)) ** 2


def problem(limit):
    '''
    >>> problem(10)
    2640
    '''
    return square_of_sum(limit) - sum_of_squares(limit)


if __name__ == "__main__":
    doctest.testmod()
    print((problem(100)))
