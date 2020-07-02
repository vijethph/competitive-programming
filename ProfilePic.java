package workout;

import java.util.Scanner;

public class ProfilePic {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int l=sc.nextInt();
		int n=sc.nextInt();
		int w[]=new int[n];
		int h[]=new int[n];
		for(int i=0;i<n;i++) {
			w[i]=sc.nextInt();
			h[i]=sc.nextInt();
		}
		for(int i=0;i<n;i++) {
			if((w[i]<l)||(h[i]<l)) {
				System.out.println("UPLOAD ANOTHER");
			}
			else {
				if(w[i]==h[i]) {
					System.out.println("ACCEPTED");
				}
				else
					System.out.println("CROP IT");
			}
		}

	}

}
