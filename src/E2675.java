
import java.util.Scanner;

public class E2675 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int R = sc.nextInt(); 
		int r = 0;
		String S;
		
		
		for(int i=0; i < R; i++) {
			r = sc.nextInt();
			S = sc.next();
			
			for(int k = 0; k < S.length(); k++) {
				for(int j = 0; j < r; j++){
					System.out.print(S.charAt(k));
				}
			}
			System.out.println();
		}
		

	}

}
