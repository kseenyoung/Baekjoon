
import java.util.Scanner;

public class E11720 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int result=0;
		int count = sc.nextInt();
		String values = sc.next();
		
		for(int i=0; i < count; i++) {
			result += values.charAt(i) - 48;
		}
		
		System.out.println(result);
	}
}
