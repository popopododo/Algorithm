import sys
sys.stdin = open("../Implementation/input.txt", "r")

T=int(input())

for test_case in range(1, T + 1):
    oNum = int(input())
    num= list(str(oNum))
    i=2
    possibleList=[]
    sortedNum=''
    num.sort(reverse=True)
    for x in num:
        sortedNum+=str(x)
    sortedNum=int(sortedNum)
    while(oNum*i<=sortedNum):
        possibleList.append(list(str(oNum*i)))
        i+=1
    # print(possibleList)
    if(len(possibleList)==0):
        print("#{} impossible".format(T))
    else:
        for x in possibleList:
            # print(sorted(x,reverse=True))
            if(sorted(x,reverse=True) == list(str(sortedNum))):
                print("#{} possible".format(T))
                break
        else:
            print("#{} impossible".format(T))