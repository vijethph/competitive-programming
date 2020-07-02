/*Done By SilentKiller*/
package workout;
import java.util.Scanner;
/**
 * @author Vijeth PH
 *
 */
public class Thirdlargest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter number of elements: ");
		int n=sc.nextInt();
		System.out.println("Enter the elements");
		int arr[]=new int[n];
		for(int i=0;i<arr.length;i++)
			arr[i]=sc.nextInt();
		int l=arr[0];	int sl=arr[0];	int tl=arr[0];
		for(int i=0;i<n;i++) {
			if(arr[i]>l)
				l=arr[i];
		}
		for(int i=0;i<n;i++) {
			if((arr[i]<l)&&(arr[i]>sl)) {
				sl=arr[i];
			}
		}
		for(int i=0;i<n;i++) {
			if((arr[i]<l)&&(arr[i]<sl)&&(arr[i]>tl)) {
				tl=arr[i];
			}
		}
			System.out.println("Third largest: " + tl);

	}

}
