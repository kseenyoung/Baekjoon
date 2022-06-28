
import java.util.Scanner;

public class E2525 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int nowH = sc.nextInt();
		int nowM = sc.nextInt();
		int plusM = sc.nextInt();
		
		nowM += plusM;
		if( nowM > 60 && nowM % 60 != 0 ) {
			nowH += nowM/60; //1시간 단위 분 올림
			nowM %= 60; //*******
		}
		else if(nowM % 60 == 0) { //*****
			nowH += nowM/60; //1시간 단위 분 올림
			nowM = 0;
		}
		
		if(nowH > 23) { //오후 12시 이후
			nowH %= 24;
		}
		
		System.out.println(nowH + " " + nowM);
		
	}

}
