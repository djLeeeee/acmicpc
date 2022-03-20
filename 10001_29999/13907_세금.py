from sys import stdin
from collections import defaultdict
import heapq

input = stdin.readline
INF = float('inf')


def dijkstra(start, end):
    dist = [[INF] * n for _ in range(n + 1)]
    dist[start][0] = 0
    heap = [(0, start, 0)]
    flag = True
    limit = n - 1
    while heap:
        c, now, road = heapq.heappop(heap)
        if flag and now == end:
            limit = road
            flag = False
        if dist[now][road] < c or road >= limit:
            continue
        for adj, dd in graph[now].items():
            if dist[adj][road + 1] > dist[now][road] + dd:
                dist[adj][road + 1] = dist[now][road] + dd
                heapq.heappush(heap, (dist[adj][road + 1], adj, road + 1))
    return dist[end][:limit + 1]


n, m, k = map(int, input().split())
s, e = map(int, input().split())
graph = defaultdict(dict)
for _ in range(m):
    x, y, d = map(int, input().split())
    graph[x][y] = d
    graph[y][x] = d
ex = 0
table = dijkstra(s, e)
length = len(table)
print(table[-1])
for _ in range(k):
    extra = int(input())
    ans = INF
    for i in range(1, length):
        table[i] += extra * i
        if table[i] < ans:
            ans = table[i]
            k = i + 1
    length = k
    print(ans)
