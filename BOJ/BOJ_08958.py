T=int(input())
while T>0:
    result=input()
    count=0
    extra=0
    for x in result:
        if x=="X":
            extra=0
        else:
            extra+=1
            count+=extra
    print(count, end="\n")
            
    T-=1


