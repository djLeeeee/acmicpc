from sys import stdin as s
from math import inf

n = int(s.readline())
rc = [list(map(int, s.readline().split())) for _ in range(n)]
dp = [[inf] * n for _ in range(n)]
dp[0][0] = 0
for i in range(1, n):
    dp[i][i] = 0
    dp[i - 1][i] = rc[i - 1][0] * rc[i][0] * rc[i][1]
for length in range(2, n):
    for start in range(n - length):
        end = start + length
        for middle in range(start, end):
            dp[start][end] = min(
                dp[start][end],
                dp[start][middle] + dp[middle + 1][end]
                + rc[start][0] * rc[middle][1] * rc[end][1]
            )
print(dp[0][-1])