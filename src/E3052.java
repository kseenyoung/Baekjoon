
import java.util.Scanner;

public class E3052 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int arr[] = new int[10];
//		int count[] = new int[10];
//		int temp=0;
		int result = 0;
		
		for(int i =0; i < 10; i++) {
			arr[i] = sc.nextInt()%42;
		}
		
		for(int i = 0; i < 10; i++) {
			int count = 0;
			for(int j = i+1; j < 10; j++) {
				if(arr[i] == arr[j]) {
					count++;
				}
			}
			if(count == 0) result++;
		}
		
		System.out.println(result);
	}

	
//	public static boolean method(int a, int[] arr) {
//		for(int i=a+1; i < 10; i++)
//			if(arr[a] == arr[i])
//				return true;
//		return false;
//	}
}


