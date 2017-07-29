#include<stdio.h>
#include<iostream>
#include<fstream>
using namespace std;

struct vert
{
	int flag=0,n,lead=0,fac=0;
	int arr[100];
};

struct graph
{
	int v;
	vert * nodes;
};

int main()
{
	graph* g = new graph;
	g->v=;
	g->nodes = new vert[v];
	long a,b,count=0;
	char c,d,e;
	int sno=1,fixi=0;
	ifstream myfile ("SCC.txt");
	while(!myfile.eof())
	{
		myfile>>a;
		if(a>sno)
		{sno++;
		g->nodes.n=fixi;
		 fixi=0;}
		myfile.get(c);
		myfile>>g->nodes[a].arr[fixi];
		fixi++;
		myfile.get(d);
		myfile.get(e);
		if(e=='\n')
		count++;
	}
	cout<<count;
	return 0;
}
