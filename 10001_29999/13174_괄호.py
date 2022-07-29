def power(a, b):
    res = 1
    while b > 0:
        if b % 2:
            res *= a
            res %= div
        a *= a
        a %= div
        b //= 2
    return res


n, k = map(int, input().split())
ans = 1
div = 10 ** 9 + 7
factor = 1
for i in range(1, n + 1):
    ans *= k + 1
    if i % 2:
        if i > 1:
            r = i // 2 - 1
            factor *= k
            factor *= (4 * r + 2)
            factor *= power(r + 2, div - 2)
            factor %= div
        ans -= factor
    ans %= div
print(ans)
