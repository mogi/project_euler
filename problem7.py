# -*- coding: utf-8 -*-
'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''
import doctest
from functools import reduce


def primes(n):
    '''
    >>> primes(6)
    [2, 3, 5, 7, 11, 13]
    '''
    def calc(i, chunk):
        for x in chunk:
            if i % x == 0:
                continue
        else:
            yield i

    seaquence = [2]
    i = 3
    while len(seaquence) < n:
        seaquence.append(next(calc(i,seaquence)))
        i += 2
    return seaquence


def problem(n):
    '''
    >>> problem(6)
    13
    '''
    return primes(n)[-1]


if __name__ == "__main__":
    doctest.testmod()
    print((problem(10001)))
