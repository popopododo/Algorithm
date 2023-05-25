N,K = map(int,input().split())
answer=0
while(N!=1):
    targetNum = (N//K)*K # N보다 작은 가장 큰 K의 배수
    answer+= N-targetNum # targetNum을 만들 때 까지 -1 한 횟수
    N=targetNum
    while(N%K==0): # N이 K로 나누어 떨어지지 않을 때 까지
        N=N//K
        answer+=1  # 나눠준 횟수 만큼 더함
print(answer)



