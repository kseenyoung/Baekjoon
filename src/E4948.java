import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class E4948 {

	static boolean[] prime = new boolean[246913];
	static int[] count_prime = new int[246913];
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		while(true) {
			int num = Integer.parseInt(br.readLine());
			if(num == 0) break;
			
			get_prime();
			count_prime();

			sb.append(count_prime[2*num] - count_prime[num]).append('\n');
		}
		
		System.out.println(sb);
	}

	public static void get_prime() {
		prime[0] = prime[1] = true;
		for(int i = 2; i <= Math.sqrt(prime.length); i++) {
			if(prime[i] == true) continue;
			
			for(int j=i*i; j < prime.length; j = i+j) {
				prime[j] = true;
			}
		}
	}
	
	public static void count_prime() {
		int count = 0;
		for(int i=2; i < prime.length; i++) {
			if(!prime[i]) count++; //false가 소수
			count_prime[i] = count;
		}
	}
}
