burger=[]
soda=[]
for x in range(3):
    temp=int(input())
    burger.append(temp)
    burger.sort()
for x in range(2):
    temp=int(input())
    soda.append(temp)
    soda.sort()
print(burger[0]+soda[0]-50)