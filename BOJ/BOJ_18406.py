N= input()
pre=0
post=0
halfLength=len(N)//2
for i in range(halfLength):
    pre+=int(N[i])
    post+=int(N[i+halfLength])

if(pre==post):
    print("LUCKY")
else:
    print("READY")