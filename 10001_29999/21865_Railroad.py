from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def draw_or_edge(x, y):
    graph[-x].append(y)
    graph[-y].append(x)


def draw_nor_edge(x, y):
    graph[x].append(-y)
    graph[y].append(-x)


def draw_xor_edge(x, y):
    graph[-x].append(y)
    graph[-y].append(x)
    graph[y].append(-x)
    graph[x].append(-y)


def draw_false_edge(x):
    graph[x].append(-x)


def dfs(idx):
    if visited[idx]:
        return
    visited[idx] = True
    for adj in graph[idx]:
        if not visited[adj]:
            dfs(adj)
    stack.append(idx)


def dfs_inv(idx):
    if scc[idx]:
        return
    scc[idx] = component
    if scc[idx] == scc[-idx]:
        print('NO')
        exit()
    for adj in graph[-idx]:
        if not scc[-adj]:
            dfs_inv(-adj)


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]
graph = [[] for _ in range(8 * n * m + 1)]
for i in range(n):
    for j in range(m):
        now = (m * i + j) * 4
        if board[i][j] == 'L':
            draw_xor_edge(now + 1, now + 3)
            draw_xor_edge(now + 2, now + 4)
        elif board[i][j] == 'X':
            for d in range(1, 5):
                draw_false_edge(now + d)
        elif board[i][j] == 'O':
            for ii in range(2, 5):
                for jj in range(1, ii):
                    draw_or_edge(now + ii, now + jj)
        else:
            draw_nor_edge(now + 1, now + 2)
            draw_nor_edge(now + 1, now + 4)
            draw_nor_edge(now + 3, now + 2)
            draw_nor_edge(now + 3, now + 4)
            draw_nor_edge(now + 1, -(now + 3))
            draw_nor_edge(now + 3, -(now + 1))
            draw_nor_edge(now + 2, -(now + 4))
            draw_nor_edge(now + 4, -(now + 2))
di = [0, -1, 0, 1, 0]
dj = [0, 0, -1, 0, 1]
trans = [0, 3, 4, 1, 2]
for i in range(n):
    for j in range(m):
        if board[i][j] != 'X':
            now = (m * i + j) * 4
            for d in range(1, 5):
                ni = i + di[d]
                nj = j + dj[d]
                nei = (m * ni + nj) * 4
                if 0 <= ni < n and 0 <= nj < m and board[ni][nj] != 'X':
                    draw_xor_edge(now + d, -(nei + trans[d]))
                else:
                    draw_false_edge(now + d)
stack = []
visited = [False] * (8 * m * n + 1)
for i in range(1, 4 * m * n + 1):
    if not visited[i]:
        dfs(i)
    if not visited[-i]:
        dfs(-i)
component = 0
scc = [0] * (8 * m * n + 1)
while stack:
    now = stack.pop()
    if not scc[now]:
        component += 1
        dfs_inv(now)
print('YES')
answer = [[0] * m for _ in range(n)]
trans = {
    1111: chr(43), 1101: chr(62), 1110: chr(118), 111: chr(60),
    1011: chr(94), 1100: chr(114), 1001: chr(76), 110: chr(55),
    11: chr(74), 101: chr(124), 1010: chr(45)
}
for i in range(n):
    for j in range(m):
        now = (m * i + j) * 4
        check = 0
        for d in range(1, 5):
            if scc[now + d] > scc[-(now + d)]:
                check += 10 ** (d - 1)
        if board[i][j] == 'X':
            answer[i][j] = board[i][j]
        elif check in trans:
            answer[i][j] = trans[check]
        else:
            answer[i][j] = '.'
for line in answer:
    print(''.join(line))
