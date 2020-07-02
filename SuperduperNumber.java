/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class SuperduperNumber {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int arr[]=new int[n+1];
		for(int i=1;i<=n;i++)
			arr[i]=sc.nextInt();
		int oddsum=0,evnsum=0;
		for(int i=1;i<=n;i++) {
			if(i%2==0)
				evnsum+=arr[i];
			else
				oddsum+=arr[i];
		}
		int sum=oddsum-evnsum;
		if(sum==0)
			System.out.println("SUPER DUPER NUMBER");
		else
			System.out.println(sum);

	}

}
