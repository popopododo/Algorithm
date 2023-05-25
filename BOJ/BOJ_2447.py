N = int(input())

def factorial_star(x):
    if(x==1):
        return
    for i in range(x):
        for j in range(x):
            if(i ==x//3 and j==x//3):
                print(" ",end='')
            else:
                print("*",end='')
        print()


factorial_star(N)
