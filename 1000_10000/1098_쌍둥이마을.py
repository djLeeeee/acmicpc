from sys import stdin

input = stdin.readline


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


n = int(input())
town = [tuple(map(int, input().split())) for _ in range(n)]
p, d = map(int, input().split())
graph = []
for i in range(n - 1):
    for j in range(i + 1, n):
        if dist(town[i], town[j]) >= d:
            graph.append((dist(town[i], town[j]), 2 * i, 2 * j))
t = 1 << 2 * n
dp = [0] * t
dp[0] = [0, 0]
ans = [0, 0]
for d, x, y in graph:
    for i in range(t - 1, -1, -1):
        if dp[i] and (i >> x) & 3 < p and (i >> y) & 3 < p:
            j = i + (1 << x) + (1 << y)
            if dp[j]:
                if dp[j][0] < dp[i][0] + 1:
                    dp[j] = [dp[i][0] + 1, dp[i][1] + d]
                elif dp[j][0] == dp[i][0] + 1:
                    dp[j][1] = min(dp[j][1], dp[i][1] + d)
            else:
                dp[j] = [dp[i][0] + 1, dp[i][1] + d]
            if ans[0] < dp[j][0]:
                ans = dp[j][:]
            elif ans[0] == dp[j][0]:
                ans[1] = min(ans[1], dp[j][1])
print(*ans)
