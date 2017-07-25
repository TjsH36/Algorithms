#include<stdio.h>
#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

int qsort(int *arr,int l,int h);
int main()
{
	int n,i,res;
	n=10000;
	int arr[n];
	ifstream myfile ("quick.txt");
	while(!myfile.eof())
	{
		myfile>>arr[i];
		i++;
	}
	myfile.close();
	res=qsort(arr,0,n-1);
	cout<<endl<<res;
	return 0;
}

int qsort(int *arr,int l,int h)
{
	if(l<h)
	{
	int a,b,c;
	a=arr[l];b=arr[h];c=arr[(l+h)/2];
	int p=max(min(max(a,b),c),min(a,b));
	int cor,col;
	int cou=h-l;
	int i=l+1,j,temp;
		if(p==b)
	{
		temp=arr[h];
		arr[h]=arr[l];
		arr[l]=temp;	
	}
	if(p==c)
	{
		temp=arr[(l+h)/2];
		arr[(l+h)/2]=arr[l];
		arr[l]=temp;
	}
	p=arr[l];
	for(j=l+1;j<=h;j++)
	{
		if(arr[j]<p)
		{temp=arr[j];
		arr[j]=arr[i];
		arr[i]=temp;
		i++;}
	}
	if(i>l+1)
	{
	temp=arr[i-1];
	arr[i-1]=p;
	arr[l]=temp;}
	cor=qsort(arr,i,h);
	col=qsort(arr,l,i-2);
	return (cou+col+cor);
	}
	else
	return 0;
}
