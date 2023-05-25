string=list(input())
a = ['-1' for x in range(26)]

for x in range(0,len(string)):
    temp=ord(string[x])-97
    if(a[temp]=='-1'):
        a[temp]=x

for x in a:
    print(x, end=" ")
