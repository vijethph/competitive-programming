/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class NumvowelPrime {

	/**
	 * @param args
	 */
	static int factsum=0;
	static void factors(int n) {
		int j=0;
		for(int i=1;i<n;i++)
			if(n%i==0)
				factsum=factsum+i;
	}
	static boolean isprime(int n) {
		for(int i=2;i<n;i++) {
			if(n%i==0) {
				return false;
			}
		}
		return true;
	}
	static int fact(int n) {
		if(n==0)
			return 1;
		return n*fact(n-1);
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String str= sc.nextLine();
		char[] astr=str.toCharArray();
		int count=0;
		for(int i=0;i<astr.length;i++) {
			switch(astr[i]) {
			case 'a': case 'e': case 'i': case 'o': case 'u': count++; break;  
			default: break;
			}
		}
		if(isprime(count)) {
			System.out.println(fact(count));
		}
		else {
			factors(count);
			System.out.println(factsum);
		}
			
	}

}
