/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */

public class Romanumeral {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		for(int m=0;m<t;m++) {
			String str= sc.nextLine();
			char[] astr=str.toCharArray();
			int sum=0;
			for(int i=0;i<astr.length;i++) {
				switch(astr[i]) {
				case 'I': if((astr[i-1]=='V')||(astr[i-1]=='X')||(astr[i-1]=='L')||(astr[i-1]=='C')) {
							sum++; }
							if((astr[i+1]=='V'))
								sum=5-sum;
							else if((astr[i+1]=='X'))
								sum=10-sum;
							else if((astr[i+1]=='L'))
								sum=50-sum;
							else if((astr[i+1]=='C'))
								sum=100-sum;
							else {}
							break;
				case 'V':sum=sum+5; break;
				case 'X':sum=sum+10;break;
				case 'L':sum=sum+50;break;
				case 'C':sum=sum+100; break;
				
				}
			}
			System.out.println(sum);
				
		}
	}

}
