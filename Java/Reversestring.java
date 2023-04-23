/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class Reversestring {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String str= sc.nextLine();
		char[] astr=str.toCharArray();
		int i;
		for(i=0;i<astr.length;i++) {
			if(astr[i]==' ') {
				for(int j=i-1;(j>=0);j--) {
					if(astr[j]==' ')
						break;
					System.out.print(astr[j]);
					
				}
				System.out.print(" ");
			}
		}
		for(int j=i-1;(j>=0);j--) {
			if(astr[j]==' ')
				break;
			System.out.print(astr[j]);
		}

	}

}
