N,M = map(int,input().split())
d=[0]*10001
bills=[]
for i in range(N):
    k=int(input())
    bills.append(k)

for x in bills:
    d[x] = 1

for i in range(1,M+1):
    tempMin = 10001
    for j in bills:
        if(i%j==0):
            d[i]=min(i//j,d[i-j]+1)



if(d[M]==0):
    print(-1)
else:
    print(d[M])









