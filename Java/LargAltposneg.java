/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class LargAltposneg {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int count[]=new int[n];
		int j=0;
		int arr[]=new int[n+1];
		for(int i=1;i<=n;i++)
			arr[i]=sc.nextInt();
		for(int i=1;i<=n;i++) {
			if(((i%2==0)&&(arr[i]<0))||((i%2!=0)&&(arr[i]>0)))
				count[j]++;
			else {
				j++; count[j]++;
			}
		}
		int lar=count[0];
		for(int i=0;i<count.length;i++)
			if(lar<count[i])
				lar=count[i];
		System.out.println(lar);

	}

}
