/*Done By SilentKiller*/
package workout;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class LarNumString {

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
			char[] astr=new char[20*n];
			int j=0;
			for(int i=0;i<n;i++) {
				while(arr[i]!=0) {
					int k=arr[i]%10;
					astr[j++]=(char)(k+'0');
					arr[i]=arr[i]/10;
				}
			}
			for(int i=0;i<astr.length;i++) {
				for(j=0;j<astr.length-1;j++) {
					if(astr[j]<astr[j+1]) {
						char tmp=astr[j];
						astr[j]=astr[j+1];
						astr[j+1]=tmp;
					}
				}
			}
			for(int i=0;i<astr.length;i++)
				System.out.print(astr[i]);
		}

	}

}
