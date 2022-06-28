

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class E2941 {

	public static void main(String[] args) throws IOException { 
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String word = br.readLine();
		int count=0;
		
		int ln = word.length();
		char ch;
		for(int i=0; i < ln; i++) {
			ch = word.charAt(i);
			
			if(ch == 'c' && (i + 1 < ln)) {
				if(word.charAt(i+1) == '=')
					i++;
				else if(word.charAt(i+1) == '-') 
					i++;
			}
			
			if(ch == 'd' && (i+1 < ln)) {
				if(word.charAt(i+1) == 'z' && (i+2 < ln)) {
					if(word.charAt(i+2) == '=')
						i += 2;
				}
				else if(word.charAt(i+1) == '-')
					i++;
			}
			
			if(ch == 'l' && (i+1 < ln)){
				if(word.charAt(i+1) == 'j')
					i++;
			}
			
			if(ch == 'n' && (i+1 < ln)) {
				if(word.charAt(i+1) == 'j')
					i++;
			}
			
			if(ch == 's' && (i+1 < ln)) {
				if(word.charAt(i+1) == '=')
					i++;
			}
			
			if(ch == 'z' && (i+1 < ln)) {
				if(word.charAt(i+1) == '=')
					i++;
			}
			
			count++;
		} //for문 종료(문자개수 파악 완료)
		
		System.out.println(count);
	}

}
