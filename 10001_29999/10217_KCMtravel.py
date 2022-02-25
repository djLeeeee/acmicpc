# 10217 KCM Travel
# 2차원 DP

from sys import stdin as s

input = s.readline
INF = int(1e9)
for _ in range(int(input())):
    n, m, t = map(int, input().split())
    connection = [[] for _ in range(n + 1)]
    # dist[도착지점][사용한 돈] = 걸린 시간
    dist = [[INF] * (m + 1) for _ in range(n + 1)]
    dist[1][0] = 0
    for _ in range(t):
        x, y, c, d = map(int, input().split())
        connection[x].append((d, c, y))
    for cost in range(m + 1):
        for now in range(1, n + 1):
            if dist[now][cost] == INF:
                continue
            for nd, nc, ny in connection[now]:
                if cost + nc <= m:
                    dist[ny][cost + nc] = min(
                        dist[ny][cost + nc],
                        dist[now][cost] + nd
                    )
    result = min(dist[n])
    if result == INF:
        print('Poor KCM')
    else:
        print(result)
