from sys import stdin
from collections import defaultdict
import heapq

input = stdin.readline


def find(target, sqrt):
    init = 1
    fin = target
    while init <= fin:
        middle = (init + fin) // 2
        if middle ** sqrt >= target:
            ans = middle
            fin = middle - 1
        else:
            init = middle + 1
    return ans


n = int(input())
start = [(0, n), (n - 1, 1)]
dist = defaultdict(int)
dist[1] = n - 1
while start:
    cnt, now = heapq.heappop(start)
    if dist[now] < cnt:
        continue
    if now == 1:
        break
    for div in range(2, 63):
        x = find(now, div)
        cost1 = (now - (x - 1) ** div) + 1
        cost2 = (x ** div - now) + 1
        if cost1 > cost2:
            if dist[x] == 0 or dist[x] > cnt + cost2:
                dist[x] = cnt + cost2
                heapq.heappush(start, (dist[x], x))
        else:
            if dist[x - 1] == 0 or dist[x - 1] > cnt + cost1:
                dist[x - 1] = cnt + cost1
                heapq.heappush(start, (dist[x - 1], x - 1))
    if dist[1] > cnt + now - 1:
        dist[1] = cnt + now - 1
        heapq.heappush(start, (dist[1], 1))
print(cnt)
