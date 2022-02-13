# 1261 알고스팟
# 재밌어보임

from sys import stdin as s
from math import inf
import heapq

input = s.readline
m, n = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
labyrinth = []
for i in range(n):
    labyrinth.append(list(map(int, input().rstrip())))
d = [[inf] * m for _ in range(n)]
d[0][0] = 0
heap = []
heapq.heappush(heap, (0, 0, 0))
while heap:
    cost, x, y = heapq.heappop(heap)
    if cost > d[x][y]:
        continue
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if 0 <= nx < n and 0 <= ny < m and d[nx][ny] > cost + labyrinth[nx][ny]:
            d[nx][ny] = cost + labyrinth[nx][ny]
            heapq.heappush(heap, (d[nx][ny], nx, ny))
print(d[-1][-1])
