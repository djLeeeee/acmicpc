# 내장함수 최대한 안 쓰고 통계값 출력
# 입력값의 number보다 Range가 많이 작을 때 효과적일 듯? 

import sys

n=int(sys.stdin.readline())

N=4000

a=[0 for _ in range(2*N+1)]
min=N+1
max=-N-1

# 기존 데이터를 보다 간단하게 list로 정리 / max min 저장
for _ in range(n):
    num=int(sys.stdin.readline())
    a[num+N]+=1
    if min>num:
        min=num
    if max<num:
        max=num

M=1
maximum=[]
sum=0
order=0
for i,j in enumerate(a):
    sum+=(i-N)*j
    if order<=n//2:
        order+=j
        middle=i-N   
    if j>M:
        maximum=[i-N]
        M=j
    elif j==M:
        if len(maximum)<=1:
            maximum.append(i-N)


print(round(sum/n)) # 평균
print(middle)       # 중앙값
print(maximum[-1])  # 최빈값(여러개인 경우 2번째 최빈값)
print(max-min)      # 범위