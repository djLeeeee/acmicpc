from sys import stdin

input = stdin.readline

n = int(input())
arr = map(int, input().split())
grundy = 0
for num in arr:
    grundy ^= num
print('koosaga' if grundy else 'cubelover')
