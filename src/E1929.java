import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.math.*;

public class E1929 {

	public static void main(String[] args) throws IOException {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			StringTokenizer st = new StringTokenizer(br.readLine());
			int M = Integer.parseInt(st.nextToken());
			int N = Integer.parseInt(st.nextToken());
			
			boolean[] prime = new boolean[N+1];
			prime[0] = prime[1] = true;
			
			for(int i=2; i <= Math.sqrt(N); i++) {
				if(prime[i] == true) continue;
				
				for(int j=i*i; j <= N; j = i+j) {
					prime[j] = true;
				}
			}
			
			for(int i=M; i <= N; i++) {
				if(prime[i] == false)
					System.out.println(i);
			}
	}
	
}
