n= int(input())
graph=[]
for l in range(n):
    x=list(map(int,input().split()))
    x.append(1)
    x.append(l)
    graph.append(x)


G = sorted(graph, key = lambda x : x[0],reverse=True)
# print(G)
for x in range(n):
    for y in range(n):
        if(x==y):
            continue
        if(G[x][1]<G[y][1] and G[x][0]<G[y][0]):
            G[x][2]+=1


graph = sorted(G, key = lambda x : x[3])

for x in range(n):
    print(graph[x][2],end=' ')




# print(G)

# print(graph)