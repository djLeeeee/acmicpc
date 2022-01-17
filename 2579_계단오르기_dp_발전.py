import sys
p=sys.stdin.readline

a=int(p())
score=[0]
for i in range(a):
    score.append(int(input()))

scoreget=[0 for i in range(a+1)]
scoreget[1]=score[1]
if a==1:
    print(score[1])
elif a==2:
    print(score[1]+score[2])
elif a==3:
    print(score[1]+score[3])
else:
    scoreget[2]=score[1]+score[2]
    scoreget[3]=score[1]+score[3]
    for i in range(4,a+1):
        scoreget[i]=max(scoreget[i-3]+score[i-1],scoreget[i-2])+score[i]
    print(scoreget[-1])