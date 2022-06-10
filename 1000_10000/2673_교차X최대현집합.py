from sys import stdin

input = stdin.readline

n = int(input())
line = [[0] * 101 for _ in range(101)]
for _ in range(n):
    s, e = map(int, input().split())
    line[s][e] = 1
    line[e][s] = 1
dp = [[0] * 101 for _ in range(101)]
for i in range(1, 101):
    for j in range(i, 0, -1):
        for k in range(j, i):
            if dp[j][i] < dp[j][k] + dp[k][i] + line[i][j]:
                dp[j][i] = dp[j][k] + dp[k][i] + line[i][j]
print(dp[1][100])
