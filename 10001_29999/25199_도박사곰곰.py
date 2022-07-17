from collections import defaultdict

div = 10 ** 9 + 7
n, m = map(int, input().split())
cnt = [0] * (m + 1)
for num in map(int, input().split()):
    cnt[num] += 1
y = max(cnt)
for i in range(m, 0, -1):
    if cnt[i] == y:
        x = i
        break
dp = [defaultdict(int) for _ in range(m + 1)]
for i in range(n + 1):
    dp[0][i] = 1
for i in range(1, x):
    for j in range(n + 1):
        dp[i][j] = dp[i - 1][j] - dp[i - 1][j - y - 1]
    for j in range(n + 1):
        dp[i][j] += dp[i][j - 1]
        dp[i][j] %= div
for i in range(x, m + 1):
    for j in range(n + 1):
        dp[i][j] = dp[i - 1][j] - dp[i - 1][j - y]
    for j in range(n + 1):
        dp[i][j] += dp[i][j - 1]
        dp[i][j] %= div
print((dp[m][n] - dp[m][n - 1]) % div)
