#include<stdio.h>
#include<math.h>
#include<iostream>
#include<string.h>
#include<sstream>
using namespace std;
string add(string s1,string s2,int n1);
string sub(string s1,string s2);

string mult(string a,string b);
int main()
{
	int n;
	cout<<"Enter length";
	cin>>n;
	string s1,s2;
	cin>>s1;
	cin>>s2;
	cout<<endl<<endl<<mult(s1,s2);
	return 0;
}

string mult(string ar1,string ar2)
{
	int n=ar1.length();
		
	if(n==2)
	{
		//converted into numbers
		int a,b,c,d;
		a=ar1[0]-'0';
		b=ar1[1]-'0';
		c=ar2[0]-'0';
		d=ar2[1]-'0';
		
		//mutliplication
		int t1=a*c;
		int t2=b*d;
		int t3=((a+b)*(c+d)-t1-t2);
		
		//zero strings
		string zs2="00";
		string zs1="0";
		
		//back to strings
		stringstream conv,tenv,penv;
		string te1,te2,te3;
		conv<<t1;
		te1=conv.str();
		tenv<<t2;
		te2=tenv.str();
		penv<<t3;
		te3=penv.str();
		
		//now adding zero strings
		string term1,term2,term3;
		term1=te1+zs2;
		int n1=term1.length();
		int n2=te2.length();
		if((n1-n2)==2)
		term2=zs2+te2;
		else
		term2=zs1+te2;
		term3=te3+zs1;
		
		//adding
		string temp;
		temp=add(term1,term2,term1.length());
		string sum;
		sum=add(temp,term3,term3.length());
		return sum;
	}
	
	else
	{
		cout<<"ENTER else 1st time"<<endl;
		int i;
		//breaking strings
		string semi1,semi2,semi3,semi4;
		semi1=ar1.substr(0,n/2);
		semi2=ar1.substr(n/2,n/2);
		semi3=ar2.substr(0,n/2);
		semi4=ar2.substr(n/2,n/2);
		
		//getting ac bd s
		string smat1,smat2,smat3;
		smat1=mult(semi1,semi3);
		smat2=mult(semi2,semi4);
		cout<<"a*c and b*d are founded"<<endl;
		cout<<"they are :"<<endl<<smat1<<endl<<smat2<<endl;
		
		//getting a+b c+d - -
		string ab=add(semi1,semi2,semi1.length());
		string cd=add(semi3,semi4,semi3.length());
		string tmp1,tmp2;
		tmp1=mult(ab,cd);
		tmp2=sub(tmp1,ab);
		smat3=sub(tmp2,cd);
		cout<<" big term also founded"<<endl<<"IT is :"<<endl<<smat3<<endl;
		
		//zero strings
		char zsn[n],zsh[n/2];
		for(i=0;i<n;i++)
		{
			zsn[i]='0';
		}
		for(i=0;i<n/2;i++)
		{
			zsh[i]='0';
		}
		
		
		//adding zeros to num
		string bigt1,bigt2,bigt3;
		bigt1=smat1+zsn;
		bigt3=smat3+zsh;
		int bigt1len=bigt1.length();
		int smalen=smat2.length();
		int dif=bigt1len-smalen;
		char zsdif[dif];
		for(i=0;i<dif;i++)
		{
			zsdif[i]='0';
		}
		bigt2=zsdif+smat2;
		
		//adding
		string tempb;
		tempb=add(bigt1,bigt2,bigt1.length());
		string sumb;
		sumb=add(tempb,bigt3,tempb.length());
		return sumb;
}

}
string add (string s1,string s2,int n1)
{
	int i,a,b,r,cr=0,st;
	char s3[n1],sf[n1+1];
	for(i=n1-1;i>=0;i--)
	{
		a=s1[i]-'0'; b=s2[i]-'0';
		r=a+b+cr;
		if(r>9)
		{
			st=r-10;
			s3[i]=st+'0';
			cr=1;
		}
		else
		{
			s3[i]=r+'0';
			cr=0;
		}
	}
	if(cr==1)
	{
		for(i=0;i<n1;i++)
		{
			sf[i+1]=s3[i];
		}
		sf[0]=1+'0';
		sf[n1+1]='\0';
		return sf;
	}
	else
	return s3;
}

string sub(string s1,string s2)
{
	int i,n1=s1.length(),n2=s2.length(),dif,n;
	if(n1==n2)
	n=n1;
	else 
	{
		n=n1;
		dif=n1-n2;
		char zsdif[dif];
		for(i=0;i<dif;i++)
		{
			zsdif[i]='0';
		}
		s2=zsdif+s2;
	}
	
	char s3[n];
	for(i=n-1;i>=0;i--)
	{
		int a=s1[i]-'0';
		int b=s2[i]-'0';
		if(a>b)
		s3[i]=(a-b)+'0';
		else
		{
			s3[i]=(a-b+10)+'0';
			int z=s1[i-1]-'0';
			z=z-1;
			s1[i-1]=z+'0';
		}
	}
	return s3;
}
