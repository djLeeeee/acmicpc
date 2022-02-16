# 1328 고층 빌딩
# dp 문제긴 한데... 이딴 게 플레??

n, l, r = map(int, input().split())
dp = [[0] * (r + 1) for _ in range(l + 1)]
dp[1][1] = 1
for i in range(2, n + 1):
    new_dp = [[0] * (r + 1) for _ in range(l + 1)]
    for j in range(1, l + 1):
        for k in range(1, r + 1):
            new_dp[j][k] = dp[j - 1][k] + dp[j][k - 1] + dp[j][k] * (i - 2)
            new_dp[j][k] %= 1000000007
    dp = new_dp[:]
print(dp[l][r])
