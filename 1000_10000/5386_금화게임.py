
from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    if m % 2:
        if n % 2:
            print(1)
        else:
            print(0)
    else:
        n %= (m + 1)
        if n == m:
            print(m)
        elif n % 2:
            print(1)
        else:
            print(0)
"""
규칙 찾기용 코드
n, m = map(int, input().split())
grundy = [0] * (n + 1)
grundy[1] = 1
for num in range(2, n + 1):
    sub_grundy = set()
    if m == 1:
        sub_grundy.add(grundy[num - 1])
    else:
        check = 1
        while check <= num:
            sub_grundy.add(grundy[num - check])
            check *= m
    for gn in range(num + 1):
        if gn not in sub_grundy:
            grundy[num] = gn
            break
for i in range(10):
    print(grundy[i * 10 + 1:i * 10 + 11])
"""
