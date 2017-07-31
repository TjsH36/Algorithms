from sys import *
from random import *
v1list=[]
v2list=[]
edcost=[]
n=0
c=0
with open("clustering1.txt") as myfile:
	for rel in myfile:
		if c==0:
			n=int(rel.split('\n')[0])
			c=c+1
		else:
			x, y, z=[int(x) for x in rel.split()]
			v1list.append(x)
			v2list.append(y)
			edcost.append(z)
components=[i+1 for i in range(n)]
com=1234
while len(set(components))>3:
	ind=edcost.index(min(edcost))
	print(edcost[ind])
	edcost[ind]=maxsize
	u=(v1list[ind])
	v=(v2list[ind])
	if components[v-1]!=components[u-1]:
		for i in range(len(components)):
			if components[i]==components[u-1] or components[i]==components[v-1]:
				components[i]=com
