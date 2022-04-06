from sys import stdin

input = stdin.readline


def sol():
    def find(target):
        if target == parents[target]:
            return target
        parents[target] = find(parents[target])
        return parents[target]

    def union(a, b):
        a, b = find(a), find(b)
        parents[a] = b

    blue = []
    red = []
    component = n
    parents = list(range(n + 1))
    for _ in range(m):
        c, x, y = input().strip().split()
        x, y = int(x), int(y)
        if find(x) != find(y):
            union(x, y)
            component -= 1
        if c == 'R':
            red.append((x, y))
        else:
            blue.append((x, y))
    if component > 1 or k > len(blue) or k >= n:
        return 0
    parents = list(range(n + 1))
    c_red = n
    d_red = 0
    for x, y in red:
        if find(x) != find(y):
            union(x, y)
            c_red -= 1
        else:
            d_red += 1
    parents = list(range(n + 1))
    c_blue = n
    d_blue = 0
    for x, y in blue:
        if find(x) != find(y):
            union(x, y)
            c_blue -= 1
        else:
            d_blue += 1
    if c_red - 1 <= k and c_blue <= n - k:
        return 1
    return 0


while True:
    n, m, k = map(int, input().split())
    if n == m == k == 0:
        break
    print(sol())
