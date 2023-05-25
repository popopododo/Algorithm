N= int(input())
def fibo(x):
    # x = 0 을 도달했을 때 재귀함수 종료
    if(x == 2 or x==1):
        return 1
    if(x==0):
        return 0
    return fibo(x-1)+fibo(x-2)

print(fibo(N))



