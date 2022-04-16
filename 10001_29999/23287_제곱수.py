from sys import stdin

input = stdin.readline


def prime_list(n):
    check = [1] * (n + 1)
    check[0] = 0
    check[1] = 0
    result = set()
    for i in range(2, n + 1):
        if check[i] == 1:
            result.add(i)
            for j in range(2 * i, n + 1, i):
                check[j] = 0
    return result


prime = prime_list(10 ** 5)
m = int(input())
stack = [1]
for p in prime:
    while m % p == 0:
        stack.append(p)
        m //= p
    if m == 1:
        break
ans = [0, 0, 0, 1]
M = max(stack)
sol = [[1] * 5 for _ in range(M + 1)]
sol[0] = []
for i in range(1, M + 1):
    j = 1
    while j * j <= i:
        if len(sol[i]) > len(sol[i - j * j]) + 1:
            sol[i] = sol[i - j * j] + [j]
            break
        j += 1
while stack:
    a = sol[stack.pop()] + [0] * 3
    b1 = abs(+a[0] * ans[0] - a[1] * ans[2] - a[2] * ans[3] - a[3] * ans[1])
    b2 = abs(-a[0] * ans[3] + a[1] * ans[1] - a[2] * ans[0] - a[3] * ans[2])
    b3 = abs(-a[0] * ans[1] - a[1] * ans[3] + a[2] * ans[2] - a[3] * ans[0])
    b4 = abs(-a[0] * ans[2] - a[1] * ans[0] - a[2] * ans[1] + a[3] * ans[3])
    ans = [b1, b2, b3, b4]
print(*ans)
