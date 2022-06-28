
import java.util.Scanner;

public class E1157 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] word = new int[26];
		String S = sc.nextLine();
		int s, max=0, count=0;
		
		for(int i=0; i < S.length(); i++) { //알파벳 발생 횟수
			s = S.charAt(i);
			if(s > 96)  //소문자
				word[s-97]++;
			else  //대문자
				word[s-65]++;
		}
		
		for(int i=0; i < 26; i++) { //최대 발생 찾기
			if(word[i] > max) { 
				max = word[i];
				count = i;
			}
			else if(word[i] == max && max != 0) 
				count = -1;
		}
		
		System.out.println(count < 0 ? "?" : (char)(count+65));
		
	}

}
