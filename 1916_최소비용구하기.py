from sys import stdin as s
from math import inf
import heapq

n = int(s.readline())
m = int(s.readline())
connection = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, cost = map(int, s.readline().split())
    connection[x].append((cost, y))
init, fin = map(int, s.readline().split())
d = [inf] * (n + 1)
d[init] = 0
heap = []
heapq.heappush(heap, (0, init))
while heap:
    cost, point = heapq.heappop(heap)
    if d[point] < cost:  # 이 if 문이 있어야 코드 통과함
        continue         # 의미: 다른 곳을 보는 사이에 이미 힙에 저장된 것보다 짧은 경로를 찾음
    for i in connection[point]:
        if d[i[1]] > d[point] + i[0]:
            d[i[1]] = d[point] + i[0]
            heapq.heappush(heap, (d[i[1]], i[1]))
print(d[fin])
