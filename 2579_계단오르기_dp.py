import sys
p=sys.stdin.readline

a=int(p())
score=[0]
for i in range(a):
    score.append(int(input()))

score.append(0)
score.append(0)

scoreget=[[0,0] for i in range(a+3)]
scoreget[1]=[score[1],score[1]]
scoreget[2]=[score[1]+score[2],score[2]]
scoreget[3]=[score[2]+score[3],score[1]+score[3]]
updated=[1,2,3]
while True:
    reupdated=[]
    for i in updated:
        if i<=a:
            if scoreget[i+2][1]<max(scoreget[i])+score[i+2]:
                scoreget[i+2][1]=max(scoreget[i])+score[i+2]
                reupdated.append(i+2)
            if scoreget[i+1][0]<scoreget[i][1]+score[i+1]:
                scoreget[i+1][0]=scoreget[i][1]+score[i+1]
                reupdated.append(i+1)
    if reupdated==[]:
        break
    updated=reupdated

if a==1:
    print(score[1])
elif a==2:
    print(score[1]+score[2])
elif a==3:
    print(max(score[1],score[2])+score[3])
else:    
    print(max(scoreget[a]))