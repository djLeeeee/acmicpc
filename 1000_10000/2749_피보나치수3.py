# 피사노 주기 사용

n=int(input())
n = n % 1500000
a=[0, 1]
for i in range(n-1):
    a.append((a[-1]+a[-2])% 1000000)
print(a[-1])