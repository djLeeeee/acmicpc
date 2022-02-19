from sys import stdin as s
from collections import deque


def find(target):
    if parents[target] == target:
        return target
    parents[target] = find(parents[target])
    return parents[target]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


for _ in range(int(s.readline())):
    v, e = map(int, s.readline().split())
    connection = [[] for _ in range(v + 1)]
    parents = list(range(v + 1))
    for _ in range(e):
        x, y = map(int, s.readline().split())
        union(x, y)
        connection[x].append(y)
        connection[y].append(x)
    check = [0] * (v + 1)
    start = set()
    for i in range(1, v + 1):
        x = find(i)
        check[x] = 1
        start.add(x)
    start = deque(start)
    result = True
    while start and result:
        now = start.popleft()
        pm = check[now]
        for can_go in connection[now]:
            if check[can_go] == 0:
                start.append(can_go)
                check[can_go] = -pm
            elif check[can_go] == pm:
                result = False
                break
    print(check)
    if result:
        print('YES')
    else:
        print('NO')
