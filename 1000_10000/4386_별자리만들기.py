from sys import stdin
from sys import setrecursionlimit as st
import heapq

st(10 ** 6)
input = stdin.readline

n = int(input())
p = list(range(n))


def get_dist(p1: tuple, p2: tuple) -> float:
    result = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    return result ** 0.5


def find(t: int) -> int:
    if t == p[t]:
        return t
    p[t] = find(p[t])
    return p[t]


def union(a: int, b: int) -> None:
    a = find(a)
    b = find(b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


point = []
dist = []
for _ in range(n):
    x, y = map(float, input().split())
    point.append((x, y))
for i in range(n - 1):
    for j in range(i + 1, n):
        dist.append((get_dist(point[i], point[j]), i, j))
heapq.heapify(dist)
edge = 0
ans = 0
while edge < n - 1:
    d, xx, yy = heapq.heappop(dist)
    if find(xx) != find(yy):
        ans += d
        union(xx, yy)
        edge += 1
print('{:.2f}'.format(ans))
