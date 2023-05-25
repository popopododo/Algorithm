import sys
n,m=map(int,input().split())

ice_bucket=[]

for i in range(n):
    ice_bucket.append(list(map(int,input())))


def dfs(x,y):
    if (x<0 or x>=n or y<0 or y>=m):
        return False
    if(ice_bucket[x][y]==0):
        ice_bucket[x][y]=1
        dfs(x-1,y)
        dfs(x + 1, y)
        dfs(x, y+1)
        dfs(x,y-1)
        return True
    return False

answer = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            answer+=1

print(answer)