import sys
n=int(input())
num= list(map(int, sys.stdin.readline().split()))

def prime(n):
    i=2
    if(n==1):
        return False
    while i*i<=n:
        if(n%i==0):
            return False
        i+=1
    return True

for x in num:
    if(prime(x)==False):
        n-=1

print(n)