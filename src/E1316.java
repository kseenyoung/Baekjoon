

import java.util.Scanner;

public class E1316 {

	static Scanner sc = new Scanner(System.in);	//(수정)main밖으로 빼며 Static
	public static void main(String[] args) {
		int n = sc.nextInt(), count = n;
			
		for(int i=0; i < n; i++) { //n개의 word
			if(!check()) count -= 1;
		}	
			System.out.println(count);
	}

	public static boolean check() { //(수정)
		boolean[] alph = new boolean[26]; //(수정) '>1' 체크보다 true/false, 효율 증가
		String word = sc.next();
		int prev = 0, now; //(revice)문자 
		int ln = word.length();
		
		for	(int i=0; i < ln; i++) { //word의 문자
			now = word.charAt(i);
			
			if(prev != now) { //이미 실행됐던 문자
				if(alph[now - 'a'] == false) { //**굳이 숫자 69빼는 것보다 'a'사용하자
					alph[now - 'a'] = true;
					prev = now;
				}
				else // now가 나온적 있는 경우
					return false;
			}

			continue;
		}
		
		return true;
	}
}
