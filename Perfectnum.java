/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */

public class Perfectnum {

	/**
	 * @param args
	 */
	static int sum;
	static void factors(int n) {
		int j=0;
		for(int i=1;i<n;i++)
			if(n%i==0)
				sum=sum+i;
	}
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		for(int m=0;m<t;m++) {
			int n=sc.nextInt();
			sum=0; factors(n);
			if(sum==n)
				System.out.println(1);
			else
				System.out.println(0);
			
		

		}
	}

}
