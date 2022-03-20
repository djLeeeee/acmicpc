from sys import stdin, setrecursionlimit
from collections import defaultdict
import heapq


def trace(end):
    if end == s:
        return
    if visited[end]:
        return
    visited[end] = True
    for node, q in graph_inv[end].items():
        if dist[node] + q == dist[end]:
            del graph[node][end]
            if not visited[node]:
                trace(node)


input = stdin.readline
setrecursionlimit(10 ** 5)

INF = float('inf')
while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    s, e = map(int, input().split())
    graph = defaultdict(dict)
    graph_inv = defaultdict(dict)
    for _ in range(m):
        x, y, p = map(int, input().split())
        graph[x][y] = p
        graph_inv[y][x] = p
    dist = [INF] * n
    dist[s] = 0
    start = [(0, s)]
    while start:
        d, now = heapq.heappop(start)
        if now == e:
            break
        if dist[now] < d:
            continue
        for adj, ex in graph[now].items():
            if dist[now] + ex < dist[adj]:
                dist[adj] = dist[now] + ex
                heapq.heappush(start, (dist[adj], adj))
    if dist[e] == INF:
        print(-1)
    else:
        visited = [False] * n
        trace(e)
        del graph_inv
        start = [(0, s)]
        dist = [INF] * n
        dist[s] = 0
        while start:
            d, now = heapq.heappop(start)
            if now == e:
                break
            if dist[now] < d:
                continue
            for adj, ex in graph[now].items():
                if dist[now] + ex < dist[adj]:
                    dist[adj] = dist[now] + ex
                    heapq.heappush(start, (dist[adj], adj))
        ans = -1 if dist[e] == INF else dist[e]
        print(ans)
