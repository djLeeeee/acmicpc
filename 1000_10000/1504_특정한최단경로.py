# 1504 최단 경로
# 다익스트라 3번 쓰는 풀이가 맞나???
# 일단 진행해 봄.

from sys import stdin as s
from math import inf
import heapq

n, e = map(int, s.readline().split())
connection = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(e):
    x, y, cost = map(int, s.readline().split())
    connection[x][y] = cost
    connection[y][x] = cost
mid1, mid2 = map(int, s.readline().split())
nodes = [1, mid1, mid2, n]
nodes2 = [mid2, n, mid1]
total2 = 0
total = 0
for j in range(3):
    heap = [(0, nodes[j])]
    ans = [inf] * (n + 1)
    ans[nodes[j]] = 0
    while heap:
        cost, now = heapq.heappop(heap)
        if cost > ans[now]:
            continue
        for k in range(1, n + 1):
            if connection[now][k] != 0:
                if ans[k] > connection[now][k] + cost:
                    ans[k] = connection[now][k] + cost
                    heapq.heappush(heap, (ans[k], k))
    total += ans[nodes[j + 1]]
    total2 += ans[nodes2[j]]
total = min(total, total2)
if total == inf:
    print(-1)
else:
    print(total)
