from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 6)


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a = find(a)
    b = find(b)
    if a in full:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = list(range(m + 1))
full = set()
for _ in range(n):
    x, y = map(int, input().split())
    if find(x) != find(y):
        if find(x) in full and find(y) in full:
            print('SMECE')
        else:
            print('LADICA')
        union(x, y)
    else:
        if find(x) in full:
            print('SMECE')
        else:
            full.add(find(x))
            print('LADICA')
