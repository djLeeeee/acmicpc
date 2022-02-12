# 1939 중량제한
# 이렇게 어려운데 골4???
# 그냥 파인드-유니온으로 품
# 파인드 유니온은 전설이다...

from sys import stdin as s
import heapq

n, m = map(int, s.readline().split())
parents = list(range(n + 1))


def find(target):
    if target == parents[target]:
        return target
    parents[target] = find(parents[target])
    return parents[target]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    return


connection = []
for _ in range(m):
    x, y, d = map(int, s.readline().split())
    heapq.heappush(connection, (-d, x, y))
init, fin = map(int, s.readline().split())
while find(init) != find(fin):
    distance, a, b = heapq.heappop(connection)
    union(a, b)
print(-distance)
