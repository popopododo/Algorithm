import sys

sys.stdin = open("input.txt","r")

T = int(input())

for testcase in range(1,T+1):
    N, M = map(int,input().split())
    Ai = list(map(int,input().split()))
    Bj = list(map(int, input().split()))
    answer = [0]*min(N,M)
    iterate = abs(N-M)+1
    # print(Ai,Bj,answer)

    if(N < M):
        shortList = Ai
        longList = Bj
    else:
        shortList = Bj
        longList = Ai

    for i in range(iterate): # 0 ~ N-M +1
        tempAnswer =0
        for j in range(len(shortList)):
            # print(j,j+i)
            tempAnswer+= shortList[j]*longList[j+i]
        answer.append(tempAnswer)



    print("#{} {}".format(testcase,max(answer)))



