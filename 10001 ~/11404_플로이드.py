# 11404 플로이드 와샬
# 이번엔 간선에 비중이 있음 -> 전형적인 플로이드 와샬 문제

from sys import stdin as s

n = int(s.readline())
m = int(s.readline())
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    x, y, m = map(int, s.readline().split())
    if graph[x - 1][y - 1] == 0:
        graph[x - 1][y - 1] = m
    else:
        graph[x - 1][y - 1] = min(graph[x - 1][y - 1], m)
for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] and graph[i][k] and j != k:
                if graph[j][k] == 0:
                    graph[j][k] = graph[j][i] + graph[i][k]
                else:
                    graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
for p in graph:
    print(*p)