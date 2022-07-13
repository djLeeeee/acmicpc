from random import randrange
from math import gcd
from collections import defaultdict


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
    if not t % 2:
        ans.add(2)
        if 2 not in previous:
            previous[2] = 0
        while not t % 2:
            t //= 2
        pollard_rho(t)
        return
    if is_prime(t):
        if t not in previous:
            previous[t] = 0
        ans.add(t)
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


n = int(input())
gn = 0
previous = {}
pa = set()
arr = list(map(int, input().split()))
for i in range(n):
    ans = set()
    pollard_rho(arr[i])
    for key in previous:
        if key in ans:
            previous[key] += 1
            if i == n - 1:
                gn ^= previous[key]
        else:
            gn ^= previous[key]
            previous[key] = 0
print("First" if gn else "Second")
