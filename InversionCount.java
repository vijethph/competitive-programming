/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class InversionCount {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		int t=sc.nextInt();
		for(int m=0;m<t;m++) {
			int bcount=0;
			int n=sc.nextInt();
			int arr[]=new int[n];
			for(int i=0;i<n;i++)
				arr[i]=sc.nextInt();
			for(int i=0;i<n;i++)
				for(int j=0;j<n-1;j++)
					if(arr[j]>arr[j+1]) {
						bcount++;
						int tmp=arr[j];
						arr[j]=arr[j+1];
						arr[j+1]=tmp;
					}
				
			System.out.println(bcount);
		}

	}

}
