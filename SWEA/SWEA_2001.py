import sys
sys.stdin = open('input.txt','r')
'''
10
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29
'''
T= int(input())
def add(x,y):
    count = 0
    for i in range(M):
        for j in range(M):
            count += board[x+i][y+j]
    return count
for testcase in range(1,T+1):
    N, M = map(int,input().split())
    board = []
    flyKiller = N-M +1
    for i in range(N):
        tempBoard = tuple(map(int,input().split()))
        board.append(tempBoard)
    d = [0] * (N*N)

    for i in range(flyKiller): # 0~3
        for j in range(flyKiller): # 0~3
            d[N*i + j] = add(i,j)

    # print(d)
    print("#{} {}".format(testcase,max(d)))