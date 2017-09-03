from heapq import *
node=0
val_dict={x:[] for x in range(1,201)}
nei_dict={x:[] for x in range(1,201)}
mylist=[]
myl=[]
with open("dijinp.txt") as myfile:
	for rel in myfile:
		node_flag=False
		for x in (rel.strip('\n')).split("\t"):
			if len(x)>0:
				if node_flag==False:
					node=int(x)
					node_flag=True
				else:
					nei_dict[node].append(int(x.split(',')[0]))
					val_dict[node].append(int(x.split(',')[1]))

new_dist=0
heap_list=[[0,1]]
checked={1:[0,1]}
final={}
while len(final)<node:
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
			#print(checked)
	#print(final)
	#print(heap_list)

target=[7,37,59,82,99,115,133,165,188,197]
print(len(final))
for key in final:
	if key in target:
		print(str(key)+" "+str(final[key]))
