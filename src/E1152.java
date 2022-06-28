
import java.util.Scanner;

public class E1152 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine(); //공백문자 포함 입력
		sc.close();
		
		s = s.trim(); //**String의 전후방 공백 제거
		String word[] = s.split(" ");
		
		if(s.isEmpty())
			System.out.println(0);
		else
			System.out.println(word.length);

	}

}
