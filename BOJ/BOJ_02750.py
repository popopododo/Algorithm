n=int(input())
l=[]
max=0
for x in range(n):
    temp=int(input())
    if(temp in l):
        continue
    l.append(temp)

for x in range(n-1,0,-1):
    for y in range(x):
        if(l[y]>l[y+1]):
            t=l[y]
            l[y]=l[y+1]
            l[y+1]=t

for x in l:
    print(x,sep="\n")