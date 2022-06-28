
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class E1978 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer sb = new StringTokenizer(br.readLine());
		int num, count=0;
		
		for(int i=0; i < N; i++) { //주어진 숫자 개수
			num = Integer.parseInt(sb.nextToken());
			if(num == 1) count++;
			for(int j=2; j < num; j++)
				if( num!=1 && num%j == 0) {
					count++;
					break;
				}
		}
		
		System.out.println(N-count);
		

	}

}
