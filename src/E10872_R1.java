import java.io.*;
public class E10872_R1 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		System.out.println(get_fectorial(n));

	}

	public static int get_fectorial(int n) {
		if(n < 2)
			return 1;
		else {
			return get_fectorial(n-1)*n;
			
		}
		
	}
}
