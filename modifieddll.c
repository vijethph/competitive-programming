/*multi-purpose DLL*/
/*Done By SilentKiller*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct node
{
	char str[30];
	struct node *prev,*next;
};
typedef struct node nd;
void insert_front(nd *h)
{
	nd *t=malloc(sizeof(nd));
	printf("enter string:");
	scanf("%s",t->str);
	t->next=t->prev=0;
	t->next=h->next;	t->prev=h;	h->next=t;
	if(h->next==h)
	{	h->prev=t;	return;	}
}
void insert_rear(nd *h)
{
	nd *t=malloc(sizeof(nd));	nd *c=0;
	printf("enter string:");
	scanf("%s",t->str);
	t->next=t->prev=0;
	t->next=h;	h->prev=t;
	if(h->next==h)
	{	t->prev=h;	h->next=t;	return;	}
	for(c=h->next;c->next!=h;c=c->next);
	c->next=t;	t->prev=c;
}
void delete_front(nd *h)
{
	nd *t=0;
	if(h->next==h)
	{
		printf("Doubly linked list is empty");	h->prev=h;
		return;
	}
	t=h->next;	h->next=t->next;
	printf("Node deleted is:\n");
	printf("%s\n",t->str);
	free(t);
}
void delete_rear(nd *h)
{
	nd *p=0,*c=0;
	if(h->next==h)
	{
		printf("Doubly linked list is empty");	h->prev=h;
		return;
	}
	for(c=h->next;c->next!=h;p=c,c=c->next);
	printf("Node deleted is:%s\n",c->str);
	free(c);
	if(p==h)
	{	h->next=h->prev=h;	return;	}
	p->next=h;		h->prev=p;
}
void it_display(nd *h)
{
	int count=0;
	nd *f=0;
	if(h->next==h)
	{
		printf("Doubly linked list is empty");
		return;
	}
	printf("String details are:\n");
	printf("Forward order:\n");
	for(f=h->next;f->next!=h;f=f->next)
	{
		printf("%s\t",f->str);
		count++;
	}
	printf("%s\t",f->str);
	printf("\nReverse order:\n");
	for(;f!=h;f=f->prev)
		printf("%s\t",f->str);
	printf("\nNumber of nodes in the list:%d\n",count+1);
}
void end_insert(nd *h)
{
	int i,n;
	nd *c=0,*r=0;
	printf("Enter the number of nodes:");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		nd *t=malloc(sizeof(nd));
		printf("Enter string:");
		scanf("%s",t->str);
		t->next=t->prev=0;
		if(h->next==h)
		{
			r=h->next=h->prev=t;	t->prev=h;	continue;
		}
		r->next=t;	t->prev=r;
		r=r->next;
	}
	r->next=h;	h->prev=r;
}
void insert_pos(nd *h)
{
	nd *t=0,*c=0,*p=0;
	int pos,count=1;
	t=(nd *)malloc(sizeof(nd));
	printf("Enter the position:");	scanf("%d",&pos);
	printf("Enter the string:");	scanf("%s",t->str);
	if(h->next==h)
	{	t->next=t->prev=h;	h->next=h->prev=h;	return;		}
	for(c=h->next;c->next!=h;c=c->next)
		count++;
	if(pos<=0||pos>count)
	{	printf("Invalid position\n");	return;	}
	for(count=1,c=h->next;count<pos;count++,p=c,c=c->next);
	t->prev=p;	t->next=c;	c->prev=p->next=t;
}
void delete_pos(nd *h)
{
	nd *t=0,*c=0,*p=0;
	int pos,i,count=1;
	if(h->next==h)
	{
		printf("Doubly linked list is empty");	h->prev=h;
		return;
	}
	printf("Enter the position:");	scanf("%d",&pos);
	for(c=h->next;c->next!=h;c=c->next)
		count++;
	if(pos<=0||pos>count)
	{	printf("Invalid position\n");	return;	}
	for(count=1,c=h->next;count<pos;count++,p=c,c=c->next);
	t=c;	p->next=t->next;	c=c->next;	c->prev=t->prev;
	printf("Node deleted;%s\n",t->str);
	free(t);
}
void arrange(nd *h)
{
	nd *p,*c=0;
	char tmp[30];
	if(h->next==h)
	{
		printf("Doubly linked list is empty");
		return;
	}
	for(c=h->next;c->next!=h;c=c->next)
		for(p=h->next;p->next!=h;p=p->next)
			if(strcmp(p->str,(p->next)->str)>0)
			{
				strcpy(tmp,p->str);
				strcpy(p->str,(p->next)->str);
				strcpy((p->next)->str,tmp);
			}
	printf("Strings are arranged\n");
}
void reverse(nd *h)
{
	nd *p=0,*c=h->next;
	if(h->next==h)
	{
		printf("Doubly linked list is empty");
		return;
	}
	if((h->next)->next==h)
		return;
	while(c!=h)
	{
		p=c->prev;
		c->prev=c->next;
		c->next=p;
		c=c->prev;
	}
	if(p!=h)
		h->next=p->prev;
	printf("Strings reversed\n");
}
void revf_display(nd *h,nd *t)
{
	if(h->next==t)
	{
		printf("%s\n",h->str);
		return;
	}
	printf("%s ",h->str);
	revf_display(h->next,t);
}
void revr_display(nd *h,nd *t)
{
	if(h->prev==t)
	{
		printf("%s\n",h->str);
		return;
	}
	printf("%s ",h->str);
	revr_display(h->prev,t);
}
int main()
{
	int ch;
	nd head={"\0",&head,&head};
	nd p,*t=0;
	for(;;)
	{
		printf("1.End Insert\n2.Insert Front\t3.Insert Rear\t4.Insert at Position\n5.Delete Front\t6.Delete Rear\t7.Delete at Position\n8.Arrange\t9.Reverse\t10.Iterative Display\n11.Recursive Display-Forward\t12.Recursive Display-Backward\n13.Exit\n");
		printf("Enter choice:");	scanf("%d",&ch);
		switch(ch)
		{
			case 1:end_insert(&head);		break;
			case 2:insert_front(&head);		break;
			case 3:insert_rear(&head);		break;
			case 4:insert_pos(&head);		break;
			case 5:delete_front(&head);		break;
			case 6:delete_rear(&head);		break;
			case 7:delete_pos(&head);		break;
			case 8:arrange(&head);			break;
			case 9:reverse(&head);			break;
			case 10:it_display(&head);		break;
			case 11:p=head;	t=&head;	revf_display(&p,t);		break;
			case 12:p=head;	t=&head;	revr_display(&p,t);		break;
			case 13:return 0;
			default: printf("Invalid option\n");
		}
	}
}
