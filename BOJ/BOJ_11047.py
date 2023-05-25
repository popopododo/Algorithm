n,m = map(int,input().split())
l=[]
result=0
for x in range(n):
    x=int(input())
    l.append(x)

for x in range(n-1,-1,-1):
    if(m//l[x]!=0):

        result+=m//l[x]
        m%=l[x]
    if(m==0):
        break
print(result)