/*multi-function binary tree*/
/*Done By SilentKiller*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct node
{
	struct node *left,*right;
	char info[10];
};
typedef struct node nd;
nd * insert_node(nd *f)
{
	nd *t,*p,*c;
	int i,j,n;
	char str[20];
	FILE *fp;
	fp=fopen("bintree.txt","r");
	printf("Reading the number of nodes in tree:");
	fscanf(fp,"%d",&n);
	t=(nd *)malloc(sizeof(nd));
	printf("Reading root value:");
	fscanf(fp,"%s",t->info);
	t->left=t->right=0;	f=t;
	for(i=0;i<n;i++)
	{
		t=(nd *)malloc(sizeof(nd));
		printf("Reading node info\n");
		fscanf(fp,"%s",t->info);
		t->left=t->right=0;
		printf("Reading string to insert node:");
		fscanf(fp,"%s",str);
		for(p=0,c=f,j=0;j<strlen(str);j++)
		{
			p=c;
			if(str[j]=='L')
				c=c->left;
			else
				c=c->right;
		}
		if(str[strlen(str)-1]=='L')
			p->left=t;
		else
			p->right=t;
	}
	return f;
}
void preorder(nd *r)
{
	if(r)
	{
		printf("%s ",r->info);
		preorder(r->left);
		preorder(r->right);
	}
}
void inorder(nd *r)
{
	if(r)
	{
		inorder(r->left);
		printf("%s ",r->info);
		inorder(r->right);
	}
}
void postorder(nd *r)
{
	if(r)
	{
		postorder(r->left);
		postorder(r->right);
		printf("%s ",r->info);
	}
}
void it_inorder(nd *r)
{
	nd *st[20]={0},*c=0;
	int top=-1;
	if(!r)
	{	printf("Binary tree is empty\n");	return;	}
	c=r;
	for(;;)
	{
		while(c!=0)
		{	st[++top]=c;	c=c->left;	}
		if(top!=-1)
		{
			c=st[top--];
			printf("%s ",c->info);
			c=c->right;
		}
		else
			return;
	}
}
void levorder(nd *root)
{
	int f=0,r=-1;
	nd *c,*q[20]={0};
	if(!root)
	{	printf("Binary tree is empty\n");	return;	}
	q[++r]=root;
	for(;;)
	{
		c=q[f++];
		if(c)
		{
			printf("%s ",c->info);
			if(c->left)
				q[++r]=c->left;
			if(c->right)
				q[++r]=c->right;
		}
		else
			break;
	}
}
int main()
{
	nd *r=0;
	r=insert_node(r);
	printf("\nPreorder traversal:\n");
	preorder(r);
	printf("\nPostorder traversal:\n");
	postorder(r);
	printf("\nInorder traversal:\n");
	inorder(r);
	printf("\nIterative inorder traversal:\n");
	it_inorder(r);
	printf("\nLevel order traversal:\n");
	levorder(r);
	return 0;
}

