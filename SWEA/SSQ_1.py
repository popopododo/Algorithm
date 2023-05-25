import sys
sys.stdin = open('input_1.txt','r')
T= int(input())
'''
2
3
3 5 3
4
3 7 5 8
'''

for x in range(T):
    n = int(input())
    l = list(map(int, input().split()))
    answer = 0
    for i in range(n):
        for j in range(i+1,n):
            # print(i,j)
            answer+=(l[i]%l[j] + l[j]%l[i])

    print("#{} {}".format(x+1,answer))


