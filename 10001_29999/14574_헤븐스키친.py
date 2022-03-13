# 14574 헤븐스 키친
# n이 작아서 재귀 깊이 안 건드림
# 분리 집합 까먹을 뻔 ㄷㄷ
from sys import stdin

input = stdin.readline


def find(a):
    if p[a] == a:
        return a
    p[a] = find(p[a])
    return p[a]


def union(a, b):
    a = find(a)
    b = find(b)
    p[a] = b


n = int(input())
cook = [list(map(int, input().split())) for _ in range(n)]
p = list(range(n + 1))
rate = []
for i in range(n - 1):
    for j in range(i + 1, n):
        rate.append((int((cook[i][1] + cook[j][1]) / abs(cook[i][0] - cook[j][0])), i + 1, j + 1))
rate.sort()
graph = [[] for _ in range(n + 1)]
deg = [0] * (n + 1)
e = 0
ans = 0
while e < n - 1:
    r, x, y = rate.pop()
    if find(x) != find(y):
        ans += r
        e += 1
        union(x, y)
        graph[x].append(y)
        graph[y].append(x)
        deg[x] += 1
        deg[y] += 1
print(ans)
matches = []
leaves = [v for v in range(1, n + 1) if deg[v] == 1]
remain = [True] * (n + 1)
while leaves:
    leaf = leaves.pop()
    if not remain[leaf]:
        continue
    remain[leaf] = False
    for adj in graph[leaf]:
        if remain[adj]:
            matches.append((adj, leaf))
            deg[adj] -= 1
            if deg[adj] == 1:
                leaves.append(adj)
            break
for match in matches:
    print(*match)
