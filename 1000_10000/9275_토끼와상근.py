from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 5)


def find(target):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target])
    return parent[target]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[a] = b


def check(a):
    for b in stack:
        if find(a) == find(b):
            checker = 0
            for aa in graph[a]:
                if aa == b:
                    checker += 1
                if b in graph[aa]:
                    checker += 1
            if checker < 2:
                return True
    return False


while True:
    try:
        n, m = map(int, input().split())
    except ValueError:
        break
    parent = list(range(n + 1))
    deg = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        deg[x] += 1
        deg[y] += 1
        union(x, y)
        graph[x].append(y)
        graph[y].append(x)
    if max(deg) >= 4:
        print('YES')
    elif max(deg) <= 2:
        print('NO')
    else:
        stack = []
        ans = 'NO'
        for i in range(1, n + 1):
            if deg[i] == 3:
                if check(i):
                    ans = 'YES'
                    break
                stack.append(i)
        print(ans)
