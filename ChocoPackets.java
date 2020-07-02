/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class ChocoPackets {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		int t=sc.nextInt();
		for(int m=0;m<t;m++) {
			int n=sc.nextInt();
			int arr[]=new int[n];
			for(int i=0;i<n;i++)
				arr[i]=sc.nextInt();
			int k=sc.nextInt();
			for(int i=0;i<n;i++)
				for(int j=0;j<n-1;j++)
					if(arr[j]>arr[j+1]) {
						int tmp=arr[j];
						arr[j]=arr[j+1];
						arr[j+1]=tmp;
					}
			int count[]=new int[n];
			int u=0;
			for(int i=0;i<n;i++) {
				if(i+k<n) {
					count[u++]=arr[i+k-1]-arr[i];
				}
			}
			int min=count[0];
			for(int i=1;i<count.length;i++)
				if((min>count[i])&&(count[i]!=0))
					min=count[i];
			System.out.println(min);

		}
	}

}
