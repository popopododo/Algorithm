N,M,K = map(int,input().split())
n = list(map(int,input().split()))
n.sort() # 슬라이싱을 위해 sort
# max * M하고 가장 가까운 K의 배수 + secondMax * M mod K
print(n[-1]*((M//K)*K) + n[-2]*(M%K))



