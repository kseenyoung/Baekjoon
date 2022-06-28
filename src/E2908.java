
import java.util.Scanner;

public class E2908 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String input = sc.nextLine();
		String[] number = input.split(" "); //숫자 분리

		
		for(int i=2; i >= 0; i--) {
			if(number[1].charAt(i) > number[0].charAt(i)) {
				for(int j=2; j >= 0 ; j--) //j >= 0 유의
					System.out.print(number[1].charAt(j));
				break;
			}
			else if(number[1].charAt(i) < number[0].charAt(i)) {
				for(int j=2; j >= 0 ; j--)
					System.out.print(number[0].charAt(j));
				break;
			}
		}

	}

}
