from sys import stdin, setrecursionlimit
from collections import defaultdict
from random import randrange
from math import gcd

input = stdin.readline
setrecursionlimit(10 ** 5)


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
        div_p[2] += 1
        pollard_rho(t // 2)
        return
    if is_prime(t):
        div_p[t] += 1
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


def dfs(num, idx):
    if idx == n:
        div.append(num)
        return
    t = div_arr[idx]
    for exp in range(div_p[t] + 1):
        dfs(num * t ** exp, idx + 1)


ans = []
while True:
    target = int(input())
    if not target:
        break
    if target == 1:
        now = 3
    elif is_prime(target):
        now = target + 2
    else:
        div_p = defaultdict(int)
        pollard_rho(target)
        div = []
        div_arr = list(div_p)
        n = len(div_p)
        dfs(1, 0)
        div.sort()
        m = len(div)
        now = target + 2
        for i in range(m):
            if div[i] ** 3 > target:
                break
            remain = target // div[i]
            start = i
            end = m // 2 + 1
            while start <= end:
                mid = (start + end) // 2
                if div[mid] * div[mid] > remain:
                    end = mid - 1
                else:
                    res = mid
                    start = mid + 1
            for j in range(res, i - 1, -1):
                if not remain % div[j]:
                    if now > div[i] + div[j] + remain // div[j]:
                        now = div[i] + div[j] + remain // div[j]
                    break
    ans.append(now)
print(*ans, sep='\n')
