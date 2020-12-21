package 객체지향프로그램0909;
import java.util.*;

public class Hw1_randomNumber {
	
	public static void main(String [] args){
		Scanner s = new Scanner(System.in);
		System.out.println("몇개의 난수를 생성할 것인가?");
		int how = s.nextInt();
		System.out.println("원하는 난수 값은 0부터 시작해서 모두 몇 개인가?");
		int zStart = s.nextInt();
		
		int [] randomArray = new int[zStart];
		for (int i = 0; i < zStart; i++) {
			randomArray[i] = 0;
		}
		for (int i = 0; i < how; i ++) {
			Random r = new Random();
			int rNum = r.nextInt(zStart);
			randomArray[rNum] = randomArray[rNum] + 1;
		}
		for (int i = 0; i < zStart; i++) {
			System.out.print(i + " ");
			System.out.println(randomArray[i]);
		}
	}

}