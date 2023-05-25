N=int(input())

stack=[]

for i in range(N):
    num=int(input())
    if(num==0):
        if(stack):
            stack.pop()
            continue
        else:
            continue
    stack.append(num)

# print(stack)
print(sum(stack))
