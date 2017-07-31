
clustno=[0]*pow(2,24)
c=0
tem=0
numbers=[]
with open("clustering_big.txt") as myfile:
	cluster=1
	for rel in myfile:
		if c==0:
			n, lab=[int(x) for x in rel.split()]
			c+=1
		else:
			s=(rel.split('\n')[0])
			tem=int(s.replace(' ',''),base=2)
			numbers.append(tem)
			clustno[tem]=cluster
			cluster+=1
print(len(numbers))
hamming_no=[0]*300
k=0
for i in range(lab):
	for j in range(i,lab):
		bit1=1<<i
		bit2=1<<j
		hamming_no[k]=bit1|bit2
		k+=1
def nbr(x):
	result=[]
	for i in hamming_no:
		if clustno[x^i]!=0:
			result.append(x^i)
	return result
totalclust=[]
for i in numbers:
	if clustno[i] in totalclust:
		continue
	n1=[i]
	while len(n1)!=0:
		n2=[]
		for j in n1:
			for k in nbr(j):
				if clustno[k]!=clustno[i]:
					n2.append(k)
					clustno[k]=clustno[i]
		n1=n2
	totalclust.append(clustno[i])
print(len(totalclust))