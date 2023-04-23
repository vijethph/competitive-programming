/*Done By SilentKiller
 dynamic programming Java implementation of coin change problem*/
package dynamicProgramming;
import java.util.Arrays;
import java.util.Scanner;
/**
 * @author Vijeth PH
 *	time complexity: O(mn)
 *	space complexity: O(n)
 */
public class CoinChange {

	static long countways(int s[],int m,int n) {
		long[] table=new long[n+1];
		Arrays.fill(table, 0);
		table[0]=1;
		for(int i=0;i<m;i++)
			for(int j=s[i];j<=n;j++)
				table[j]+=table[j-s[i]];
		return table[n];
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter the value to make change: ");
		int n=sc.nextInt();
		int arr[]=new int [n];
		System.out.print("Enter the number of different coins that you have: ");
		int m=sc.nextInt();
		System.out.print("Enter the supply of coins: ");
		for(int i=0;i<m;i++)
			arr[i]=sc.nextInt();
		System.out.println("Number of ways the change can be made: "+countways(arr,m,n));
		sc.close();
	}

}
