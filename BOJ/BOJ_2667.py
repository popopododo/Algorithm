import sys
from collections import deque
sys.setrecursionlimit(10**6)

N= int(input())
graph=[]
answer=[]
count = 0
for _ in range(N):
    t= list(map(int,input()))
    graph.append(t)

def dfs(x,y): # i , j
    global count
    if(x<=-1 or x>=N or y<=-1 or y>=N):
        return False
    if(graph[x][y]==1):
        graph[x][y]=0
        count+=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        # print("{} {}||{}".format(x,y,count))
        return True
    return False


for i in range(N):
    for j in range(N):
        if(dfs(i,j)== True):
            answer.append(count)
            count=0  # 집에 갯수를 센 후에 answer 에 append

print(len(answer)) # 단지의 갯수 구하기
answer.sort() # 오름차순 내림차순은 sorted(reverse=True)
for i in answer:
    print(i)

