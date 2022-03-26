from sys import stdin

input = stdin.readline


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


def prime_checker(num):
    checker = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for i in range(12):
        if not Miller_Rabin(num, checker[i]):
            return 0
    return 1


a, b = map(int, input().split())
if a % 2 == 0:
    a += 1
ans = []
for j in range(a, b + 1, 2):
    if prime_checker(j):
        ans.append(j)
    elif j == 9:
        ans.append(j)
print(*ans)
