def power(a, b):
    res = 1
    while b > 0:
        if b % 2:
            res *= a
        a *= a
        b //= 2
    return res


def solve(w, l):
    p = (1 - power(f, l)) / (1 - power(f, w + l))
    return p * w - (1 - p) * l * (1 - n)


n, m = map(lambda x: float(x) / 100, input().split())
if m == 0:
    print(0)
    exit()
f = (1 - m) / m
ans = 0
win, lose = 1, 1
while True:
    pre = 0
    flag = False
    while True:
        now = solve(win, lose)
        if now >= ans:
            ans = now
            flag = True
        else:
            if flag:
                win -= 1
            break
        win += 1
        pre = now
    if not flag:
        break
    lose += 1
print(ans)
