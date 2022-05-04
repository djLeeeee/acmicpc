from sys import stdin

input = stdin.readline

n = int(input())
grundy = 0
for _ in range(n):
    x, y = map(int, input().split())
    grundy ^= ((x // 3) ^ (y // 3)) * 3 + ((x + y) % 3) % 3
print('koosaga' if grundy else 'cubelover')
