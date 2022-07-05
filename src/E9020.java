import java.io.*;

public class E9020 {

	static boolean[] prime = new boolean[10001];
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		int n, num1, num2;
		
		get_prime();
		
		for(int i=0; i < T; i++) {
			n = Integer.parseInt(br.readLine());
			num1 = num2 = n/2;
			
			while(prime[num1] != false || prime[num2] != false) {
				num1--; num2++;
			}
			sb.append(num1 + " " + num2 + "\n");
		}
		System.out.println(sb);
	}

	public static void get_prime() {
		prime[0] = prime[1] = true;
		for(int i=2; i <= Math.sqrt(prime.length); i++) {
			if(prime[i]) continue;
			
			for(int j=i*i; j < prime.length; j += i) {
				prime[j] = true;
			}
		}
	}
}
