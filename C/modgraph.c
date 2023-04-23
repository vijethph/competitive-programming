/*modified graph using adjacency matrix*/
/*Done By: SilentKiller*/
#include<stdio.h>
#include<stdlib.h>
#define MAX_VERTICES 40
#define TRUE 1
#define FALSE 0
int a[10][10]={{0,1,1},{0,0,0,1,1},{0,0,0,0,0,1,1}};
short int visited[MAX_VERTICES]={FALSE};
void BFS(int source,int n)
{
	int u,v,f=0,r=-1,q[MAX_VERTICES];
	visited[source]=TRUE;
	q[++r]=source;
	while(r>=f)
	{
		u=q[f++];
		for(v=0;v<n;v++)
			if((a[u][v]==1)&&(visited[v]==0))
			{
				q[++r]=v;
				visited[v]=TRUE;
			}
	}
	for(u=0;u<n;u++)
	{
		if(visited[u]==0)
			printf("%d is not reachable\n",u);
		else
			printf("%d is reachable\n",u);
	}
}
void DFS(int source,int n)
{
	int col;
	visited[source]=TRUE;
	printf("%d is reachable\n",source);
	for(col=0;col<n;col++)
		if((a[source][col]==1)&&(visited[col]==0))
			DFS(col,n);
}
int main()
{
	int i,ch,source,n;
	printf("Enter the number of vertices:");	scanf("%d",&n);
	printf("Enter the source vertex:");	scanf("%d",&source);
	for(;;)
	{
		printf("1.BFS\t2.DFS\t3.Exit\n");	printf("Enter choice:");
		scanf("%d",&ch);
		for(i=0;i<n;i++)
			visited[i]=FALSE;
		switch(ch)
		{
			case 1:BFS(source,n);	break;
			case 2:DFS(source,n);	break;
			case 3:return 0;
			default:printf("Invalid option\n");	break;
		}
	}
}
