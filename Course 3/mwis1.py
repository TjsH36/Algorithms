myl=[0]
flag=False
with open("mwis.txt") as myfile:
	for rel in myfile:
		n=int(rel)
		if flag==False:
			num=n
			flag=True
		else:
			myl.append(n)
subg=[0]
subg.append(myl[1])
for i in range(2,num+1):
	subg.append(max(subg[i-1],subg[i-2]+myl[i]))
#print(len(subg))
verts=[]
i=len(subg)-1
while i>=1:
	if subg[i-1]>subg[i-2]+myl[i]:
		i=i-1
	else:
		verts.append(i)
		i=i-2
verts.reverse()
inp=[1,2,3,4,17,117,517,997]
oup=[]
ind=0
for k in verts:
	if k in inp:
		for i in range(ind,inp.index(k)):
			oup.append(0)
			ind+=1
		oup.append(1)
		ind+=1
while len(oup)<len(inp):
	oup.append(0)
print(oup)



