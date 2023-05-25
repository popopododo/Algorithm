N = int(input())
l=[]
for x in range(N):
    x = tuple(map(int,input().split()))
    l.append(x)
sorted(l,key=lambda x: x[0])
sorted(l,key=lambda x: x[1])

count=0
pre=0

for i,j in l:
    if(i>=pre):
        count+=1
        pre=j
print(count)

