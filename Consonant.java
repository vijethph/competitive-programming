package workout;

import java.util.Scanner;

public class Consonant {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("enter string");
		String str=sc.next();
		char[] astr=str.toCharArray();
		int count=0;
		for(int i=0;i<astr.length;i++) {
			switch(astr[i]) {
			case 'a': case 'e': case 'i': case 'o': case 'u': case 'A': case 'E': case 'I': case 'O': case 'U': System.out.println("Vowel: "+ astr[i]); count++; break;
			default: System.out.println("Consonant: "+ astr[i]); break;
			}
		}
		System.out.println("Vowels: "+ count  + " Consonants: "+ (astr.length-count));

	}

}
