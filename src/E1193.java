
//import java.util.Scanner;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class E1193 {

	public static void main(String[] args) throws IOException {
		//Scanner sc = new Scanner(System.in);
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int crose_count = 1, crose_count_sum = 0;
		//sc.close();
		
		while(true) {
			
			if(crose_count_sum + crose_count >= n) {
				if( crose_count % 2 == 0) { //짝수번째 대각선 분모가 먼저 큰 값을 가짐
					System.out.println((n - crose_count_sum) + "/" + (crose_count - (n - crose_count_sum -1)));
					break;
			}
				else { //홀수번째 대각선
					System.out.println((crose_count - (n - crose_count_sum -1)) + "/" + (n - crose_count_sum));
					break;
				}
			}
			else {
				crose_count_sum += crose_count;
				crose_count++;
					
			}
			
			}
		}

	}
