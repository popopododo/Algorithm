n=input()
leng= len(n) # 9
count=0
croatian=['c=','c-','dz=','d-','lj','nj','s=','z=']
for x in range(leng):
    if(n[x]=='c' or n[x]=='d'):
        if(x<=leng-1):
            if(n[x+1]=='-'):
                count+=1
                x+=1
            else:
                count+=1
        else:
            count+=1
    elif(n[x]=='c' or n[x]=='s' or n[x]=='z'):
        if(x<=leng-1):
            if(n[x+1]=='='):
                count+=1
                x+=1
            else:
                count+=1
        else:
            count+=1
    elif (n[x] == 'l' or n[x] == 'n'):
        if (x < leng - 1):
            if (n[x + 1] == 'j'):
                count += 1
                x += 1
            else:
                count += 1
        else:
            count+=1
    elif(n[x]=='d'):
        if(x<leng-3):
            if(n[x+1]=='z'):
                if(n[x+2]=='='):
                    count+=1
                    x+=2
                else:
                    count+=2

            else:
                pass
        else:
            count+=1

        '''
        elif(n[x]=='c' and n[x+1]=='=' or n[x]=='c'n[x+1]=='-' or n[x+1]=='j'):
            count+=1
            x+=2
        else:
            count+=1
'''
print(count)
