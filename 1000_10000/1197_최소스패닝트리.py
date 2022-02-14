from sys import stdin as s
from sys import setrecursionlimit as stlim

stlim(10 ** 6)

v, e = map(int, s.readline().split())

connection = []
for _ in range(e):
    connection.append(list(map(int, s.readline().split())))
connection.sort(key=lambda n: n[-1])

parent = list(range(v + 1))


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    x = find(a)
    y = find(b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    return


i = 1
ans = 0
for line in connection:
    if find(line[0]) != find(line[1]):
        union(line[0], line[1])
        i += 1
        ans += line[2]
    if i == v:
        break
print(ans)
