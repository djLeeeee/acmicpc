from sys import stdin

input = stdin.readline

n = int(input())
tower = [0] + list(map(int, input().split()))
m = sum(tower) // 2 + 1
dp = [-1] * (m + 1)
dp[0] = 0
for i in range(1, n + 1):
    new_dp = [-1] * (m + 1)
    h = tower[i]
    if h > m:
        continue
    new_dp[0] = 0
    if dp[h] != -1:
        new_dp[0] = dp[h]
    if dp[0] > 0:
        new_dp[0] = max(new_dp[0], dp[0])
    for j in range(1, m + 1):
        now = dp[j]
        if j >= h and dp[j - h] != -1:
            if now < dp[j - h] + h:
                now = dp[j - h] + h
        if j <= h and dp[h - j] != -1:
            if now < dp[h - j] + j:
                now = dp[h - j] + j
        if j + h <= m and dp[j + h] != -1:
            if now < dp[j + h]:
                now = dp[j + h]
        new_dp[j] = now
    dp = new_dp
if dp[0] != 0:
    print(dp[0])
else:
    print(-1)
