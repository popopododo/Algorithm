S = input()
answer=0
flag=False
if(S[0]=='0' or S[0]=='1'): # 첫 번째 숫자가 0 또는 1 이면 answer를 1로
    answer=1
else:
    answer= int(S[0])
for i in range(1,len(S)):
    if(S[i]=='0' or S[i]=='1'):
        answer+=int(S[i])
    else: # 한 번이라도 숫자를 곱하면 flag를 True로, 즉 answer를 0으로 할 필요가 없
        flag= True
        answer*=int(S[i])

if(flag==False): # 모든 숫자가 0 이면 answer를 0 으로
    answer=0

print(answer)

