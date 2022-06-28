
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class E2941_R {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String word = br.readLine();
		int count=0;
    
		 for(int i=0; i < word.length(); i++) {
			 
			 if(word.charAt(i) == 'c' && i+1 < word.length()) {
				 if(word.charAt(i+1) == '=')
					 i++;
				 else if(word.charAt(i+1) == '-')
					 i++;
		 	}
		 	else if(word.charAt(i) == 'd'&& i+1 < word.length()) {
		 		if(word.charAt(i+1) == 'z' && i+2 < word.length()) {
		 			if(word.charAt(i+2) == '=')
		 				i += 2;
		 		}
		 		else if(word.charAt(i+1) == '-') //***
		 			i++;
		 	}
		 	else if(word.charAt(i) == 'l'&& i+1 < word.length()) {
		 		if(word.charAt(i+1) == 'j')
		 			i++;
		 	}
		 	else if(word.charAt(i) == 'n'&& i+1 < word.length()) {
		 		if(word.charAt(i+1) == 'j')
		 			i++;
		 	}
		 	else if(word.charAt(i) == 's'&& i+1 < word.length()) {
		 		if(word.charAt(i+1) == '=')
		 			i++;
		 	}
		 	else if(word.charAt(i) == 'z'&& i+1 < word.length()) {
		 		if(word.charAt(i+1) == '=')
		 			i++;
		 	}
		 	
		 	count++;
		    
			}
		 System.out.println(count);
	}
}
