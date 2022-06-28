
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class E10250 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		StringTokenizer inform;
		int W, H, N, x, y;
		for(int i=0; i < n; i++) {
			inform = new StringTokenizer(br.readLine());
			H = Integer.parseInt(inform.nextToken());
			W = Integer.parseInt(inform.nextToken());
			N = Integer.parseInt(inform.nextToken());
			x = N/H + 1;
			y = N%H;
			if(y == 0) { //꼭대기 층
				x = N/H;
				y = H;
			}
			System.out.println(y*100 + x);	
		}

	}

}
