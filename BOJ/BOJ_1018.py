N,M = map(int, input().split()) # y, x
K= 0
l=0
r=0
min=65
compare=[]
chess=[]
if(N== 8 and M==8 ):
    l=1
    r=1
    K=1

elif(N>=8 or M>=8):
    l=N-7
    r= M-7
    K = l*r

for i in range (N):   # 체스판 만들기
        temp= list(input())
        chess.append(temp)

for i in range(l):  # 체스판에 첫번재 좌표로 사용할 좌표 compare 안에 저장
    for j in range(r):
        compare.append((i,j))

for c in compare:
    tempAlpha=''
    tempBeta=''
    isSame=False
    countAlpha=0
    countBeta=0
    #print(c[0],c[1],chess[c[0]][c[1]])
    #print("============")
    if((c[0]%2) == (c[1]%2)):
        isSame=True

    if(chess[c[0]][c[1]]=='W'): # 첫번째 알파벳이 W 인지 B 인지 비교 연산
        tempAlpha= 'W'
        tempBeta='B'
    else:
        tempAlpha = "B"
        tempBeta='W'
    for i in range(c[0], c[0] + 8): # 체스판 Brute Force 하면서 하나씩 W, B 비교
        for j in range(c[1], c[1] + 8): # 맞는 조건 명시 후 else 로 처리
            temp1=i%2
            temp2=j%2
            if(isSame==True):
                if(temp1==temp2):
                    if(chess[i][j]!=tempAlpha):
                        #print(i,j,chess[i][j])
                        countAlpha+=1
                elif(temp1!=temp2):
                    if(chess[i][j]==tempAlpha):
                        countAlpha+=1
                        #print(i, j,chess[i][j])
            else:
                if (temp1 != temp2):
                    if (chess[i][j] != tempAlpha):
                        #print(i, j, chess[i][j])
                        countAlpha += 1
                elif (temp1 == temp2):
                    if (chess[i][j] == tempAlpha):
                        countAlpha += 1
                        #print(i, j, chess[i][j])

    for i in range(c[0], c[0] + 8): # 체스판 Brute Force 하면서 하나씩 W, B 비교
        for j in range(c[1], c[1] + 8): # 맞는 조건 명시 후 else 로 처리
            temp1=i%2
            temp2=j%2
            if(isSame==True):
                if(temp1==temp2):
                    if(chess[i][j]!=tempBeta):
                        #print(i,j,chess[i][j])
                        countBeta+=1
                elif(temp1!=temp2):
                    if(chess[i][j]==tempBeta):
                        countBeta+=1
                        #print(i, j,chess[i][j])
            else:
                if (temp1 != temp2):
                    if (chess[i][j] != tempBeta):
                        #print(i, j, chess[i][j])
                        countBeta += 1
                elif (temp1 == temp2):
                    if (chess[i][j] == tempBeta):
                        countBeta+= 1
                        #print(i, j, chess[i][j])


    if(countAlpha>countBeta):
        count= countBeta
    else:
        count=countAlpha

    if(min>count):
        min=count

print(min)
