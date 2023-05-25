N = int(input())

road = tuple(map(int, input().split()))

fuel_price = list(map(int, input().split()))

total_price = 0


total_price = road[0] * fuel_price[0]

# fuel_price.pop()

min_cost = fuel_price[0]


x = 1

while(x< N-1):
    if (min_cost <= fuel_price[x] ):
        total_price += min_cost *road[x]
        # print(total_price)
    else:
        total_price+= fuel_price[x] * road[x]
        min_cost = fuel_price[x]
    x+=1

print(total_price)



















