N=int(input())
coin = list(map(int,input().split()))
# coin_list=[0]*(sum(coin)+1) dp 로 풀려다 포기
coin.sort()
answer=1 # 만들 수 있는 가장 작은 금액을 1로 설정

for i in coin:
    if(answer>=i):
        answer+=i
    else:  # 만들 수 있는 가장 작은 금액 보다 coin이 크면 못 만드는 금액
        break
print(answer)

