def digit(a):
    l=[]
    add=a
    leng=str(a)
    leng=len(leng)
    if(leng==1):
        l.append(a)
    elif(leng==2):
        l.append(a//10)
        l.append(a%10)
    elif(leng==3):
        l.append(a//100)
        a%=100
        l.append(a//10)
        l.append(a%10)
    elif(leng==4):
        l.append(a//1000)
        a%=1000
        l.append(a//100)
        a%=100
        l.append(a//10)
        l.append(a%10)
    else:
        return 0
    add+=sum(l)
    return add

res=[]
for count in range(1,10001):
    res.append(digit(count))
    res.sort()

for x in range(1,10000):        
    if x in res:
        continue
    else:
        print(x)
        