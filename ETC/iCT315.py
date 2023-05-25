N,M = map(int,input().split())
bowlingBall= list(map(int,input().split()))
overLapCount=[] # 크기마다 중복되는 볼링공의 갯수들 저장
answer=0
for i in range(1,N):
    answer+=i # 모든 경우의 수를 저장

for i in range(1,M+1): # 중복되는 볼링공의 갯수 count
    if(bowlingBall.count(i)>1):
       overLapCount.append(bowlingBall.count(i))

for i in overLapCount:
    for i in range(1,i):
        answer-=i  # 모든 경우의 수 - 중복되는 볼링공의 경우의 수

print(answer)
