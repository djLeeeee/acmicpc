from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 5)


def sol(idx, pc):
    if dp[idx][pc]:
        return dp[idx][pc]
    if not tree[idx]:
        return (pc == 1) + 1
    result = float('inf')
    for color in range(1, 20):
        if color != pc:
            now = color
            for adj in tree[idx]:
                now += sol(adj, color)
            if now < result:
                result = now
    dp[idx][pc] = result
    return result


n = int(input())
if n == 1:
    print(1)
    exit()
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
visited = [False] * (n + 1)
tree = [[] for _ in range(n + 1)]
point = [1]
visited[1] = True
while point:
    x = point.pop()
    for y in graph[x]:
        if not visited[y]:
            visited[y] = True
            point.append(y)
            tree[x].append(y)
dp = [[0] * 20 for _ in range(n + 1)]
print(sol(1, 0))
