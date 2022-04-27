from sys import stdin

input = stdin.readline

n = int(input())
ans = 0
arr = list(map(int, input().split()))
grundy = 0
for num in arr:
    grundy ^= num
for num in arr:
    grundy ^= num
    if grundy < num:
        ans += 1
    grundy ^= num
print(ans)
