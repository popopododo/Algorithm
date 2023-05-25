T=int(input())


for _ in range(T):
    stack=[]
    brackets=list(input())
    for i in brackets:
        stack.append(i)
        for j in range(0,len(stack)):
            if(stack.count()==1):
                continue
            else:

        print(stack)





