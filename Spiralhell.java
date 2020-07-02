package workout;

import java.util.Scanner;

public class Spiralhell {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		
		System.out.print("enter number: ");
		int n=sc.nextInt();
		int len=n*2-1;
		for(int i=0;i<len;i++) {
			for(int j=0;j<len;j++) {
				int min=i<j?i:j;
				min=min<len-i?min:len-i-1;
				min=min<len-j-1?min:len-j-1;
				System.out.print(n-min+ " ");
				
			}
			System.out.println();
		}
		
		
	}

}
