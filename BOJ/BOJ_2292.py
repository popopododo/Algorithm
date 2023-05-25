n=int(input())
division = (n-2)/6
temp=0
i=0
if(n==1):
    print(1)
else:
    while(True):
        i+=1
        if (division < temp and i !=1):
            print(i)
            break
        elif (division == temp and i!=1):
            print(i + 1)
            break
        temp += i


