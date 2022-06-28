
import java.util.Scanner;

public class E10809 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String S = sc.nextLine();
		int[] result = new int[26];
		
		for(int i=0; i < 26; i++) //초기화
			result[i] = -1;
		
		for(int i=0; i < S.length(); i++) { //입력
			int alpa = S.charAt(i)-97;
			if(result[alpa] == -1)
				result[alpa] = i;
		}
		
		for(int i=0; i < 26 ;i++) { //출력
			System.out.print(result[i] + " ");
		}
	}

}
