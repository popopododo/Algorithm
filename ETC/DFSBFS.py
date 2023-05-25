from collections import deque

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited_DFS=[False]* 9
visited_BFS=[False]*9

def dfs(graph,v,visited_DFS):
    visited_DFS[v]=True
    print(v,end='')
    for i in graph[v]:
        if not visited_DFS[i]:
            dfs(graph,i,visited_DFS)

def bfs(graph,start,visited_BFS):
    queue= deque([start])
    visited_BFS[start]= True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited_BFS[i]:
                queue.append(i)
                visited_BFS[i] = True

bfs(graph,1,visited_DFS)




