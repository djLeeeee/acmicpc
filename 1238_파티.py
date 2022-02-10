# 1238 파티
# 다익스트라와 이제 좀 친해진 듯

from sys import stdin as s
from math import inf
import heapq

n, m, party = map(int, s.readline().split())
connection1 = [[] for _ in range(n + 1)]
connection2 = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, cost = map(int, s.readline().split())
    connection1[x].append((cost, y))
    connection2[y].append((cost, x))
d1 = [inf] * (n + 1)
d1[party] = 0
d2 = [inf] * (n + 1)
d2[party] = 0
heap1 = []
heapq.heappush(heap1, (0, party))
heap2 = []
heapq.heappush(heap2, (0, party))
while heap1:
    cost, point = heapq.heappop(heap1)
    if d1[point] < cost:
        continue
    for i in connection1[point]:
        if d1[i[1]] > i[0] + d1[point]:
            d1[i[1]] = i[0] + d1[point]
            heapq.heappush(heap1, (d1[i[1]], i[1]))
while heap2:
    cost, point = heapq.heappop(heap2)
    if d2[point] < cost:
        continue
    for i in connection2[point]:
        if d2[i[1]] > i[0] + d2[point]:
            d2[i[1]] = i[0] + d2[point]
            heapq.heappush(heap2, (d2[i[1]], i[1]))
d = [d1[i] + d2[i] for i in range(1, n + 1)]
print(max(d))