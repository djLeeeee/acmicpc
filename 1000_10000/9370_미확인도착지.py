# 9370 미확인 도착지
# 간만에 골2 문제
# check 변수 확인을 잘못해 계속 헤맸다... new_check 를 선언해 해결
# 다익스트라 시러

from sys import stdin as s
from math import inf
import heapq

for _ in range(int(s.readline())):
    n, m, t = map(int, s.readline().split())
    start, g, h = map(int, s.readline().split())
    connection = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, s.readline().split())
        connection[a][b] = d
        connection[b][a] = d
    arrivals = [int(s.readline()) for _ in range(t)]
    target = {(g, h), (h, g)}
    passed = [False] * (n + 1)
    distance = [inf] * (n + 1)
    distance[start] = 0
    heap = [(0, start, False)]
    while heap:
        cost, now, check = heapq.heappop(heap)
        if distance[now] < cost:
            continue
        for i in range(1, n + 1):
            new_check = check
            if (now, i) in target:
                new_check = True
            if connection[now][i] != 0:
                if connection[now][i] + cost < distance[i]:
                    passed[i] = new_check
                    distance[i] = connection[now][i] + cost
                    heapq.heappush(heap, (distance[i], i, new_check))
                elif connection[now][i] + cost == distance[i]:
                    if new_check and not passed[i]:
                        passed[i] = True
                        heapq.heappush(heap, (distance[i], i, True))
    result = []
    for arrival in arrivals:
        if passed[arrival]:
            result.append(arrival)
    result.sort()
    print(*result)
