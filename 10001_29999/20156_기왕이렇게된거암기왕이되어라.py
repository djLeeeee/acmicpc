from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)
input = stdin.readline


def find(target):
    if p[target] == target:
        return target
    p[target] = find(p[target])
    return p[target]


def union(a, b):
    a = find(a)
    b = find(b)
    p[a] = p[b]


n, m, k = map(int, input().split())
p = list(range(n + 1))
line = list(map(int, input().split()))
for i in range(n):
    if line[i] > 0:
        p[i + 1] = line[i]
orders = [(0, 0)]
changed = [False] * (n + 1)
for _ in range(m):
    order = int(input())
    if changed[order] or p[order] == order:
        orders.append((0, 0))
    else:
        changed[order] = True
        orders.append((order, p[order]))
        p[order] = order
query = [list(map(int, input().split())) + [j] for j in range(k)]
ans = ["No;"] * k
query.sort()
stage = m
while query:
    r, x, y, idx = query.pop()
    while stage > r:
        z, w = orders[stage]
        union(z, w)
        stage -= 1
    if find(x) == find(y):
        ans[idx] = "Same Same;"
print('\n'.join(ans))
