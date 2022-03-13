# 6091 핑크플로이드
# find-union + 오프라인 쿼리 개념으로 품
# 근데 이게 오프라인 쿼리 개념이 맞긴 한가?

from sys import stdin as s
from sys import setrecursionlimit as strc

strc(10 ** 6)

n = int(s.readline())

parent = list(range(n + 1))


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


connection = []
for i in range(1, n):
    a = list(map(int, s.readline().split()))
    for x, j in enumerate(a):
        connection.append([j, i, i + x + 1])
connection.sort()
v = 0
result = [[] * (n + 1) for _ in range(n + 1)]
pointer = 0
while v < n - 1:
    line = connection[pointer]
    if find(line[1]) != find(line[2]):
        union(line[1], line[2])
        result[line[1]].append(line[2])
        result[line[2]].append(line[1])
        v += 1
    pointer += 1
for i in range(1, n + 1):
    print(len(result[i]), *sorted(result[i]))
