from sys import stdin

input = stdin.readline


def dist(p1, p2):
    res = 0
    for i in range(3):
        res += abs(p1[i] - p2[i])
    return res


def dfs(idx):
    for adj in graph[idx]:
        if not visited[adj]:
            visited[adj] = True
            if not match[adj] or dfs(match[adj]):
                match[adj] = idx
                return 1
    return 0


n = int(input())
bn = 0
wn = 0
black = {}
white = {}
for _ in range(n):
    x, y, z = map(int, input().split())
    if (x + y + z) % 2:
        bn += 1
        black[(x, y, z)] = bn
    else:
        wn += 1
        white[(x, y, z)] = wn
graph = [[] for _ in range(bn + 1)]
cnt = [1] * (bn + wn + 1)
for bk, bv in black.items():
    for wk, wv in white.items():
        if dist(bk, wk) == 1:
            graph[bv].append(wv)
            cnt[bv] = 0
            cnt[-wv] = 0
match = [0] * (wn + 1)
ans = sum(cnt) - 1
for i in range(1, bn + 1):
    visited = [False] * (wn + 1)
    ans += dfs(i)
print(ans)
