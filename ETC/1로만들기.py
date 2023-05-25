n=int(input())

d=[0]*(n+1)

d[2]=1
d[3]=1
d[4]=2
d[5]=1

for i in range(6,n+1):
    tempA= 30000
    tempB=0

    if(i%2==0):
        tempB=d[i//2]+1
    elif(i%3==0):
        tempB = d[i // 3] + 1
    elif(i%5==0):
        tempB = d[i//5]+1
    else:
        tempB = d[i-1]+1
    tempA = d[i-1]+1
    d[i] = min(tempA,tempB)
    print(tempA,tempB)

print(d)
