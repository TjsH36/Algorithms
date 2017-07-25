#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string>
#include <stdlib.h>
#include <time.h>
using namespace std;

struct edge{
	int src,dest;
}eds[2600];

struct subset{
	int parent;
	int rank;
}sts[200];

int find(struct subset *sts,int i);
void add(struct subset *sts,int x,int y);

int main()
{
	srand(time(NULL));
	int arr[200][42];
	char c;
	int i=0,j=0,ed=0,k=0;
	
	//reading input
	ifstream myfile ("input.txt");
	while(!myfile.eof())
	{
		if(j==0)
		{
			myfile>>arr[i][j];
			j++;
		}
		else
		{
		myfile.get(c);
		if(c=='\n')
		{
			for(;j<42;j++)
			{
				arr[i][j]=0;
			}
			i++;
			j=0;
		}
		myfile>>arr[i][j];
		j++;}
	}
		for(;j<42;j++)
			{
				arr[i][j]=0;
			}
	myfile.close();
	
	

	//Algo started~!!!!!
	// getting edges
	for(i=0;i<200;i++)
	{
		for(j=1;j<42;j++)
		{
			if(arr[i][j]!=0)
			{
				if(arr[i][j]>i)
				{
					eds[ed].src=i;
					eds[ed].dest=arr[i][j];
					ed++;
				}
			}
		}
	}
	//creating vertex subsets
	for(j=0;j<200;j++)
	{
		sts[j].parent=j;
		sts[j].rank=0;
	}
	int vertices=200;
	while(vertices>2)
	{
		//selecting random edge
		int i=rand()%ed;
		
		//find vertices(subests) of this edge
		int sb1=find(sts,eds[i].src);
		int sb2=find(sts,eds[i].dest);
		
		//contracting!!!
		if(sb1!=sb2)
		{
		vertices--;
		add(sts,sb1,sb2);}
	}
	int cutedges=0;
	for(k=0;k<ed;k++)
	{
		int s1=find(sts,eds[k].src);
		int s2=find(sts,eds[k].dest);
		if(s1!=s2)
		cutedges++;
	}
	cout<<"answer:"<<endl<<cutedges;
	return 0;
}




int find(struct subset *sts,int i)
{
	if(sts[i].parent!=i)
	sts[i].parent=find(sts,sts[i].parent);
	return sts[i].parent;
}

void add(struct subset *sts,int x,int y)
{
	int xroot=find(sts,x);
	int yroot=find(sts,y);
	
	if(sts[xroot].rank<sts[yroot].rank)
	sts[xroot].parent=yroot;
	else if(sts[xroot].rank>sts[yroot].rank)
	sts[yroot].parent=xroot;
	else
	{
		sts[yroot].parent=xroot;
		sts[xroot].rank++;
	}
}

