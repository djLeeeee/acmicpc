from sys import stdin

input = stdin.readline

n, q1, q2 = map(int, input().split())
arr = [int(input()) for _ in range(n)]
sn = int(n ** 0.5)
square_sum = [0] * (n // sn + 1)
ex = [0] * (n // sn + 1)
for i in range(n):
    square_sum[i // sn] += arr[i]
for _ in range(q1 + q2):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        _, s, e, k = query
        s -= 1
        e -= 1
        i, j = s // sn, e // sn
        if i == j:
            if s % sn == 0 and e % sn == sn - 1:
                ex[i] += k
            else:
                for t in range(s, e + 1):
                    arr[t] += k
        else:
            for t in range(i + 1, j):
                ex[t] += k
            ri, rj = s % sn, e % sn
            if ri == 0:
                ex[i] += k
            else:
                for t in range(ri, sn):
                    arr[i * sn + t] += k
                square_sum[i] += k * (sn - ri)
            if rj == sn - 1:
                ex[j] += k
            else:
                for t in range(rj + 1):
                    arr[j * sn + t] += k
                square_sum[j] += k * (rj + 1)
    elif query[0] == 2:
        _, s, e = query
        s -= 1
        e -= 1
        i, j = s // sn, e // sn
        if i == j:
            ans = sum(arr[s:e + 1]) + ex[i] * (e - s + 1)
        else:
            ri, rj = s % sn, e % sn
            ans = ex[i] * (sn - ri) + ex[j] * (rj + 1)
            for t in range(i + 1, j):
                ans += square_sum[t] + ex[t] * sn
            for t in range(ri, sn):
                ans += arr[i * sn + t]
            for t in range(rj + 1):
                ans += arr[j * sn + t]
        print(ans)
