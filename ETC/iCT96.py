N,M =map(int,input().split())
answer=0  # 제일 작은 수
for _ in range(N):
    tempList=list(map(int,input().split()))
    tempList.sort()
    if(tempList[0]>=answer): # tempList 마다 제일 작은 값 중 최대 값을 answer에 대입
        answer=tempList[0]

print(answer)

