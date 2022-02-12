from sys import stdin as s

A = s.readline().strip()
B = s.readline().strip()

la = len(A)
lb = len(B)
if la < lb:
    A, B = B, A
    la, lb = lb, la
dp = [''] * (lb + 1)
for x in range(1, la + 1):
    old_dp = dp[:]
    for y in range(1, lb + 1):
        if A[x - 1] == B[y - 1]:
            dp[y] = old_dp[y - 1] + A[x - 1]
        else:
            dp[y] = max(dp[y], dp[y - 1], key=lambda n: len(n))
print(len(dp[-1]))
# print(dp[-1])
