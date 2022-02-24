# 1753 최단경로
# 다익스트라 알고리즘. 뭐 특별한 건 줄 알았는데 점 하나에 대해서만 진행하는 거 같다.
# 그냥 플로이드 와샬 쓰는게 낫지 않나? => 플로이드 와샬은 모든 점에 대해서 진행해야하네...

from sys import stdin as s
from math import inf
import heapq

v, e = map(int, s.readline().split())
init = int(s.readline())
connection = [[] for _ in range(v + 1)]
for _ in range(e):
    x, y, z = map(int, s.readline().split())
    connection[x].append((z, y))
d = [inf] * (v + 1)
d[init] = 0
heap = []
heapq.heappush(heap, (0, init))
while heap:
    # 갱신된 노드 중 가장 가까운 놈 / 이걸 위해 힙구조 사용
    distance, now = heapq.heappop(heap)
    if d[now] < distance:
        continue
    for cd, cy in connection[now]:
        if d[cy] > d[now] + cd:
            d[cy] = d[now] + cd
            heapq.heappush(heap, (d[cy], cy))
for i in range(1, v + 1):
    if d[i] == inf:
        print("INF")
    else:
        print(d[i])
