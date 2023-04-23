package workout;

import java.util.Scanner;

public class Asciivalue {

	public static void main(String[] args) {
		
		
		Scanner sc=new Scanner(System.in);
		System.out.println("enter number of strings: ");
		int m=sc.nextInt();
		System.out.println("enter array of string");
		String[] str=new String[m];
		for(int i=0;i<m;i++)
			str[i]=sc.next();
		for(int i=0;i<m;i++) {
			
				char[] astr=str[i].toCharArray();
				System.out.println("word "+ (i+1));
				for(int j=0;j<astr.length;j++) {
					int n=astr[j];
					System.out.println("ascii value: "+ n);
				}
		}

	}

}
