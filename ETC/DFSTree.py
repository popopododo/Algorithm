graph=[
    [],
    [2,4],
    [1,3,5],
    [2],
[1,6,7],
[2],
[4],
[4],
]

visited= [False]*8


def dfs(graph,v,visited):
    visited[v]=True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,1,visited)
