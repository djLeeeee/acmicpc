from sys import stdin

input = stdin.readline


def f(i, j):
    if i <= 0:
        dp[i][j] = 0
        return 0
    if dp[i][j] > -1:
        return dp[i][j]
    result = 1
    for bit in range(10):
        if (1 << bit) & j:
            result &= f(i - bit - 1, j - (1 << bit))
    dp[i][j] = result ^ 1
    return dp[i][j]


dp = [[-1] * 1024 for _ in range(65)]
ans = ''
for _ in range(int(input())):
    a, b, k = map(int, input().split())
    s = (k * k + k) // 2
    x, y = (b - a) // s, (b - a) % s
    if k % 2 and x % 2:
        if not f(y, (1 << k) - 1):
            ans += 'swoon\n'
        else:
            ans += 'raararaara\n'
    else:
        if f(y, (1 << k) - 1):
            ans += 'swoon\n'
        else:
            ans += 'raararaara\n'
print(ans.rstrip())
