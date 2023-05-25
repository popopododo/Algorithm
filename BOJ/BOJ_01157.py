n=input()
n=n.upper()
t={}
n=list(n)

for x in n:
    if(x not in t):
        t.setdefault(x,1)

    elif(x in t):
        t[x]+=1

def countmost(t):
    m=0
    word='-'
    temp=[]
    for key,val in t.items():
        if(val>=m):
            m=val
            word=key
            temp.append(val)
    if(len(temp)>=2):
        m=max(temp)
        temp.remove(max(temp))
        if(m==max(temp)):
            word='?'
    return word
print(countmost(t))
