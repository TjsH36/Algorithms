from heapq import *
from random import *
from sys import *
median=maxsize
mylist=[]
tom=0
with open("Median.txt") as myfile:
	for rel in myfile:
		l=int(rel.split('\n')[0])
		mylist.append(l)
mx=[]
mn=[]
heapify(mn)
heapify(mx)
for key in mylist:
	if key<median:
		x=-1*key
		heappush(mx,x)
	else:
		heappush(mn,key)
	if(len(mx)==len(mn)):
		median=-1*mx[0]
	elif len(mx)-len(mn)==1:
		median=-1*mx[0]
	elif len(mn)-len(mx)==1:
		median=mn[0]
	else:
		if len(mx)-len(mn)>1:
			x=heappop(mx)
			x=x*(-1)
			heappush(mn,x)
			median=-1*mx[0]
		else:
			x=heappop(mn)
			x=x*-1
			heappush(mx,x)
			median=-1*mx[0]
	tom=tom+median
print(tom%10000)