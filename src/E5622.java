
import java.util.Scanner;

public class E5622 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String word = sc.nextLine();
		int sum=0;
		
//		for(int i=0; i < word.length(); i++) {
//			if(word.charAt(i) < 'D')
//				sum += 3;
//			else if(word.charAt(i) > 'C' && word.charAt(i) < 'G')
//				sum += 4;
//			else if(word.charAt(i) > 'F' && word.charAt(i) < 'J')
//				sum += 5;
//			else if(word.charAt(i) > 'I' && word.charAt(i) < 'M')
//				sum += 6;
//			else if(word.charAt(i) > 'L' && word.charAt(i) < 'P')
//				sum += 7;
//			else if(word.charAt(i) > 'O' && word.charAt(i) < 'T')
//				sum += 8;
//			else if(word.charAt(i) > 'S' && word.charAt(i) < 'W')
//				sum += 9;
//			else
//				sum += 10;
//		}
		
		System.out.println(sum);
	}

}
