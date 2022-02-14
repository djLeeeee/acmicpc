# 11401 이항계수3
# 페르마의 소정리
# For prime p which does not divide x, x^(p-1) = 1 mod p

from sys import stdin as s

p = 1000000007


def power(a, b):
    if b == 0:
        return 1
    if b % 2:
        return ((power(a, b // 2) ** 2) * a) % p
    else:
        return (power(a, b // 2) ** 2) % p


n, k = map(int, s.readline().split())
factorial = [1] * (n + 1)
for i in range(2, n + 1):
    factorial[i] = (factorial[i - 1] * i) % p
print((factorial[n] % p) * (power(factorial[k] * factorial[n - k], p - 2) % p) % p)
