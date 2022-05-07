from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    t = 0
    for num in arr:
        if num > 1:
            t += 1
    if n == 2:
        print(1)
    else:
        print(min(n // 2, t))
