import sys

sys.stdin = open("input.txt","r")

T = int(input())
# DFS 에 얽메이지 말 것 그냥 완전탐색이 빠를 때도 있음
for testcase in range(1,T+1):
    answer = 0
    N, K = map(int, input().split())
    board=[]
    for _ in range(N):
        board.append(list(map(int,input().split())))
    # print(board)

    for col in range(N):
        count = 0
        for row in range(N):
            if(board[col][row]== 0):
                if(count == K):
                    answer +=1
                count = 0
            else:
                count +=1
        if(count == K):
            answer +=1

    for row in range(N):
        count = 0
        for col in range(N):
            if(board[col][row]== 0):
                if(count == K):
                    answer +=1
                count = 0
            else:
                count +=1
        if(count == K):
            answer +=1

    print("#{} {}".format(testcase,answer))

