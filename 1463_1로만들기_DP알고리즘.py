a=int(input())
x=[0 for i in range(a+1)]
x[a]=1
n=1
updated=[a]
while True:
    if 1 in updated:
        break
    reupdated=[]
    for i in updated:
        if i%2==0 and x[i//2]==0:
            x[i//2]=n
            reupdated.append(i//2)
        if i%3==0 and x[i//3]==0:
            x[i//3]=n
            reupdated.append(i//3)
        if x[i-1]==0:
            x[i-1]=n
            reupdated.append(i-1)
    updated=reupdated
    n+=1
if a==1:
    print(0)
else:
    print(x[1])