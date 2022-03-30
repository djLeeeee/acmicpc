from sys import stdin, setrecursionlimit
from collections import defaultdict

input = stdin.readline
setrecursionlimit(10 ** 6)


def new_idx(idx, direction):
    if direction <= 1:
        return 2 * idx - direction
    return - 2 * idx + (direction - 2)


def draw_edge(nums):
    l = len(nums)
    for a in range(l - 1):
        for b in range(a + 1, l):
            graph[nums[a]].append(-nums[b])
            graph[nums[b]].append(-nums[a])
    return True


def dfs(idx):
    if visited[idx]:
        return
    visited[idx] = True
    for adj in graph[idx]:
        if not visited[adj]:
            dfs(adj)
    stack.append(idx)


def dfs_inv(idx):
    global flag2
    if scc[idx]:
        return
    scc[idx] = component
    if scc[idx] == scc[-idx]:
        flag2 = False
        return
    for adj in graph[-idx]:
        if not scc[-adj]:
            dfs_inv(-adj)


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for _ in range(int(input())):
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    bn = 0
    wn = 0
    nw = []
    flag = True
    white = defaultdict(list)
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'B':
                bn += 1
                board[i][j] = bn
                cnt = 0
                for d in range(4):
                    ni = i + dx[d]
                    nj = j + dy[d]
                    nn = new_idx(board[i][j], d)
                    if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 'W':
                        cnt += 1
                        white[(ni, nj)].append(nn)
                    else:
                        nw.append(nn)
                if cnt < 2:
                    flag = False
            elif board[i][j] == 'W':
                wn += 1
    if bn * 2 != wn or not flag:
        print('NO')
        continue
    graph = [[] for _ in range(4 * bn + 1)]
    for k in nw:
        graph[k].append(-k)
    for value in white.values():
        draw_edge(value)
    del white
    stack = []
    visited = [False] * (4 * bn + 1)
    for i in range(1, 2 * bn + 1):
        if not visited[i]:
            dfs(i)
        if not visited[-i]:
            dfs(-i)
    scc = [0] * (4 * bn + 1)
    component = 0
    flag2 = True
    while stack and flag2:
        now = stack.pop()
        if not scc[now]:
            component += 1
            dfs_inv(now)
    if flag2:
        print('YES')
    else:
        print('NO')
