from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(2 * 10 ** 4)


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n = int(input())
x = set()
y = set()
graph = [[] for _ in range(501)]
for _ in range(n):
    a, b = map(int, input().split())
    x.add(a)
    y.add(b)
    graph[a].append(b)
if len(x) != len(y):
    print('Mirko')
    exit()
match = [0] * 501
ans = 'Slavko'
for i in x:
    visited = [False] * 501
    if not dfs(i):
        ans = 'Mirko'
        break
print(ans)
