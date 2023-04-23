/*lab program 11: DLL on Employee Record*/
#include<stdio.h>
#include<stdlib.h>
struct employee
{
	char ssn[20],name[20],dep[20],des[20];
	long int sal,phno;
	struct employee *prev,*next;
};
typedef struct employee nd;
nd * insert_front(nd *f)
{
	nd *t=malloc(sizeof(nd));
	printf("enter ssn, name, department, designation, salary, phone number:\n");
	scanf("%s%s%s%s%ld%ld",t->ssn,t->name,t->dep,t->des,&(t->sal),&(t->phno));
	t->next=t->prev=0;
	if(f==0)
		return t;
	t->prev=0;	t->next=f;
	f->prev=t;
	return t;
}
nd * insert_rear(nd *f)
{
	nd *t=malloc(sizeof(nd));	nd *c=0;
	printf("enter ssn, name, department, designation, salary, phone number:\n");
	scanf("%s%s%s%s%ld%ld",t->ssn,t->name,t->dep,t->des,&(t->sal),&(t->phno));
	t->next=t->prev=0;
	if(f==0)
		return t;
	for(c=f;c->next!=0;c=c->next);
	c->next=t;	t->prev=c;
	return f;
}
nd * delete_front(nd *f)
{
	nd *t=0;
	if(f==0)
	{
		printf("Doubly linked list is empty");
		return f;
	}
	t=f;	f=f->next;	f->prev=0;
	printf("Node deleted is:\n");
	printf("%s %s %s %s %ld %ld \n",t->ssn,t->name,t->dep,t->des,t->sal,t->phno);
	free(t);	return f;
}
nd * delete_rear(nd *f)
{
	nd *p=0,*c=0;
	if(f==0)
	{
		printf("Doubly linked list is empty");
		return f;
	}
	for(c=f;c->next!=0;p=c,c=c->next);
	printf("Node deleted is:\n");
	printf("%s %s %s %s %ld %ld \n",c->ssn,c->name,c->dep,c->des,c->sal,c->phno);
	free(c);
	if(p==0)
		return 0;
	p->next=0;	return f;
}
void display(nd *f)
{
	int count=0;
	if(f==0)
	{
		printf("Doubly linked list is empty");
		return;
	}
	printf("Employee details are:\n");
	printf("Forward order:\n");
	for(;f->next;f=f->next)
	{
		printf("%s %s %s %s %ld %ld\n",f->ssn,f->name,f->dep,f->des,f->sal,f->phno);
		count++;
		printf("*****************\n");
	}
	printf("%s %s %s %s %ld %ld \n",f->ssn,f->name,f->dep,f->des,f->sal,f->phno);
	printf("Reverse order:\n");
	for(;f!=0;f=f->prev)
	{
		printf("%s %s %s %s %ld %ld \n",f->ssn,f->name,f->dep,f->des,f->sal,f->phno);
		printf("*****************\n");
	}
	printf("Number of nodes in the list:%d\n",count+1);
}
nd * end_insert(nd *f)
{
	int i,n;
	nd *c=0,*r=0;
	printf("Enter the number of nodes:");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		nd *t=malloc(sizeof(nd));
		printf("enter ssn, name, department, designation, salary, phone number:\n");
		scanf("%s%s%s%s%ld%ld",t->ssn,t->name,t->dep,t->des,&(t->sal),&(t->phno));
		t->next=t->prev=0;
		if(f==0)
		{
			r=f=t;	continue;
		}
		r->next=t;	t->prev=r;
		r=r->next;
	}
	return f;
}
int main()
{
	int ch;
	nd *f=0;
	for(;;)
	{
		printf("1.End Insert\t2.Insert Front\t3.Insert Rear\n4.Delete Front\t5.Delete Rear\t6.Display\n7.Exit\n");
		printf("Enter choice:");	scanf("%d",&ch);
		switch(ch)
		{
			case 1:f=end_insert(f);		break;
			case 2:f=insert_front(f);	break;
			case 3:f=insert_rear(f);	break;
			case 4:f=delete_front(f);	break;
			case 5:f=delete_rear(f);	break;
			case 6:display(f);			break;
			case 7:free(f);		return 0;
			default: printf("Invalid option\n");
		}
	}
}
