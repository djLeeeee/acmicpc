from sys import stdin
from collections import defaultdict

input = stdin.readline


def dfs(idx):
    for adj in graph[idx]:
        if visited[adj]:
            continue
        visited[adj] = True
        if match[adj] == 0 or dfs(match[adj]):
            match[adj] = idx
            return 1
    return 0


for _ in range(int(input())):
    n, m = map(int, input().split())
    p1 = 0
    p2 = 0
    board = []
    dx = [0, 0, -1, -1, 1, 1]
    dy = [-1, 1, -1, 1, -1, 1]
    for _ in range(n):
        line = list(input().strip())
        for i in range(m):
            if line[i] == '.':
                if i % 2:
                    p2 += 1
                    line[i] = p2
                else:
                    p1 += 1
                    line[i] = p1
            else:
                line[i] = 0
        board.append(line)
    if p1 == 0 or p2 == 0:
        print(p1 + p2)
        continue
    graph = defaultdict(list)
    for y in range(0, m, 2):
        for x in range(n):
            if board[x][y]:
                for d in range(6):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny]:
                        graph[board[x][y]].append(board[nx][ny])
    match = [0] * (p2 + 1)
    cover = 0
    for i in range(1, p1 + 1):
        visited = [False] * (p2 + 1)
        cover += dfs(i)
    print(p1 + p2 - cover)
