import java.util.*;

public class BasicIO {

	public static void main(String[] args) {
		Scanner stdin = new Scanner(System.in);
		System.out.print("Enter your name:");
		String name = stdin.nextLine();		
		System.out.println("your name is " + name);

		System.out.print("Enter your age:");
		int years = stdin.nextInt();
		//Integer years = Integer.parseInt(agesys.nextLine());
		System.out.println("your age is " + years);
		System.out.println(years * 365);
		
		System.out.print("Enter your height:");
		Double height = stdin.nextDouble();
		System.out.println("your height is " + height);
		
		Date today = new Date();
		System.out.printf("오늘 날짜는 %ty년 %tm월 %td일 입니다." ,today,today,today);
		System.out.printf("Name : %s , Age : %d , Height : %f " , name,years,height);
	}

}
