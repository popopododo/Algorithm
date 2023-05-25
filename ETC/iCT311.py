N=int(input())
guild = list(map(int,input().split()))
answer=0
guild.sort()
while(len(guild)>1): # 길드에 한 명 이상의 모험가가 남았을 때 까지
    groupMaxFear = guild[-1]
    guild = guild[:-groupMaxFear] # 길드에서 공포도가 제일 큰 모험가의 수 만큼 길드에서 제외
    # print(guild)
    answer+=1
print(answer)
