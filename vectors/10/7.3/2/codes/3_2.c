
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
int solve(int a,int b,int c)
{

	return (c-b)/a;
}
int main()
{
int a[10]={8,1};
int b[10]={2,-5};
char c[10]="k,-4";
int i;
for(i=0;i<2;i++)
{
	printf("%d\n",a[i]);
}
printf("\n");
for(i=0;i<2;i++)
{
	printf("%d\n",b[i]);
}
printf("\n");
printf("c=%s",c);
printf("\n");


int d[10];

for(i=0;i<2;i++)
{
	d[i]=b[i]-a[i];
}

printf("\n");

for(i=0;i<2;i++)
{
	printf("%d\n",d[i]);
}
printf("Solve for k :");
int e,f,g;
e=-1;
f=8;
g=6;
int x=solve(e,f,g);
printf("%d",x);
printf("\n");


return 0;
}
