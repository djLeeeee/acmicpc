from sys import stdin
from collections import defaultdict

input = stdin.readline


def find(target):
    if not parent[target]:
        parent[target] = target
    if parent[target] != target:
        parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    pa, pb = find(a), find(b)
    if pa == pb:
        is_cycle[pa] = True
    elif pa < pb:
        parent[pb] = pa
        if is_cycle[pb]:
            is_cycle[pa] = True
    else:
        parent[pa] = pb
        if is_cycle[pa]:
            is_cycle[pb] = True


n = int(input())
ans = 0
parent = defaultdict(int)
is_cycle = defaultdict(bool)
for _ in range(n):
    x, y = map(int, input().split())
    ans += x + y
    union(x, y)
memo = defaultdict(list)
for key in parent:
    memo[find(key)].append(key)
for key in memo:
    if is_cycle[key]:
        ans -= sum(memo[key])
    else:
        ans -= sum(memo[key]) - max(memo[key])
print(ans)
