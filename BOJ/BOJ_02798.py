total,num= map(int, input().split())
cards = list(map(int, input().split()))
cards.sort(reverse=True)
# print(total,num,cards)
# 그리디 알고리즘 X 걍 노가다
candidates=[]

for first in range(0,total-2):
    for second in range(1,total-1):
        for third in range(2,total):
            if(first==second or first==third or second==third):
                continue
            if (cards[first]+cards[second]+cards[third]==num or cards[first]+cards[second]+cards[third]<num):
                candidates.append(cards[first]+cards[second]+cards[third])

candidates.sort(reverse=True)
print(candidates[0])
            
            


