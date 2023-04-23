/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class Primenumset {

	/**
	 * @param args
	 */
	
	static boolean isprime(int n) {
		for(int i=2;i<n;i++) {
			if(n%i==0) {
				return false;
			}
		}
		return true;
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		for(int m=0;m<t;m++) {
		int n=sc.nextInt();
		int prime[]=new int[n];
		int j=0;
		for(int i=2;i<n;i++) {
			if(isprime(i))
				prime[j++]=i;
		}
		for(int i=0;i<n;i++) {
			for(int k=0;k<n;k++) {
				if(prime[i]*prime[k]<=n) {
					if((prime[i]==0)||(prime[k]==0))
							continue;
					System.out.println("("+prime[i]+","+prime[k]+")");
				}
			}
		}

		}
	}

}
