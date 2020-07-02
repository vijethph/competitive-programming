/*Done By SilentKiller*/
package labPrograms;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class BellmanFord {

	static int n,dest;
	static int[] dv,inter;
	static int[][] adj;
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.print("enter number of nodes: ");
		n=sc.nextInt();
		adj=new int[n][n];
		inter=new int[n+1];
		System.out.println("enter adjacency matrix");
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				adj[i][j]=sc.nextInt();
		System.out.print("enter destination vertex: ");
		dest=sc.nextInt();
		dv=new int[n];
		for(int i=0;i<n;i++)
			dv[i]=9999;
		dv[dest-1]=0;
		compute();
		System.out.println("distance vector: ");
		for(int i=0;i<n;i++) {
			if(i==dest-1)
				continue;
			System.out.println("distance from "+(i+1)+ " through "+(inter[i]+1)+  " is "+dv[i]);
			int k=inter[i];
			System.out.print("path: "+(k+1));
			while(true) {
				k=inter[k];
				if(k==0)
					break;
				System.out.print("-->"+(k+1));
			}
			System.out.println();
		}
		System.out.println();
		
		
	}
	static void compute() {
		for(int i=0;i<n;i++) 
			for(int j=0;j<n;j++) 
				for(int k=0;k<n;k++) 
					if(adj[j][k]!=9999) 
						if(dv[k]>adj[j][k]+dv[j]) {
							dv[k]=adj[j][k]+dv[j];
							inter[k]=j;
						}
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				if(adj[i][j]!=9999)
					if(dv[j]>dv[i]+adj[i][j]) {
						System.out.println("the graph contains negative edge cycle");
						return;
					}
				
			
		
	}

}
