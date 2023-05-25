import sys
from collections import deque
sys.stdin = open("input.txt", "r")

T= int(input())
for _ in range(T):
    num = int(input())
    profit = 0
    count = 0
    price_list = list(map(int, input().split()))
    maximum = max(price_list)
    for x in range(0,):
        print(x)
        if x == maximum and profit !=0 :
            profit+= (count*x)
            count = 0
        elif( x < maximum and maximum in price_list):
            profit-=x
            count+=1
        price_list.remove()

    print(profit, price_list)





# 1 1 3 2 1 4

'''
뒤에 더 큰 숫자가 있으면 사는게 이득
1 1 구매 총 이익 -2
3때도 삼 -5
2 때도 사고 1 삼 -8
4 대 풀매도 12
'''