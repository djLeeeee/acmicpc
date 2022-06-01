from sys import stdin, setrecursionlimit
from collections import defaultdict, deque

input = stdin.readline
setrecursionlimit(2 * 10 ** 5)
INF = float('inf')


def bfs():
    stack = deque()
    for x in nodes:
        if not used[x]:
            stack.append(x)
            dist[x] = 0
        else:
            dist[x] = INF
    while stack:
        now = stack.popleft()
        for adj in graph[now]:
            if match[adj] and dist[match[adj]] == INF:
                dist[match[adj]] = dist[now] + 1
                stack.append(match[adj])


def dfs(idx):
    for adj in graph[idx]:
        if not match[adj] or (dist[match[adj]] == dist[idx] + 1 and dfs(match[adj])):
            used[idx] = True
            match[adj] = idx
            return 1
    return 0


graph = defaultdict(set)
nodes = set()
for _ in range(int(input())):
    m, *algo = input().strip().split()
    m = int(m)
    algo.sort()
    if ''.join(algo) not in nodes:
        memo = [''] * (1 << m)
        for btmsk in range((1 << m) - 1, 0, -1):
            for bit in range(m):
                if btmsk & (1 << bit):
                    memo[btmsk] += algo[bit]
            nodes.add(memo[btmsk])
            for bit in range(m):
                if btmsk & (1 << bit) == 0:
                    graph[memo[btmsk]].add(memo[btmsk + (1 << bit)])
match = defaultdict(bool)
used = defaultdict(bool)
dist = defaultdict(int)
ans = len(nodes)
while True:
    bfs()
    flow = 0
    for node in nodes:
        if not used[node]:
            flow += dfs(node)
    if flow:
        ans -= flow
    else:
        break
print(ans)
