/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class ContiguousSubarray {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		int t=sc.nextInt();
		for(int m=0;m<t;m++) {
			int n=sc.nextInt();
			int s=sc.nextInt();
			int arr[]=new int[n+1];
			for(int i=1;i<=n;i++)
				arr[i]=sc.nextInt();
			int sum=0,a=1,b=1,j=1;
			for(int i=1;i<=n;i++) {
				sum+=arr[i];
				if(sum<=s) {
					if(sum==s) {
						b=i;	System.out.println(a+" "+b ); return;
					}
				}
				else {
					
					j++; i=j;	a=j;	sum=arr[i];	 continue;
				}
			}
			System.out.println(-1);
			
		}

	}

}
