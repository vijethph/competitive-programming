/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class Armstrongnum {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		for(int m=0;m<t;m++) {
		int n=sc.nextInt();
		int num=n;
		int digits[]=new int[3];
		for(int i=0;n!=0;i++) {
			digits[i]=n%10;
			n=n/10;
		}
		int a=digits[0]*digits[0]*digits[0];	
		int b=digits[1]*digits[1]*digits[1];
		int c=digits[2]*digits[2]*digits[2];
		if(a+b+c==num)
			System.out.println("Yes");
		else
			System.out.println("No");

		}
	}

}
