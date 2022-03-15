from sys import stdin
from sys import setrecursionlimit
from collections import defaultdict

setrecursionlimit(10 ** 6)
input = stdin.readline


def min_max(xx, yy):
    return min(xx, yy), max(xx, yy)


def find(parent, target):
    if parent[target] == target:
        return target
    parent[target] = find(parent, parent[target])
    return parent[target]


def union(parent, a, b):
    aa = find(parent, a)
    bb = find(parent, b)
    parent[aa] = bb


def transform(a, b):
    return min_max(state[a], state[b])


n, m, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
state = [0] + list(map(int, input().split()))
parents = list(range(n + 1))
for x, y in edges:
    if state[x] == state[y]:
        union(parents, x, y)
q = int(input())
query = [tuple(map(int, input().split())) for _ in range(q)]
parents_dict = defaultdict(dict)
for x, y in edges:
    parents_dict[transform(x, y)][find(parents, x)] = find(parents, x)
    parents_dict[transform(x, y)][find(parents, y)] = find(parents, y)
for x, y in edges:
    union(parents_dict[transform(x, y)], find(parents, x), find(parents, y))
for x, y in query:
    result = '0'
    t = transform(x, y)
    if t in parents_dict and find(parents, x) in parents_dict[t] and find(parents, y) in parents_dict[t]:
        if find(parents_dict[t], find(parents, x)) == find(parents_dict[t], find(parents, y)):
            result = '1'
    print(result)
