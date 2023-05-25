n= int(input())
answer=0
warehouse= list(map(int,input().split()))
warehouse.insert(0,0)
d=[0]*(n+1)

d[1]=warehouse[1]
if(warehouse[1]<warehouse[2]):
    d[2]=warehouse[2]
else:
    d[2]= d[1]

print(d[1],d[2])
for i in range(3,n+1):
    d[i]= d[i - 2] + warehouse[i] if d[i-2]+warehouse[i]>=d[i-1] else d[i-1]

print(d)


'''
if(d[0]<d[1]):
    answer+=d[1]
    d[1]=0
else:
    answer+=d[0]
    d[0]=0
for x in range(1,n-2):

    if(d[x]==0):
        d[
        continue
    if(d[x]<d[x+1]):
        answer+=d[x]
        d[x]=0
    else:
        answer+=d[x+1]
        d[x+1]=0
'''

