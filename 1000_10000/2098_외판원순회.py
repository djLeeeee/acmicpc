# 2098 외판원 순회
# DP + 비트마스킹
# 3월 12일 TIL 참고
from sys import stdin as s

input = s.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (1 << n - 1) for _ in range(n)]
INF = int(1e9)


def tour(now, path):
    if dp[now][path]:
        return dp[now][path]
    if path + 1 == 1 << n - 1:
        if costs[now][0]:
            return costs[now][0]
        return INF
    result = INF
    for adj in range(1, n):
        if not costs[now][adj]:
            continue
        if path & 1 << adj - 1:
            continue
        total = costs[now][adj] + tour(adj, path | 1 << (adj - 1))
        result = min(result, total)
    dp[now][path] = result
    return result


print(tour(0, 0))
