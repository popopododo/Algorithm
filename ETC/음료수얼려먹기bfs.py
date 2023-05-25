from collections import deque
n,m=map(int,input().split())

ice_bucket=[]
queue= deque()
answer=0
for i in range(n):
    ice_bucket.append(list(map(int,input())))



def bfs(x,y,queue):
    queue.append([x,y])
    ice_bucket[x][y]=1
    while queue:
        v = queue.popleft()
        dx=[v[x]+1,v[x]-1,v[x],v[x]]
        dy=[v[y],v[y],v[y]+1,v[y]-1]
        for i in range(4):
            nx= dx[i]
            ny=dy[i]
            if (nx < 0 or nx >= n or ny < 0 or ny >= m):
                return False
            else:
                if(ice_bucket[nx][ny]==0):
                    queue.append([nx,ny])
                    return True
        return True

for i in range(n):
    for j in range(m):
        if(bfs(i,j,queue)==True):
            answer+=1

