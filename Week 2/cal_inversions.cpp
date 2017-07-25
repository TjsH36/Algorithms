#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;

long long count(int *a,int l,int h);
long long  merge(int *a,int l,int m,int h);
int main()
{
	int i,n=100000;
	int arr[n];
	ifstream myfile ("inversions.txt");
	while(!myfile.eof())
	{
		myfile>>arr[i];
		i++;
	}
	myfile.close();
	long long res=count(arr,0,n-1);
	cout<<endl<<res;
	return 0;
}

long long  count(int *a,int l,int h)
{
	
	if(l<h)
	{
		int m=(l+h)/2;
	long long  x,y,z;
		x=count(a,l,m);
		y=count(a,m+1,h);
		z=merge(a,l,m,h);
		return x+y+z;
	}
	else
	{
	return 0;
	}
}

long long merge(int *a,int l,int m,int h)
{
	int i,j,k;
	long long co=0;
	int n1=m-l+1;
	int n2=h-m;
	int la[n1],ra[n2];
	for(i=0;i<n1;i++)
	la[i]=a[l+i];
	for(j=0;j<n2;j++)
	ra[j]=a[m+1+j];
	i=0;j=0;k=l;
	while(i<n1&&j<n2)
	{
		if(la[i]<=ra[j])
		{
			a[k]=la[i];
			i++;
		}
		else
		{
			a[k]=ra[j];
			j++;
			co=co+n1-i;
		}
		k++;
	}
	while(i<n1)
	{
		a[k]=la[i];
		i++;
		k++;
	}
	while(j<n2)
	{
		a[k]=ra[j];
		j++;
		k++;
	}
	return co;
}
