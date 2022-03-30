from sys import stdin, setrecursionlimit
from collections import defaultdict

input = stdin.readline
setrecursionlimit(10 ** 4)


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == 0 or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


n = int(input())
graph = [[] for _ in range(n + 1)]
result = [{} for _ in range(n + 1)]
ans = [[0] * 5 for _ in range(n + 1)]
for t in range(1, n + 1):
    a, b = map(int, input().split())
    ans[t][0] = a
    ans[t][2] = b
    ans[t][3] = '='
    graph[t] = [a + b, a - b, a * b]
    result[t] = {a + b: '+', a - b: '-', a * b: '*'}
match = defaultdict(int)
flag = True
for i in range(1, n + 1):
    visited = defaultdict(bool)
    if not dfs(i):
        flag = False
        break
if flag:
    for key, value in match.items():
        ans[value][4] = key
        ans[value][1] = result[value][key]
    for i in range(1, n + 1):
        print(*ans[i])
else:
    print('impossible')
