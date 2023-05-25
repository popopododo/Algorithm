N,M = map(int,input().split())
words=[]
count=0
for _ in range(N):
    temp= list(input())
    words.append(temp)
# print(words)

def MBTI(x,y,count=0):
    if(x<=-1 or x>=N or y<=-1 or y>=M):
        return False
    t=words[x][y]
    if((t=='E' or t=='I') and count==0):
        MBTI(x-1,y-1,count+1)
        MBTI(x , y - 1, count + 1)
        MBTI(x +1, y - 1, count + 1)
        MBTI(x +1, y, count + 1)
        MBTI(x +1, y + 1, count + 1)
        MBTI(x , y + 1, count + 1)
        MBTI(x - 1, y+1 , count + 1)
        MBTI(x - 1, y , count + 1)

    if((t=='N' or t=='S') and count==1):
        MBTI(x - 1, y - 1, count + 1)
        MBTI(x, y - 1, count + 1)
        MBTI(x + 1, y - 1, count + 1)
        MBTI(x + 1, y, count + 1)
        MBTI(x + 1, y + 1, count + 1)
        MBTI(x, y + 1, count + 1)
        MBTI(x - 1, y + 1, count + 1)
        MBTI(x - 1, y, count + 1)

    if ((t == 'F' or t == 'T') and count == 2):
        MBTI(x - 1, y - 1, count + 1)
        MBTI(x, y - 1, count + 1)
        MBTI(x + 1, y - 1, count + 1)
        MBTI(x + 1, y, count + 1)
        MBTI(x + 1, y + 1, count + 1)
        MBTI(x, y + 1, count + 1)
        MBTI(x - 1, y + 1, count + 1)
        MBTI(x - 1, y, count + 1)

    if ((t == 'P' or t == 'J') and count == 3):
        MBTI(x - 1, y - 1, count + 1)
        MBTI(x, y - 1, count + 1)
        MBTI(x + 1, y - 1, count + 1)
        MBTI(x + 1, y, count + 1)
        MBTI(x + 1, y + 1, count + 1)
        MBTI(x, y + 1, count + 1)
        MBTI(x - 1, y + 1, count + 1)
        MBTI(x - 1, y, count + 1)
        return True
    return False



for i in range(N):
    for j in range(M):
        if(MBTI(i,j)==True):
            count+=1
print(count)