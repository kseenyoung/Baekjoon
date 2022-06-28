
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class E2869 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer numbers = new StringTokenizer(br.readLine());
		int a = Integer.parseInt(numbers.nextToken());
		int b = Integer.parseInt(numbers.nextToken());
		int v = Integer.parseInt(numbers.nextToken());
		
		int move = a - b; //실질적으로 하루동안 이동한 거리
		int safe_m = v - a; //무조건 발생하게 되는 이동거리의 합(a보다 작은 어떤 값)
		if(safe_m <= 0) {
			System.out.println(1);
			return;
		}
		
		int day = safe_m/move;
		if(day*move + a >= v)
			System.out.println(day+1);
		else 
			System.out.println(day+2);
		
		System.out.println();
	}

}
