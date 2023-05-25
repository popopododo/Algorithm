from collections import deque

N , M, V = map(int,input().split())
# N: 정점 M: 간선 V: 탐색을 시작할 정점 번호
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    n,m = map(int,input().split())
    graph[n][m]= graph[m][n]=1
# print(graph)
'''
G=[[]]*(N+1)


visited_dfs=[False]*(N+1)
visited_bfs=[False]*(N+1)

for x in range(M):
    y, z = map(int,input().split())
    if(G[y]==[]):
        G[y]=[z]
    else:
        G[y].append(z)
    if(G[z]==[]):
        G[z]=[y]
    else:
        G[z].append(y)


def dfs(G,v,visited_dfs):
    visited_dfs[v]=True
    print(v, end=' ')
    for i in G[v]:
        if not visited_dfs[i]:
            dfs(G, i, visited_dfs)

def bfs(G,start,visited_bfS):
    queue= deque([start])
    visited_bfs[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in G[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True
'''

def bfs(V):
    visited=[V]
    queue=deque()
    queue.append(V)

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for x in range(N+1):
            if(graph[v][x] ==1 and ( x not in visited)):
                visited.append(x)
                queue.append(x)

def dfs(V,visited=[]):
    visited.append(V)
    print(V, end=' ')

    for x in range(N+1):
        if(graph[V][x] == 1 and (x not in visited)):
            dfs(x,visited)

dfs(V)
print()
bfs(V)

