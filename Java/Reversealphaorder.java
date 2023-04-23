/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class Reversealphaorder {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String str= sc.nextLine();
		char[] astr=str.toCharArray();
		for(int i=0;i<astr.length;i++) {
			for(int j=0;j<astr.length-1;j++) {
				if(astr[j+1]>astr[j]) {
					char tmp=astr[j];
					astr[j]=astr[j+1];
					astr[j+1]=tmp;
				}
			}
		}
		for(int i=astr.length-1;i>=0;i--)
			System.out.print(astr[i]);

	}

}
