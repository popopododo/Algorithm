import sys

sys.stdin = open("input.txt","r")

T = int(input())
def validation(l):
    matrix = [set(),set(),set()]
    ind = 0
    for col in range(9): # 세로 줄 검사
        if(len(set(l[col]))!= 9):
            return 0

        k = set()
        for row in range(9): # 가로 줄 검사
            k.add(l[row][col])
        if(len(k) != 9):
            return 0

    for num in range(0,81):
        col = num // 9
        row = num % 9

        if(num !=0 and num % 27 == 0): # 3x3 행렬 3개씩 검사
            if(len(matrix[0]) != 9 and len(matrix[1]) != 9 and len(matrix[2]) != 9):
                return 0

        if(num !=0 and num % 3 ==0):
            if(ind == 2):
                ind = -1
            ind+=1
        matrix[ind].add(l[col][row])
    return 1


for testcase in range(1,T+1):
    matrix = [list(map(int,input().split())) for _ in range(9)]
    print("#{} {}".format(testcase,validation(matrix)))