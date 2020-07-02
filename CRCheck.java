/*Done By SilentKiller*/
package labPrograms;

import java.util.Scanner;

/**
 * @author Vijeth PH
 *
 */
public class CRCheck {
	static String xor(String a, String b) {
		StringBuilder sb=new StringBuilder();
		int len=Math.min(a.length(), b.length());
		for(int i=0;i<len;i++) {
			if(a.charAt(i)==b.charAt(i))
				sb.append('0');
			else
				sb.append('1');
		}
		return sb.toString();
	}
	
	static String divide(String divend,String divsor) {
		int dsl=divsor.length();
		int dvl=divend.length();
		while(dvl>=dsl) {
			String temp;
			if(divend.charAt(0)=='1')
				temp=xor(divsor,divend.substring(0,dsl));
			else
				temp=divend.substring(0, dsl);
			divend=temp.substring(1)+divend.substring(dsl);
			dvl-=1;
		}
		return divend;
	}
	
	static String genCW(String msg,String gen) {
		int msgl=msg.length();
		int genl=gen.length();
		String divend=String.format("%-"+(msgl+genl-1)+"s",msg).replace(' ', '0');
		String rem=divide(divend,gen);
		return msg+rem;
	}
	static boolean checkCW(String cw,String gen) {
		String temp=divide(cw,gen);
		int len=temp.length();
		for(int i=0;i<len;i++)
			if(temp.charAt(i)=='1')
				return false;
		return true;
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("enter generator string");
		String gen=sc.next();
		while(true) {
			System.out.println("\nMenu\n1.generate code word\n2.check code word\n3.exit");
			int ch=sc.nextInt();
			switch(ch) {
			case 1:System.out.println("enter message");
					String msg=sc.next();
					String res=genCW(msg,gen);
					System.out.println("codeword: "+res); 	break;
			case 2:System.out.println("enter codeword");
					String cw=sc.next();
					if(checkCW(cw,gen))
						System.out.println("code word is valid");
					else
						System.out.println("code word is invalid");	break;
			case 3:System.exit(0);
			}
		}
	}

}
