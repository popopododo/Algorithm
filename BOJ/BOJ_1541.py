N = input()
s=[]
num=[]
sub=''
pre=0
answer=0

for x in N:
    # print(x)
    if x =="+" or x =="-":
        s.append(x)
        num.append(sub)
        sub=''
        continue
    sub += x
num.append(sub)

num.reverse()
s.reverse()

if(len(num)!=len(s)):
    answer+=int(num.pop())
for x in range(len(num)):
    if(s[x]=='+'):
        pre+=int(num[x])
    else:
        pre+=int(num[x])
        answer+=(-1)*pre
        pre=0
if(pre!=0):
    answer+=pre

print(answer)

