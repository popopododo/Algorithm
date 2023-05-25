n=int(input())
p= [0 for _ in range(n+1)]

for x in range(2,n+1):
    p[x] = p[x-1]+1

    if(x%2==0 and p[x] > p[x//2]+1):
        p[x] = p[x//2]+1
    if(x%3==0 and p[x] > p[x//3]+1):
        p[x] = p[x//3]+1

print(p[n])