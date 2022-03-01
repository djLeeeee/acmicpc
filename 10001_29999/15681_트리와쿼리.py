# 15681 트리와 쿼리
# 올 것이 왔구나...
# 차근차근
from collections import deque
from sys import stdin as s

input = s.readline

n, r, q = map(int, input().split())
connection = [[] for _ in range(n + 1)]
get_in = [0] * (n + 1)
child = [1] * (n + 1)
visited = [False] * (n + 1)
for _ in range(n - 1):
    x, y = map(int, input().split())
    connection[x].append(y)
    connection[y].append(x)
    get_in[x] += 1
    get_in[y] += 1
leaves = deque()
for i in range(1, n + 1):
    if get_in[i] == 1 and i != r:
        leaves.append(i)
while leaves:
    now = leaves.popleft()
    visited[now] = True
    for can_go in connection[now]:
        get_in[can_go] -= 1
        if get_in[can_go] == 1 and can_go != r:
            leaves.append(can_go)
        if not visited[can_go]:
            child[can_go] += child[now]
for j in range(q):
    print(child[int(input())])
