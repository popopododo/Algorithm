import sys

T=int(input())

for i in range(T):
    n,m = map(int,input().split())
    mineTemp=list(map(int,sys.stdin.readline().split()))
    mine=[]
    for x in mineTemp:
        da = []
        for y in range(m):

            da.append(x)
        mine.append(da)
    print(mine)
