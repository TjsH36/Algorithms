wts=[]
lts=[]
diff=[]
fin=[]

def merge(fin,lts,wts):
	if len(fin)>1:
		m=len(fin)//2
		left=fin[:m]
		right=fin[m:]
		leftlt=lts[:m]
		rightlt=lts[m:]
		leftwt=wts[:m]
		rightwt=wts[m:]

		merge(left,leftlt,leftwt)
		merge(right,rightlt,rightwt)
		
		i=0
		j=0
		k=0
		while i < len(left) and j<len(right):
			if left[i]>right[j]:
				fin[k]=left[i]
				lts[k]=leftlt[i]
				wts[k]=leftwt[i]
				i=i+1
			elif left[i]<right[j]:
				fin[k]=right[j]
				lts[k]=rightlt[j]
				wts[k]=rightwt[j]
				j=j+1
			else:
				if leftwt[i]>rightwt[j]:
					fin[k]=left[i]
					lts[k]=leftlt[i]
					wts[k]=leftwt[i]
					i=i+1
				else:
					fin[k]=right[j]
					lts[k]=rightlt[j]
					wts[k]=rightwt[j]
					j=j+1
			k=k+1

		while i<len(left):
			fin[k]=left[i]
			lts[k]=leftlt[i]
			wts[k]=leftwt[i]
			i=i+1
			k=k+1
		while j<len(right):
			fin[k]=right[j]
			lts[k]=rightlt[j]
			wts[k]=rightwt[j]
			j=j+1
			k=k+1


c=0
with open("input.txt") as myfile:
	for rel in myfile:
		if c==0:
			n=int(rel)
			c+=1
		else:
			w, l= [int(x) for x in rel.split()]
			wts.append(w)
			lts.append(l)
for i in range(n):
	diff.append(wts[i]-lts[i])

merge(diff,lts,wts)
comp=0
wcomt=0
for i in range(len(lts)):
	comp=comp+lts[i]
	wcomt=wcomt + (wts[i]*comp)
print(wcomt)