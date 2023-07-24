import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class C10811 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		StringTokenizer st = new StringTokenizer(s);

		int n= Integer.parseInt(st.nextToken());
		int m= Integer.parseInt(st.nextToken());
		int[] bucket = new int[n];
		for(int i=1; i<=n; i++)
			bucket[i-1] = i;

		for(int k=0; k<m; k++) {
			s = br.readLine();
			st = new StringTokenizer(s);
			int i = Integer.parseInt(st.nextToken());
			int j = Integer.parseInt(st.nextToken());
			swap(bucket, i, j);
		}

		for(int i:bucket)
			System.out.print(i+" ");

	}

	public static void swap(int[] arr, int i, int j) {
		for(int k=0; k<=Math.round((j-i)/2); k++) {
			int temp = arr[i+k-1];
			arr[i+k-1] = arr[j-k-1];
			arr[j-k-1] = temp;
		}
	}

}
