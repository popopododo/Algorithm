num=int(input())

def Arithmetic(num):
    count=99
    if num<=98:
       print(num)
    elif num>98 and num<=110:
        print(99)
    else:
        for x in range(111,num+1):
            bucket=[]
            bucket=list(str(x)) # 숫자를 각각 문자열로 분리해서 리스트에 정리 [1,1,0]
            for j in range(3):
                bucket[j]=int(bucket[j])
            if(bucket[1]-bucket[0]==bucket[2]-bucket[1]):
                count+=1
                # if(sum(bucket)*3==bucket[0]+(bucket[1]-bucket[2])*3):
        print(count)
                

Arithmetic(num)
