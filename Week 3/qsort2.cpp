#include<stdio.h>
#include<iostream>
#include<fstream>
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
	{int temp;
	temp=arr[h];
	arr[h]=arr[l];
	arr[l]=temp;
	int p=arr[l],cor,col;
	int cou=h-l;
	int i=l+1,j;
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
