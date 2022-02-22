from sys import stdin as s

n, k, m = map(int, s.readline().split())


def power(p, q):
    x = 1
    while q > 0:
        if q & 1:
            x = (x * p) % m
        q >>= 1
        p = (p * p) % m
    return x


a = []
b = []
while n > 0 and k > 0:
    a.append(n % m)
    b.append(k % m)
    n //= m
    k //= m

factorial = [1] * m
inverse = [1] * m
for i in range(2, m):
    factorial[i] = (factorial[i - 1] * i) % m
    inverse[i] = power(factorial[i], m - 2) % m

l = len(a)
ans = 1
for j in range(l):
    if a[j] >= b[j]:
        ans *= (factorial[a[j]] * inverse[b[j]] * inverse[a[j] - b[j]])
    else:
        ans = 0
        break
    ans %= m
print(ans)
