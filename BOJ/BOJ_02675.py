T=int(input())
l=[]
for x in range(T):
	i,j=map(str,input().split())
	i=int(i)
	l.append(i)
	l.append(j)

# print(l)

for x in range(1,len(l),2): # x = 1,3
	for y in l[x]: # y= 1,3
		for z in range(l[x-1]):
			print(y, sep='',end='')
	print()



'''
for y in j:
	for x in range(i):
		print(y,sep='',end='')
print()
'''


