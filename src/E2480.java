
import java.util.Scanner;

public class E2480 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int d1 = sc.nextInt();
		int d2 = sc.nextInt();
		int d3 = sc.nextInt();
		int money;

		if( d1 != d2 && d1 != d3 && d2 != d3 ) {
			int max = d1;
			if(d2 > d1) max = d2;
			if(d3 > max) max = d3;
			money = max*100;
		}
		else if ( d1 == d2 && d2 != d3) {
			money = 1000 + d1*100;
		}
		else if ( d1 == d3 && d2 != d3) {
			money = 1000 + d1*100;
		}
		else if ( d2 == d3 && d2 != d1) {
			money = 1000 + d2*100;
		}
		else {
			money = 10000+d1*1000;
		}
		
		System.out.println(money);
	}

}
