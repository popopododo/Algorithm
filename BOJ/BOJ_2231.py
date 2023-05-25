n=input()

n = int(n)
min = n
con = False

for i in range(n,0,-1):

    temp=0
    temp+=i
    ori_ind=i
    size = len(str(i))
    for x in range(size):
        temp+= i%10
        i=i//10

    if(temp == n and ori_ind < min ):
        min = ori_ind
        con = True
if(con == True):
    print(min)
else:
    print(0)

