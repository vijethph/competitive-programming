/*lab program 5:Circular queue with integer values*/
#include<stdio.h>
#define MAX 3
int cnt=0;
void insert_rear(int *a,int *r)
{
	if((cnt)==MAX)
	{
		printf("circular queue overflow\n");	return;
	}
	printf("enter element:");
	(*r)=((*r)+1)%MAX;
	scanf("%d",a+(*r));
	cnt++;
}
void delete_front(int *a,int *f)
{
	if(cnt==0)
	{
		printf("circular queue underflow\n");	return;
	}
	printf("Element deleted:%d\n",a[(*f)]);
	(*f)=((*f)+1)%MAX;
	cnt--;
}
void display(int *a,int f)
{
	if(cnt==0)
	{
		printf("circular queue underflow\n");	return;
	}
	printf("Contents of queue are:\n");
	for(;cnt>0;cnt--)
	{
		printf("%d\n",a[f]);
		f=(f+1)%MAX;
	}
}
int main()
{
	int a[MAX],ch,f=0,r=-1;
	for(;;)
	{
		printf("1.Insert rear\t2.Delete front\t3.Display\t4.Exit\n");
		printf("Enter choice:");
		scanf("%d",&ch);
		switch(ch)
		{
			case 1:insert_rear(a,&r);	break;
			case 2:delete_front(a,&f);	break;
			case 3:display(a,f);	break;
			case 4:return 0;
		}
	}
}
