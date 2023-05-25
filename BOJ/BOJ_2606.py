from collections import deque
count=0
N = int(input())
M = int(input())
graph=[[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    n,m = map(int,input().split())
    graph[n][m] = graph[m][n] = 1

def dfs(V,visited=[]):
    queue= deque()
    queue.append(V)
    visited.append(V)
    while queue:
        v= queue.popleft()
        # print(v, end=' ')

        for x in range(N+1):
            if(graph[v][x]==1 and (x not in visited)):
                global count
                count+=1
                dfs(x,visited)
dfs(1)
print(count)


