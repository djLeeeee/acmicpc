"""
파이썬 공식 문서
https://python.flowdas.com/library/decimal.html#recipes
"""
from math import sin
from decimal import *

getcontext().prec = 50
pi = Decimal('3.1415926535897932384626433832795028841971693993751058209749445923')


def sin(x):
    x = x % (2 * pi)
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s


def f(x):
    return a * x + b * sin(x) - c


a, b, c = map(Decimal, input().split())
left = (c - b) / a
right = (c + b) / a
while (right - left) > Decimal(1e-40):
    middle = (left + right) / 2
    if f(middle) < 0:
        left = middle
    else:
        right = middle
print(round(middle, 6))
