/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class Freqofdigits {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String str= sc.nextLine();
		char[] astr=str.toCharArray();
		int count[]=new int[10];
		for(int i=0;i<astr.length;i++) {
			int a=astr[i];
			
			if((a>=48)&&(a<=57)) {
				
				
				switch(a) {
				case 48: count[0]++; break;
				case 49: count[1]++; break;
				case 50: count[2]++; break;
				case 51: count[3]++; break;
				case 52: count[4]++; break;
				case 53: count[5]++; break;
				case 54: count[6]++; break;
				case 55: count[7]++; break;
				case 56: count[8]++; break;
				case 57: count[9]++; break;
				}
			}
		}
		for(int i=0;i<count.length;i++)
			System.out.print(count[i]+" ");

	}

}
