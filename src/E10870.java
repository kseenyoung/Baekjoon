import java.io.*;
public class E10870 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.println(fibonacci(Integer.parseInt(br.readLine())));
		
	}

	public static int fibonacci(int n) {
		if(n < 2) {
			return n;
		}
		else {
			return fibonacci(n-1) + fibonacci(n-2);
		}
	}
}
