from sys import *
from heapq import *
v1list=[]
v2list=[]
edcost=[]

val_dict={x:[] for x in range(1,1001)}
nei_dict={x:[] for x in range(1,1001)}


c=False
v=0
ed=0
flags1=[None for i in range(v)]
with open("g3.txt") as myfile:
	for rel in myfile:
		if c==False:
			v, ed=[int(x) for x in rel.split()]
			for x in range(v):
				v1list.append(0)
				v2list.append(x+1)
				edcost.append(0)
			c=True
		else:
			x, y, z=[int(x) for x in rel.split()]
			v1list.append(x)
			v2list.append(y)
			edcost.append(z)

A=[[float("inf") for i in range(v+1)]]
verts=[i for i in range(v+1)]
for i in range(v):
	A.append([])
A[0][0]=0
mytails={i:[] for i in range(v+1)}
myedcosts={i:[] for i in range(v+1)}
for key in mytails:
	ind=[i for i,x in enumerate(v2list) if x==key]
	for a in ind:
		mytails[key].append(v1list[a])
		myedcosts[key].append(edcost[a])
def prevmin(i,v):
	arrval=[]
	fl=0
	for key in mytails[v]:
		arrval.append(A[i-1][key]+myedcosts[v][fl])
		fl+=1
	if len(arrval)>0:
		return min(arrval)
	else:
		return 0

magicverts=[]
for i in range(1,v+1):
	for x in verts:
		print(str(i)+" "+str(x))
		A[i].append(min(A[i-1][x],prevmin(i,x)))
chk=False		
for x in range(len(A[-1])):
	if A[-2][x]!=A[-1][x]:
		print("Negative cycle")
		chk=True
		break
if chk==False:
	magicverts=A[-1]
	orgv1=v1list[v:]
	orgv2=v2list[v:]
	orgedc=edcost[v:]
	newedc=[]

	for i in range(ed):
		newedc.append(orgedc[i]+magicverts[orgv1[i]]-magicverts[orgv2[i]])
	for i in range(ed):
		nei_dict[orgv1[i]].append(orgv2[i])
		val_dict[orgv1[i]].append(newedc[i])
		nei_dict[orgv2[i]].append(orgv1[i])
		val_dict[orgv2[i]].append(newedc[i])
'''
with open("magic.txt","w") as qwert:
	for i in range(v):
		  qwert.write(str(magicverts[i+1]))
		  qwert.write("\n")
'''


vert=0
min_final_val=0
checked={}
final={}
for ind in range(1,1000+1):
	print("dijks for vert "+str(ind))
	new_dist=0
	heap_list=[[0,ind]]
	checked.clear()
	checked[ind]=[0,ind]
	final.clear()
	while len(final)<1000:
		out=heappop(heap_list)
		#print(out)
		vert=out[1]
		dist=int(out[0])
		final[vert]=dist

		for x in range(len(nei_dict[vert])):
			if nei_dict[vert][x] not in final:
				#print(nei_dict[vert][x])
				new_dist=dist+val_dict[vert][x]
				new_entry=[new_dist,nei_dict[vert][x]]
				if nei_dict[vert][x] not in checked:
					checked[nei_dict[vert][x]]=new_entry
					heappush(heap_list,new_entry)
				elif new_dist<checked[nei_dict[vert][x]][0]:
					rem_entry=checked[nei_dict[vert][x]]
					checked[nei_dict[vert][x]]=new_entry
					heap_list.remove(rem_entry)
					heappush(heap_list,new_entry)
	final_val=[]
	for key in final:
		final_val.append(final[key]-magicverts[ind-1]+magicverts[key-1])
	if min_final_val>min(final_val):
		min_final_val=min(final_val)
	print(min(final_val))
	


print("shortest shortest path = "+str(min_final_val))
print("END!!!")