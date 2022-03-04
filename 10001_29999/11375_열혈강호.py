from sys import stdin as s
from sys import setrecursionlimit as st

input = s.readline
st(10 ** 4)


def dfs(start):
    for adj in graph[start]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == 0 or dfs(match[adj]):
            match[adj] = start
            return True
    return False


n, m = map(int, input().split())
graph = [[]]
for j in range(1, n + 1):
    a = input()
    if a == '0\n':
        graph.append([])
        continue
    graph.append(list(map(int, a.split()))[1:])
match = [0] * (m + 1)
for i in range(1, n + 1):
    visited = [False] * (m + 1)
    dfs(i)
print(sum([1 for j in match if j > 0]))
