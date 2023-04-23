/*lab program 10: multi-function binary search tree*/
/*Done By SilentKiller*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct node
{
	struct node *left,*right;
	int info;
};
typedef struct node nd;
void inorder(nd *r)
{
	if(r)
	{
		inorder(r->left);
		printf("%d ",r->info);
		inorder(r->right);
	}
}
nd * insert(nd *root,int key)
{
	nd *c=root,*p=0;
	nd *t=(nd *)malloc(sizeof(nd));
	t->info=key;	t->left=t->right=0;
	if(!c)
		return t;
	while(c)
	{
		if(t->info==c->info)
		{	printf("Redundancy\n");	free(t);	return root;	}
		p=c;
		if(t->info<c->info)
			c=c->left;
		else
			c=c->right;
	}
	if(t->info<p->info)
		p->left=t;
	else
		p->right=t;
	return root;
}
void itersearch(nd *root,int key)
{
	if(!root)
	{	printf("Binary search tree is empty\n");	return;	}
	while(root)
	{
		if(key==root->info)
		{	printf("Successful search\n");	return;	}
		if(key<root->info)
			root=root->left;
		else
			root=root->right;
	}
	printf("Unsuccessful search\n");
}
void recursearch(nd *root,int key)
{
	if(!root)
	{	printf("Unsuccessful search\n");	return;	}
	if(key == root->info)
	{	printf("Successful search\n");	return;	}
	if(key < root->info)
		return recursearch(root->left,key);
	return recursearch(root->right,key);
}
nd * deletenode(nd *root,int key)
{
	nd *c,*p,*q,*s;
	if(!root)
	{	printf("Binary search tree is empty\n");	return root;	}
	p=0;	c=root;
	while(c)
	{
		if(key == c->info)
		{	printf("Successful search and delete\n");	break;	}
			p=c;
		if(key<c->info)
			c=c->left;
		else
			c=c->right;
	}
	if(!c)
	{	printf("Key not found\n");	return root;	}
	if(!c->left)
		c=c->left;
	if(!c->right)
		c=c->right;
	else
	{
		s=c->right;
		while(s->left)
			s=s->left;
		s->left=c->left;
		q=c->right;
	}
	if(!p)	return q;
	if(c == p->left)
		p->left=q;
	else
		p->right=q;
	free(c);	return root;
}
int main()
{
	nd *root=0;
	int ch,i,key;
	FILE *fp;
	fp=fopen("bst2.txt","r");
	for(;;)
	{
		printf("\n1.Insert\t2.Iterative Search\t3.Recursive Search\n4.Inorder\t5.Delete a node\t6.Exit\n");
		printf("Enter choice:");	scanf("%d",&ch);
		switch(ch)
		{
			case 1: fscanf(fp,"%d",&ch);
					for(i=0;i<ch;i++)
					{
						fscanf(fp,"%d",&key);
						root=insert(root,key);
					}	break;
			case 2: printf("Enter info to be searched:");
					scanf("%d",&key);	itersearch(root,key);	break;
			case 3: printf("Enter info to be searched:");
					scanf("%d",&key);	recursearch(root,key);	break;
			case 4: inorder(root);	break;
			case 5:	printf("Enter info to be deleted:");
					scanf("%d",&ch);	root=deletenode(root,ch);
					break;
			case 6: free(root);	return 0;
		}
	}
}
