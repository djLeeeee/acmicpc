n, m = map(int, input().split())
gn = 0
for i in range(n):
    line = list(map(int, input().split()))
    ex = 0
    for j in range(m - 1, -1, -1):
        if line[j] > ex:
            ex = line[j]
        else:
            ex = line[j] - 1
    gn ^= ex
print("koosaga" if gn else "cubelover")
