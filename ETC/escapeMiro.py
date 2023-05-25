from collections import deque

n, m = map(int,input().split())
miro=[]
count=0
for i in range(n):
    miro.append(list(map(str,input())))


def bfs(x,y):
    queue= deque()
    count=0
    # miro[x][y]=count
    queue.append((x,y))
    while(queue):
        flag=False
        node = queue.popleft()
        count+=1
        miro[node[0]][node[1]] = count
        # print(queue, miro[node[0]][node[1]],node)
        if(node[0] == n-1 and node[1]==m-1):
            return miro[node[0]][node[1]]
        left =(node[0]-1,node[1])
        right = (node[0]+1,node[1])
        up = (node[0],node[1]-1)
        down = (node[0], node[1] +1)
        dir=[left,right,up,down]
        for i in dir:
            if(i[0]>=0 and i[1]>=0 and i[0]<n and i[1]<m):
                if(miro[i[0]][i[1]]=='1'):
                    flag=True
                    queue.append(i)
                    # print(queue)
        if(flag==False):
            count-=1



print(bfs(0,0))

# input

'''
5 6
101010
111111
000001
111111
111111
'''
