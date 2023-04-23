/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class ChangeAlphabet {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String str= sc.nextLine();
		String lstr=str.toLowerCase();
		char[] astr=lstr.toCharArray();
		for(int i=0;i<astr.length;i++) {
			if(astr[i]==' ')
				continue;
			if((astr[i]=='a')||(astr[i]=='e')||(astr[i]=='i')||(astr[i]=='o')||(astr[i]=='u'))
				astr[i]++;
			else
				astr[i]--;
		}
		System.out.println(astr);

	}

}
