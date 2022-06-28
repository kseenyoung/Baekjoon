
import java.util.Scanner;

public class E2292 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.close();
		int range=2, count=1;
		
		if(n == 1)
			System.out.println(1);
		else {
			while(range <= n) {
				range += 6*(count);
				count++;
			}
			System.out.println(count);
		}
		

	}

}
