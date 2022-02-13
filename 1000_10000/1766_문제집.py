# 1766 문제집 / 위상정렬 + 힙 구조
# 오늘의 찐막
# heap이랑 deque을 둘다 써야 할 듯?

from sys import stdin as s
from collections import deque
import heapq

n, m = map(int, s.readline().split())
connection = [[] for _ in range(n + 1)]
get_in = [0] * (n + 1)
parents = [ ]
result = [ ]
for _ in range(m):
    x, y = map(int, s.readline().split())
    connection[x].append(y)
    get_in[y] += 1
for i in range(1, n + 1):
    if get_in[i] == 0:
        heapq.heappush(parents, i)

while parents:
    a = heapq.heappop(parents)
    result.append(a)
    for j in connection[a]:
        get_in[j] -= 1
        if get_in[j] == 0:
            heapq.heappush(parents, j)
print(*result)