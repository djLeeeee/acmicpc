from sys import stdin as s

n = int(s.readline())
visited = [False] * (n + 1)
visited[0] = True
parents = list(range(n + 1))


def find(target):
    if target == parents[target]:
        return target
    parents[target] = find(parents[target])
    return parents[target]


def union(a, b):
    x = find(a)
    y = find(b)
    if x <= y:
        parents[y] = x
    else:
        parents[x] = y
    return


ans = 0
m = int(s.readline())
for _ in range(m):
    aircraft = find(int(s.readline()))
    if visited[aircraft]:
        break
    else:
        visited[aircraft] = True
        union(aircraft, find(aircraft - 1))
        ans += 1
print(ans)
