
import java.util.Scanner;

public class E1712 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
		int x=-1;
		
		while(c != b && x <= a/(c-b)) 
			x++;
		
		System.out.println(x);
	}

}
