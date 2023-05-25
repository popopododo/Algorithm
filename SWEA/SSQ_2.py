import sys
import math
sys.stdin = open('input_2.txt','r')
T= int(input())
'''
4
1
3
1
2
4
7 3 8 4
4
7 4 8 4
'''

for test_case in range(1, T + 1):
    n = int(input())
    l = list(map(int,input().split()))
    answer = 0
    oddEvenCount = 0
    Flag = 0
    if (n < 3):
        if (n == 2):
            if ((l[0] - l[1]) % 2 == 0):
                answer = -1
        print("#{} {}".format(test_case, answer))
        continue

    for x in l:
        if(x%2==0):
            oddEvenCount +=1
        else:
            oddEvenCount-=1
    if(abs(oddEvenCount)==0 or abs(oddEvenCount)==1):
        for i in range(n-1):
            if((l[i]-l[i+1])%2==0):
                answer+=1
            elif((l[i]-l[i+1])%2==1):
                l[i],l[i+1]= l[i+1],l[i]
        print("#{} {}".format(test_case, answer))


    else:
        answer= -1
        print("#{} {}".format(test_case, answer))


'''
for test_case in range(1, T + 1):
    n = int(input())
    l = list(map(int,input().split()))
    answer = 0
    oddEvenCount = 0
    Flag = 0
    if (n < 3):
        if (n == 2):
            if ((l[0] - l[1]) % 2 == 0):
                answer = -1
        print("#{} {}".format(test_case, answer))
        continue

    for x in l:
        if(x%2==0):
            oddEvenCount +=1
        else:
            oddEvenCount-=1
    if(abs(oddEvenCount)==0 or abs(oddEvenCount)==1):
        while(True):
            if(Flag==n-2):
                break
            Flag = 0
            for i in range(n-2):
                if((l[i]-l[i+1])%2==1 and (l[i+1]-l[i+2])%2==1): # 홀 짝 홀 or 짝 홀 짝
                    Flag+=1
                else:
                    if((l[i]-l[i+1])%2==0 and (l[i+1]-l[i+2])%2==1): # 홀 홀 짝 or 짝 짝 홀
                        l[i+1],l[i+2] = l[i+2],l[i+1]
                        answer+=1
                        break
        print("#{} {}".format(test_case, answer))
'''
