import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class E11653 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());
		
		if(num != 1) {
			for(int i=2; i <= num; i++) {
				if(num%i == 0) {
					num /= i;
					System.out.println(i);
					i=1;
				}
			}
			
		}

	}

}
