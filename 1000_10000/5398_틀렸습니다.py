from sys import stdin
from collections import defaultdict

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if not match[adj] or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


for _ in range(int(input())):
    n, m = map(int, input().split())
    board = defaultdict(dict)
    for rn in range(n):
        x, y, word = input().strip().split()
        x, y = int(x), int(y)
        l = len(word)
        for i in range(l):
            board[x + i][y] = (word[i], rn + 1)
    graph = [[] for _ in range(n + 1)]
    for cn in range(m):
        x, y, word = input().strip().split()
        x, y = int(x), int(y)
        l = len(word)
        for i in range(l):
            if y + i in board[x] and board[x][y + i][0] != word[i]:
                graph[board[x][y + i][1]].append(cn)
    ans = n + m
    match = [0] * (m + 1)
    for i in range(1, n + 1):
        visited = [False] * (m + 1)
        ans -= dfs(i)
    print(ans)
