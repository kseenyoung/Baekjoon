import java.util.*;

public class C1475 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] cards = new int[10];
		int answer=0;
		
		int n = sc.nextInt();
		while(n>0) {
			cards[n%10]+=1;
			n/=10;
		}
		cards[6] = (int) Math.ceil((cards[9] + cards[6])/2.0);
		cards[9] = 0;
		
		for(int c:cards) {
			if(answer<c)
				answer = c;
		}
		
//		System.out.println(Arrays.toString(cards));
		System.out.println(answer);
	}

}
