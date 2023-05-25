import sys

sys.stdin = open("input.txt","r")

T = int(input())

for testcase in range(1,T+1):

    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    # print(matrix)

    # # 90 도
    #
    # for j in range(0,N):
    #     for i in range(N-1,-1,-1):
    #         print(matrix[i][j],end='')
    #     print()
    #
    # # 180도
    #
    # for i in range(N-1,-1,-1):
    #     for j in range(N-1,-1,-1):
    #         print(matrix[i][j],end='')
    #     print()
    #
    # # 270도
    #
    # for j in range(N-1,-1,-1):
    #     for i in range(0,N):
    #         print(matrix[i][j],end='')
    #     print()
    print("#{}".format(testcase))
    for i in range(N):
        for j in range(N):
            print(matrix[N-1-j][i],end= "")
        print(end= " ")
        for j in range(N):
            print(matrix[N-1-i][N-1-j],end= "")
        print(end=" ")
        for j in range(N):
            print(matrix[j][N-1-i],end= "")
        print()


