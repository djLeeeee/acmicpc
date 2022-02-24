"""
# 1. 나만의 벨만 포드(다익스트라 변형) -> 오답
# while 구문 탈출 조건을 좀만 손 봐주면 될 거 같은데...
import heapq
from sys import stdin as s
from math import inf

input = s.readline

n, m = map(int, input().split())
connection = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, c = map(int, input().split())
    connection[x].append((c, y))
d = [inf] * (n + 1)
d[1] = 0
start = []
heapq.heappush(start, (0, 1))
visited = [0] * (n + 1)
while start and max(visited) < n:
    cost, now = heapq.heappop(start)
    if cost > d[now]:
        continue
    visited[now] += 1
    for ex, go in connection[now]:
        if d[go] == inf:
            d[go] = ex + d[now]
            heapq.heappush(start, (d[go], go))
        else:
            if d[go] > ex + d[now]:
                d[go] = ex + d[now]
                heapq.heappush(start, (d[go], go))
    print(visited)
if start:
    print(-1)
else:
    for j in range(2, n + 1):
        if d[j] == inf:
            print('-1')
        else:
            print(d[j])


# 2. 플로이드 와샬
# 아마 답은 나오는 거 같은데, 역시 시간 초과
# 플로이드 와샬의 시간복잡도는 v^3이니까 당연.
from sys import stdin as s

input = s.readline

n, m = map(int, input().split())
connection = [[inf] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    connection[i][i] = 0
for _ in range(m):
    x, y, c = map(int, input().split())
    connection[x][y] = c
for j in range(1, n + 1):
    for i in range(1, n + 1):
        for k in range(1, n + 1):
            connection[i][k] = min(
                connection[i][k],
                connection[i][j] + connection[j][k]
            )
minus_cycle = False
for i in range(2, n + 1):
    if connection[1][i] + connection[i][1] < 0:
        minus_cycle = True
        break
if minus_cycle:
    print(-1)
else:
    for j in range(2, n + 1):
        if connection[1][j] == inf:
            print(-1)
        else:
            print(connection[1][j])


# 3. 기억을 더듬어 벨만포드 다시 짜보기
# 벨만 포드 찾다가 graph 를 딕셔너리로 표기하는 아주 멋진 아이디어를 봤다
# 예시) connection = {A: {B: 5, C: 3}} -> A에서 B까지 길이 5의 간선 존재
# 근데 이게 왜 틀림??
# 3시간 끝에 수정 완료... 통과함
# dist[now] != INF 이 부분 있고 없고 차이였음
from sys import stdin as s

input = s.readline

n, m = map(int, input().split())
INF = int(1e9)
connection = {}
for _ in range(m):
    x, y, c = map(int, input().split())
    if connection.get(x):
        if connection[x].get(y):
            if connection[x][y] > c:
                connection[x][y] = c
        else:
            connection[x][y] = c
    else:
        connection[x] = {y: c}
dist = [INF] * (n + 1)
dist[1] = 0
negative = False
for i in range(n):
    for now in connection:
        for can_go in connection[now]:
            if dist[now] != INF and dist[can_go] > dist[now] + connection[now][can_go]:
                dist[can_go] = dist[now] + connection[now][can_go]
                if i == n - 1:
                    negative = True
if negative:
    print('-1')
else:
    for j in range(2, n + 1):
        if dist[j] == INF:
            print('-1')
        else:
            print(dist[j])
"""

# 4. 벨만 포드 - 인터넷
# 도대체 3번 코드는 왜 안 되냐고...
import sys

input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
dist = [INF] * (n + 1)


def bellman_ford(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            now, can_go, cost = edges[j]
            if dist[now] != INF and dist[can_go] > dist[now] + cost:
                dist[can_go] = dist[now] + cost
                if i == n - 1:
                    return True
    return False


if bellman_ford(1):
    print('-1')
else:
    for k in range(2, n + 1):
        if dist[k] == INF:
            print('-1')
        else:
            print(dist[k])
