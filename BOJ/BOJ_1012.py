import sys
from collections import deque
sys.setrecursionlimit(10**6) # BOJ의 최대재귀는 1000으로 제한이 되어있기 때문에 10^6 정도로 늘려줌
T= int(input()) # Test Case
answer=[0]*T #  답을 저장해놓는 리스트
def dfs(x,y): # i , j ( graph 상의 y 좌표 , graph 상의 x 좌표)
    if(x<=-1 or x >=N or y<= -1 or y>=M):
        return False # Graph 에서 범위를 벗어나면 재귀 종료
    if graph[x][y] == 1:
        #print(y,x , end = '\n\n')
        graph[x][y]=0 # 1일 경우 0으로 바꿔줘서 visit 표시
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True # 상, 하, 좌,우 모두 dfs 를 해도 1로 들어왔으니 True 리턴
    return False # 위에 조건 모두 아니면 False

for z in range(T):
    count=0
    # 배추밭 가로 , 세로 , 위치의 개수
    M,N, K = map(int,input().split())
    graph=[[0]*M for _ in range(N)]

    for _ in range(K):
        m,n= map(int,input().split())
        graph[n][m]=1

    # Graph 안을 순회하면서 모든 좌표들마다 dfs를 수행
    for i in range(N): # y
        for j in range(M): # x
            # print(i, j, end='\n')
            if dfs(i,j)==True:
                count+=1

    answer[z]= count

for i in answer:
    print(i)
''' My code 
    def dfs(V,visited=[]):
        queue=deque()
        queue.append(V)
        visited.append(V)

        while queue:
            v = queue.popleft()
            for x in range(4):
                temp=(v[0]+x_dir[x],v[1]+y_dir[x])
                if(graph[temp[0]][temp[1]]==1 and (temp not in visited)):
                    print(temp)
                    visited.append(temp)
                    dfs(temp,visited)
            global count
            count+=1

    dfs(start)
    # print(count)
'''

