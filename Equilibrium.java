/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class Equilibrium {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		int t=sc.nextInt();
		for(int m=0;m<t;m++) {
			int n=sc.nextInt();
			
			int arr[]=new int[n];
			for(int i=0;i<n;i++)
				arr[i]=sc.nextInt();
			int eqlib=0,lftcnt=0,rgtcnt=0;
			for(int i=0;i<n;i++) {
				eqlib=i;
				for(int j=0;j<eqlib;i++)
					lftcnt+=arr[j];
				for(int j=eqlib+1;j<n;i++)
					rgtcnt+=arr[j];
				if(lftcnt==rgtcnt) {
					System.out.println(eqlib); return;
				}
				
			}
			System.out.println(-1);
			
		}

	}

}
