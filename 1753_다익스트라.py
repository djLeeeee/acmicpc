# 1753 최단경로
# 다익스트라 알고리즘. 뭐 특별한 건 줄 알았는데 점 하나에 대해서만 진행하는 거 같다.
# 그냥 플로이드 와샬 쓰는게 낫지 않나? => 플로이드 와샬은 모든 점에 대해서 진행해야하네...

from sys import stdin as s
import heapq
from math import inf

v, e = map(int, s.readline().split())
init = int(s.readline())
connection = [[] * (v + 1) for _ in range(v + 1)]
d = [inf] * (v + 1)
d[init] = 0
for _ in range(e):
    x, y, m = map(int, s.readline().split())
    connection[x].append((y, m))

heap = []
heapq.heappush(heap, (0, init))
while heap:
    now = heapq.heappop(heap)  # 갱신된 노드 중 가장 가까운 놈 / 이걸 위해 힙구조 사용
    for i in connection[now[1]]:
        if i[1] + now[0] < d[i[0]]:
            d[i[0]] = i[1] + now[0]
            heapq.heappush(heap, (d[i[0]], i[0]))

for i in range(1, v + 1):
    if d[i] == inf:
        print("INF")
    else:
        print(d[i])
