import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class E2581 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int M = Integer.parseInt(br.readLine());
		int N = Integer.parseInt(br.readLine());
		int min = -1;
		int sum = 0;
		boolean temp;

		for(int i=M; i <= N; i++) {
			temp = true;
			if(i == 1) temp=false; //반복문이 2부터 시작이므로 1에 대한 예외처리 해야 함!!
			for(int j=2; j < i; j++) 
				if(i%j == 0) {
					temp = false;
					break; //소수가 아님이 판별 됐으므로 진행종료
				}
			
			if(temp == true) {
				if(min==-1) min = i;
				sum += i;
			}
		}
		
		//출력
		if(min == -1)
			System.out.println(min);
		else
			System.out.println(sum + "\n" + min);
	}
}
