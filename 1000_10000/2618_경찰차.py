# 2618 경찰차
# 2차원 DP
# dp[i][j] : 1번 경찰차 마지막 처리한 일이 i번, 2번 경찰차 j번
# 그때 걸린 시간을 저장

from sys import stdin as s
from sys import setrecursionlimit as st
st(10 ** 6)

input = s.readline

INF = int(1e9)
n = int(input())
m = int(input())
x = [0] * (m + 1)
y = [0] * (m + 1)
for i in range(1, m + 1):
    x[i], y[i] = map(int, input().split())
dp = [[INF] * (m + 1) for _ in range(m + 1)]
dp[0][1] = 2 * n - x[1] - y[1]
dp[1][0] = x[1] + y[1] - 2
for j in range(2, m + 1):
    d = abs(x[j] - x[j - 1]) + abs(y[j] - y[j - 1])
    for k in range(j - 1):
        dp[k][j] = dp[k][j - 1] + d
        dp[j][k] = dp[j - 1][k] + d
    dp[j][j - 1] = dp[0][j - 1] + x[j] + y[j] - 2
    dp[j - 1][j] = dp[j - 1][0] + 2 * n - x[j] - y[j]
    for p in range(1, j - 1):
        dd = abs(x[j] - x[p]) + abs(y[j] - y[p])
        dp[j - 1][j] = min(dp[j - 1][j], dp[j - 1][p] + dd)
        dp[j][j - 1] = min(dp[j][j - 1], dp[p][j - 1] + dd)


def trace(p1, p2):
    # print(p1, p2)
    if p1 == 0:
        return '2' * p2
    if p2 == 0:
        return '1' * p1
    if p1 > p2 + 1:
        return trace(p2 + 1, p2) + '1' * (p1 - p2 - 1)
    if p2 > p1 + 1:
        return trace(p1, p1 + 1) + '2' * (p2 - p1 - 1)
    if p1 == p2 + 1:
        if dp[0][p2] + x[p1] + y[p1] - 2 == dp[p1][p2]:
            return trace(0, p2) + '1'
        for idx in range(1, p2):
            ex = abs(x[p1] - x[idx]) + abs(y[p1] - y[idx])
            if dp[idx][p2] + ex == dp[p1][p2]:
                return trace(idx, p2) + '1'
    if dp[p1][0] + 2 * n - x[p2] - y[p2] == dp[p1][p2]:
        return trace(p1, 0) + '2'
    for idx in range(1, p1):
        ex = abs(x[p2] - x[idx]) + abs(y[p2] - y[idx])
        if dp[p1][idx] + ex == dp[p1][p2]:
            return trace(p1, idx) + '2'


mini = INF
for i in range(m):
    if dp[i][m] < mini:
        mini = dp[i][m]
        a, b = i, m
    if dp[m][i] < mini:
        mini = dp[m][i]
        a, b = m, i

print(mini)
for i in trace(a, b):
    print(i)
