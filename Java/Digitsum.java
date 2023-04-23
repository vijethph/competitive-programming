package workout;
import java.util.Scanner;
public class Digitsum {

	
	static long fact(long n) {
		if(n==0)
			return 1;
		return n*fact(n-1);
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter number");
		long n=sc.nextInt();	long sum=0;
		long res=fact(n);
		while(res!=0) {
			sum=sum+res%10;
			res=res/10;
		}
		System.out.println("sum of digits:" +sum);
	}

}
