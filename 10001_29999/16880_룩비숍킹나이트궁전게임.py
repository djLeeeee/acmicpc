from sys import stdin

input = stdin.readline

gn = 0
for _ in range(int(input())):
    x, y, s = input().strip().split()
    x, y = int(x), int(y)
    z = min(x, y)
    if s == 'R':
        ex = x ^ y
    elif s == 'B':
        ex = z
    elif s == 'K':
        if (x - y) % 2:
            if z % 2:
                ex = 3
            else:
                ex = 1
        else:
            if z % 2:
                ex = 2
            else:
                ex = 0
    elif s == 'N':
        if z % 3 == 0:
            ex = 0
        elif z % 3 == 1:
            ex = 1 if x != y else 0
        else:
            ex = 2 if abs(x - y) > 1 else 1
    else:
        dx, dy = x // 3, y // 3
        ex = 3 * (dx ^ dy) + (x + y) % 3
    gn ^= ex
print("koosaga" if gn else "cubelover")
