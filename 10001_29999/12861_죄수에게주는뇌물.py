from sys import stdin

input = stdin.readline


def sol(start, end):
    if start + 1 == end:
        return 0
    if dp[start][end] >= 0:
        return dp[start][end]
    ans = int(1e9)
    for i in range(start + 1, end):
        ans = min(ans, sol(start, i) + sol(i, end) + t[end] - t[start] - 2)
    dp[start][end] = ans
    return ans


n, m = map(int, input().split())
t = list(map(int, input().split()))
t.sort()
t = [0] + t + [n + 1]
dp = [[-1] * (m + 2) for _ in range(m + 2)]
print(sol(0, m + 1))
