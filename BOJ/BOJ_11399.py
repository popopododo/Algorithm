N= int(input())
k=list(map(int,input().split()))

wait_time=0
elapsed_time=0
pre_time=0
k.sort()

for x in range(N):
    elapsed_time+=k[x]
    for y in range(x):
        wait_time+=k[y]


print(elapsed_time+wait_time)
