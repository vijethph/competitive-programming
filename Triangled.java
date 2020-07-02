package workout;

import java.util.Scanner;

public class Triangled {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		float a=sc.nextFloat();
		float b=sc.nextFloat();
		float c=sc.nextFloat();
		if((a+b)>c) {
			if((c+a)>b) {
				if((b+c)>a) {
					System.out.println("YES");
				}
				else
					System.out.println("NO");
			}
		}
		else
			System.out.println("NO");

	}

}
