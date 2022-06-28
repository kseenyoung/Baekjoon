
import java.util.Scanner;

public class E1065 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int count=0;
		
		for(int i=1; i <= num; i++) {
			if(isH(i)) count++;
		}
		
		System.out.println(count);
		
	}
	
	public static boolean isH(int n) {
		if(n < 100)
			return true;
		else {
			int hun = n/100;
			int ten = (n - (hun*100 +n%10))/10;
			int one = n%10;
			if(hun - ten == ten - one)
				return true;
		}
		return false;
	}
}
