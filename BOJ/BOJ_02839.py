n= int(input())

def Sugar(n): # 24
    three=0
    five=n//5 # five=4
    n%=5      # n=4
    while(five>=0): # 4 3
        if(n%3==0): 
            three=n//3 # three=3
            n%=3  # n=0
            break
        five-=1 # five= 3
        n+=5 # n=9
    print(three+five)
    
Sugar(n)


    

        


        
                
                


