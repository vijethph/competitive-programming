package workout;

import java.util.Scanner;

public class Triplett {

	static boolean triplet(int a,int b,int c) {
		int x=a*a;
		int y=b*b;
		int z=c*c;
		if((x+y==z)||(x+z==y)||(y+z==x))
			return true;
		else
			return false;
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		for(int m=0;m<t;m++) {
		int n=sc.nextInt();
		int arr[]=new int[n];
		for(int i:arr)
			arr[i]=sc.nextInt();
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				for(int k=0;k<n;k++) {
					if(triplet(arr[i],arr[j],arr[k])) {
						System.out.println("Yes");
						return;
					}
				}
			}
		}
		System.out.println("No");
		}
		
		

	}

}
