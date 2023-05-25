'''
def solution(number, k):
    answer=''
    number=list(number)


    # strNum= str(number)
    firstDigit=number[0] # 제일 큰 숫자의 자릿 수 저장
    while(k!=0):
        for x in range(1, len(number)-1): # 첫번째 자릿 수 추출
            if(number[x]>number[x-1] and number[x]>=number[x+1]):
                firstDigit= max(firstDigit, number[x])
                firstPos= x
                k=k-firstPos
                break

        number= number[firstPos:]

        # 남은 k 만큼 자릿 수 제거

        for x in range(1,len(number)-3):
            if(x==len(number)-3 and k!=0):
                if(x)

            if(number[x]<number[x-1] and number[x]<number[x+1]):
                number.pop(x)
                k-=1



    pre= number[0]
    while(k!=0):
        for x in range(1,len(number)):
            if(number[x]>)
    for x in number:
        answer+=x
    return answer
'''

