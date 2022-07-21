from sys import stdin

input = stdin.readline


def power(a, b):
    result = 1
    while b > 0:
        if b % 2:
            result *= a
            result %= div
        a *= a
        a %= div
        b //= 2
    return result


div = 998244353
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
ans = 1
m += 1
for x in arr[::-1]:
    m -= x - 1
    ans *= m
    ans %= div
ans *= power(m, div - 2) * (m - n)
ans %= div
print(ans)
