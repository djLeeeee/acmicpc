from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(2 * 10 ** 5)


def dfs(now, last):
    for adj, c in graph[now]:
        if not ans[adj] and adj != 1:
            dist[adj] = dist[now] + c
            start = 0
            end = last
            while start <= end:
                mid = (start + end) // 2
                init, idx = cht[mid]
                if init < sv[adj][1]:
                    res = idx
                    start = mid + 1
                else:
                    end = mid - 1
            ans[adj] = ans[res] + (dist[adj] - dist[res]) * sv[adj][1] + sv[adj][0]
            start = 0
            end = last
            while start <= end:
                mid = (start + end) // 2
                init, idx = cht[mid]
                if ans[adj] - ans[idx] > init * (dist[adj] - dist[idx]):
                    res = mid
                    start = mid + 1
                else:
                    end = mid - 1
            ns = (ans[adj] - ans[cht[res][1]]) / (dist[adj] - dist[cht[res][1]])
            memo = cht[res + 1][:]
            cht[res + 1] = [ns, adj]
            dfs(adj, res + 1)
            cht[res + 1] = memo


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y, d = map(int, input().split())
    graph[x].append((y, d))
    graph[y].append((x, d))
sv = [0, 0] + [tuple(map(int, input().split())) for _ in range(n - 1)]
dist = [0] * (n + 1)
ans = [0] * (n + 1)
cht = [[0, 0] for _ in range(n)]
cht[0][1] = 1
dfs(1, 0)
print(*ans[2:])
