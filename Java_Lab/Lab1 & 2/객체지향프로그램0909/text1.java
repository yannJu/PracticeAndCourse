package 객체지향프로그램0909;
import java.io.*;

public class text1 {
	public static int count = 0;
	public static void main(String[] args) throws IOException {
		BufferedReader number = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Input Number>>");
		Integer nb = Integer.parseInt(number.readLine());
		oneMake(nb);
		System.out.println(count);
	}
	
	public static int oneMake(int temp){
		if (temp == 1) {
			return count;
		}//1일때
		else if (temp%2 == 0) {
			count++;
			if (temp%3 == 0) {
				return oneMake(temp/3);
			}
			else if (temp%2 == 0) {
				if ((temp/2)%2 == 0) {
					return oneMake(temp/2);
				}
				else {
					return oneMake(temp-1);
				}
			}
		}//짝수일때
		else {
			count++;
			if((temp != 1)) {
				if (temp%3 == 0) {
					return oneMake(temp/3);
				}
				else {
					return oneMake(temp-1);
				}
			}//홀수일때
		}
		return count;
	}

}
