# 2차원 dp 활용
# 메모리제이션인가 이게??
from sys import stdin as s
from sys import setrecursionlimit as st

st(10 ** 4)
input = s.readline


def pick(start, end):
    if dp[start][end]:
        return dp[start][end]
    if start + 2 == end:
        dp[start][end] = sum(score[start:end + 1])
        return dp[start][end]
    if start + 2 > end:
        return 0
    result = 0
    for i in range(start + 1, end):
        result = max(result, pick(start, i) + pick(i, end) + score[start] + score[i] + score[end])
    dp[start][end] = result
    return dp[start][end]


while True:
    a = input()
    if a == '0\n':
        break
    n, *score = list(map(int, a.split()))
    dp = [[0] * n for _ in range(n)]
    print(pick(0, n - 1))
