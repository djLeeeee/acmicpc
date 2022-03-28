from sys import stdin

input = stdin.readline

while True:
    lx, ly, lz, x, y, z = map(int, input().split())
    if lx == ly == lz == 0:
        break
    if x == 0 or y == 0 or z == 0:
        print(x * x + y * y + z * z)
    elif x == lx:
        a = (lx + y) * (lx + y) + z * z
        b = (lx + z) * (lx + z) + y * y
        c = (lx + lz - z) * (lx + lz - z) + (lz + y) * (lz + y)
        d = (lx + ly - y) * (lx + ly - y) + (ly + z) * (ly + z)
        print(min(a, b, c, d))
    elif y == ly:
        a = (ly + x) * (ly + x) + z * z
        b = (ly + z) * (ly + z) + x * x
        c = (ly + lz - z) * (ly + lz - z) + (lz + x) * (lz + x)
        d = (ly + lx - x) * (ly + lx - x) + (lx + z) * (lx + z)
        print(min(a, b, c, d))
    elif z == lz:
        a = (lz + y) * (lz + y) + x * x
        b = (lz + x) * (lz + x) + y * y
        c = (lz + lx - x) * (lz + lx - x) + (lx + y) * (lx + y)
        d = (lz + ly - y) * (lz + ly - y) + (ly + x) * (ly + x)
        print(min(a, b, c, d))
