from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)
input = stdin.readline


def dfs(v_idx, t_idx):
    global flag
    if not flag:
        return
    if team[v_idx]:
        if team[v_idx] != t_idx:
            flag = False
        return
    else:
        team[v_idx] = t_idx
    for adj, value in graph[v_idx].items():
        if value <= limit:
            dfs(adj, -t_idx)


def check():
    for idx in range(1, n + 1):
        if not team[idx]:
            dfs(idx, 1)


n = int(input())
graph = [{} for _ in range(n + 1)]
team = [0] * (n + 1)
m = int(input())
for i in range(1, m + 1):
    x, y = map(int, input().split())
    graph[x][y] = i
    graph[y][x] = i
start = 1
end = m
while start <= end:
    limit = (start + end) // 2
    team = [0] * (n + 1)
    flag = True
    check()
    if flag:
        start = limit + 1
    else:
        ans = limit
        end = limit - 1
print(ans)
