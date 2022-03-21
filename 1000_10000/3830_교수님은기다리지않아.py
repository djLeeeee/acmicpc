from sys import stdin, setrecursionlimit

input = stdin.readline
setrecursionlimit(10 ** 5)


def find(target):
    if parents[target] == target:
        return target
    new_parent = find(parents[target])
    mass[target] += mass[parents[target]]
    parents[target] = new_parent
    return parents[target]


def union(a, b, weight):
    pa = find(a)
    pb = find(b)
    mass[pa] = mass[b] - weight - mass[a]
    parents[pa] = pb


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    parents = list(range(n + 1))
    mass = [0] * (n + 1)
    for _ in range(m):
        order, *nums = input().strip().split()
        nums = [int(num) for num in nums]
        if order == '!':
            x, y, w = nums
            if find(x) != find(y):
                union(x, y, w)
        else:
            x, y = nums
            if find(x) != find(y):
                print('UNKNOWN')
            else:
                print(mass[y] - mass[x])
