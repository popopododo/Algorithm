n = int(input())
stairs = [0]
answer=0
d=[0]*(n+1)
for i in range(n):
    k=int(input())
    stairs.append(k)



if(n<=3):
    if(n==1):
        print(stairs[1])
    elif(n==2):
        print(stairs[1]+stairs[2])
    elif(n==3):
        print(max(stairs[1]+stairs[3],stairs[2]+stairs[3]))
else:

    d[1]= stairs[1]
    d[2]= d[1]+stairs[2]
    d[3] = max(stairs[1]+stairs[3],stairs[2]+stairs[3])

    for x in range(4,n+1):
        d[x] = max((stairs[x-1]+d[x-3]),d[x-2])+stairs[x]
    print(d[n])









