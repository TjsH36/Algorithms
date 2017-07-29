#include<stdio.h>
#include<iostream>
#include<fstream>
#include<unordered_set>

using namespace std;

int main();

unordered_set<long long> htab;

/*bool check(int i)
{
	unordered_set<long long>::iterator it,temp;
	for(it=htab.begin();it!=htab.end();++it)
	{
		temp=htab.find(i-(*it));
		if(temp!=htab.end())
		return true;
	}
	return false;
}*/
int main()
{
	unordered_set<long long>::iterator it;
	unordered_set<long long>::iterator temp;
	int i;
	long long a;
	ifstream myfile ("input.txt");
	while(!myfile.eof())
	{
		myfile>>a;
		htab.insert(a);
	}
	cout<<"hehehe";
	long count=0;
	for(i=-10000;i<=10000;i++)
	{
		cout<<i<<endl;
	for(it=htab.begin();it!=htab.end();++it)
	{
		temp=htab.find(i-(*it));
		if(temp!=htab.end())
		{		count++;
		break;}
	/*	if(check(i))
			count++;*/
	}}
	cout<<count;
	return 0;
} 
