package academyforjava;

public class threesixnine {

	public static void main(String[] args) {
		for (int x = 1; x<=100; x++) {
			if (( x / 10 == 3) || ( x / 10 == 6) || ( x/ 10 == 9)){
				if (x%10 == 0) {
					System.out.println("*0");
				}
				else if ((x%10 ==3) || (x%10 ==6) || (x%10 ==9)){
					System.out.println("**");
				}
				else {
					System.out.println("*" + (x%10));
				}
			} //30,60,90�� �϶�		
			else if ((x%10 == 3) || (x%10 ==6) || (x%10 == 9)){
				if (x<10){
					System.out.println("*");
				}
				else {
					System.out.println((x/10) + "*");
				}
			}//3,6,9�� �ִ� �κ� * ó��
			else {
				System.out.println(x);
			}
		}//for��
	}
}