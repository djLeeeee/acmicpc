from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))
M = max(arr)
fib = [1, 1]
grundy = [0] * (M + 1)
for idx in range(1, M + 1):
    sub_grundy = set()
    if fib[-1] + fib[-2] == idx:
        fib.append(idx)
    for num in fib:
        sub_grundy.add(grundy[idx - num])
    for gn in range(idx + 1):
        if gn not in sub_grundy:
            grundy[idx] = gn
            break
total_grundy = 0
for num in arr:
    total_grundy ^= grundy[num]
print('koosaga' if total_grundy else 'cubelover')
