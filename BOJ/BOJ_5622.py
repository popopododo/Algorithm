n=input()
answer=0
dial = [('A','B','C'),
        ('D','E','F'),
        ('G','H','I'),
        ('J','K','L'),
        ('M','N','O'),
        ('P','Q','R','S'),
        ('T','U','V'),
        ('W','X','Y','Z')]

for x in n:
    for y in dial:
        if(x in y):
            answer+=dial.index(y)+3
print(answer)