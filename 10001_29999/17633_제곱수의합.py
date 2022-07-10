"""
삼성 블로그 제곱수의 합
http://www.secmem.org/blog/2019/10/18/sum-of-squares/
"""
from collections import defaultdict
from random import randrange
from math import gcd


def power(a, b, mod):
    result = 1
    while b > 0:
        if b % 2:
            result = (result * a) % mod
        a = (a * a) % mod
        b //= 2
    return result


def Miller_Rabin(num, check):
    if num == check:
        return 1
    k = num - 1
    while True:
        x = power(check, k, num)
        if x == num - 1:
            return 1
        if k % 2:
            if x == 1:
                return 1
            break
        k //= 2
    return 0


def is_prime(t):
    checker = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for c in checker:
        if not Miller_Rabin(t, c):
            return 0
    return 1


def pollard_rho(t):
    if t == 1:
        return
    if is_prime(t):
        div[t] += 1
        return
    x = randrange(2, t)
    y = x
    c = randrange(1, 10)
    g = 1
    while g == 1:
        x = (x * x % t + c)
        y = (y * y % t + c)
        y = (y * y % t + c)
        g = gcd(x - y, t)
        if g == t:
            return pollard_rho(t)
    pollard_rho(g)
    pollard_rho(t // g)


def sol(t):
    while not t % 4:
        t //= 4
    if t % 8 == 7:
        return 4
    if int(t ** 0.5) * int(t ** 0.5) == t:
        return 1
    if not t % 2:
        t //= 2
    pollard_rho(t)
    for key, value in div.items():
        if key % 4 == 3 and value % 2:
            return 3
    return 2


target = int(input())
div = defaultdict(int)
print(sol(target))
