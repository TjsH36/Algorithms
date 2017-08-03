from random import *
"""
myl=[randint(1,20) for x in range(10)]
print(myl)
"""
flag=False
num=0
myl=[]
with open("huffman.txt") as myfile:
	for rel in myfile:
		n=int(rel)
		if flag==False:
			num=n
			flag=True
		else:
			myl.append(n)
print(len(myl))
class Tree(object):
	def __init__(self,data=None,left=None,right=None):
		self.left=left
		self.right=right
		self.data=data

mytree=[]
midnodes=[]
def disp(node):
	if node:
		print(node.data)
		disp(node.left)
		disp(node.right)
def max_len(node):
	if node:
		return max(max_len(node.left),max_len(node.right))+1
	else:
		return 0
def min_len(node):
	if node:
		return min(min_len(node.left),min_len(node.right))+1
	else:
		return 0
k=0
while len(myl+midnodes)>1:
	c1=0
	c2=0
	n1=min(myl+midnodes)
	if n1 in myl:
		#print("n1"+" "+str(myl.index(n1)))
		del myl[myl.index(n1)]
	elif n1 in midnodes:
		#print("n1"+" "+str(midnodes.index(n1)))
		del midnodes[midnodes.index(n1)]
		c1+=1
	n2=min(myl+midnodes)
	if n2 in myl:
		#print("n2"+" "+str(myl.index(n2)))
		del myl[myl.index(n2)]
	elif n2 in midnodes:
		#print("n2"+" "+str(midnodes.index(n2)))
		del midnodes[midnodes.index(n2)]
		c2+=1
	midnodes.append(n1+n2)
	if c1==0 and c2==0:
		mytree.append(Tree(n1+n2,Tree(n1),Tree(n2)))
	elif c1==1 and c2==1:
		mytree.append(Tree(n1+n2,mytree[k],mytree[k+1]))
		k+=2
	elif c1==1 and c2==0:
		mytree.append(Tree(n1+n2,mytree[k],Tree(n2)))
		k+=1
	else:
		mytree.append(Tree(n1+n2,Tree(n1),mytree[k]))
		k+=1
#disp(mytree[-1])
print(max_len(mytree[-1])-1)
print(min_len(mytree[-1])-1)