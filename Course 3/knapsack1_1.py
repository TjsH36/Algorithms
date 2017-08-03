
flag=False
cap=0
items=0
value=[0]
weight=[0]
with open("knapsack1.txt") as myfile:
	for rel in myfile:
		if flag==False:
			cap, items=[int(x) for x in rel.split()]
			flag=True
		else:
			x, y=[int(x) for x in rel.split()]
			value.append(x)
			weight.append(y)
arr=[[0 for x in range(cap+1)] for x in range(items+1)]
for i in range(1,items+1):
	for x in range(cap+1):
		if weight[i]>x:
			arr[i][x]=arr[i-1][x]
		else:
			arr[i][x]=max(arr[i-1][x],arr[i-1][x-weight[i]]+value[i])
print(arr[items][cap])
