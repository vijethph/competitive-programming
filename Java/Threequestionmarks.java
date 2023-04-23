/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class Threequestionmarks {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String str= sc.nextLine();
		char[] astr=str.toCharArray();
		boolean state=false;
		int count=0,b,c;
		for(int i=0;i<astr.length;i++) {
			int a=astr[i];
			
			if((a>=48)&&(a<=57)) {
				state=true; b=a;
			}
			if(state==true)
				if(astr[i]=='?')
					count++;
			
			if(count==3) {
				System.out.println("true");
				break;
			}
			if(state==true) {
				state=false; count=0; continue;
			}
		}
		System.out.println("false");

	}

}
