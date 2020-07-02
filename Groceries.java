/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class Groceries {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		for(int m=0;m<t;m++) {
			int n=sc.nextInt();
			int weigh[]=new int[n];
			int num=sc.nextInt();
			for(int i=0;i<n;i++)
				weigh[i]=sc.nextInt();
			for(int i=0;i<n;i++)
				for(int j=0;j<n-1;j++)
					if(weigh[j]>weigh[j+1]) {
						int tmp=weigh[j];
						weigh[j]=weigh[j+1];
						weigh[j+1]=tmp;
					}
			int sonsum=0,dadsum=0;
			for(int i=0;i<n;i++) {
				if(i<num) {
					sonsum+=weigh[i];
				}
				else
					dadsum+=weigh[i];
			}
			System.out.println(dadsum-sonsum);
		}

	}

}
