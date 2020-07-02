/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class Numvowel {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String str=sc.next();
		char[] astr=str.toCharArray();
		char[] vstr= {'a','e','i','o','u'};
		int vowcount[]=new int[5];
		for(int i=0;i<astr.length;i++) {
			switch(astr[i]) {
			case 'a':vowcount[0]=vowcount[0]+1; break;
			case 'e':vowcount[1]=vowcount[1]+1; break;
			case 'i':vowcount[2]=vowcount[2]+1; break;
			case 'o':vowcount[3]=vowcount[3]+1; break;
			case 'u':vowcount[4]=vowcount[4]+1; break;
			
			default:break;
			
			}
		}
		int lar=vowcount[0];
		for(int i=0;i<5;i++) {
			if(lar<vowcount[i])
				lar=vowcount[i];
		}
		System.out.println("letters to be added:");
		for(int i=0;i<5;i++) {
			vowcount[i]=lar-vowcount[i];
			while(vowcount[i]!=0) {
				System.out.print(vstr[i]+" ");
				vowcount[i]=vowcount[i]-1;
			}
		}
		

	}

}
