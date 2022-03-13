# 13308 주유소
# dp는 재밌엉~~
from sys import stdin
import heapq

input = stdin.readline

n, m = map(int, input().split())
oil_rate = [0] + list(map(int, input().split()))
graph = {}
for _ in range(m):
    x, y, d = map(int, input().split())
    if graph.get(x):
        graph[x][y] = d
    else:
        graph[x] = {y: d}
    if graph.get(y):
        graph[y][x] = d
    else:
        graph[y] = {x: d}
INF = float('inf')
ans = [[INF] * 2501 for _ in range(n + 1)]
check = [[] for _ in range(n + 1)]
starts = [(0, oil_rate[1], 1)]
while starts:
    total, oil, now = heapq.heappop(starts)
    if now == n:
        break
    if total > ans[now][oil]:
        continue
    oil = min(oil, oil_rate[now])
    for adj in graph[now]:
        if oil * graph[now][adj] + total < ans[adj][oil]:
            ans[adj][oil] = oil * graph[now][adj] + total
            heapq.heappush(starts, (ans[adj][oil], oil, adj))
print(total)
