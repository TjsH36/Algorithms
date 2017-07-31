import sys
e1=[]
e2=[]
cost=[]
acc=[]
checkarr=[False for x in range(500)]
checkarr[0]=True

with open("edges.txt") as myfile:
	c=0
	for rel in myfile:
		if c==0:
			v, ed= [int(x) for x in rel.split()]
			c=c+1
		else:
			w, l, k= [int(x) for x in rel.split()]
			e1.append(w)
			e2.append(l)
			cost.append(k)
print(v)
cv=[1]
totalminlen=0


def smallify(u,m):
	lastvis=0
	for i in range(len(e1)):
		if u==e1[i]:
			if checkarr[e2[i]-1]==False:
				if cost[i]<m:
					m=cost[i]
					lastvis=e2[i]
		elif u==e2[i]:
			if checkarr[e1[i]-1]==False:
				if cost[i]<m:
					m=cost[i]
					lastvis=e1[i]
	if lastvis>0:
		acc.append(lastvis)
	return m


while len(cv)!=500:
	cheaped=sys.maxsize
	for key in cv:
		req=smallify(key,cheaped)
		if(req<cheaped):
			cheaped=req
	checkarr[acc[-1]-1]=True
	cv.append(acc[-1])
	totalminlen=totalminlen+cheaped
print(cv)
print(totalminlen)
	