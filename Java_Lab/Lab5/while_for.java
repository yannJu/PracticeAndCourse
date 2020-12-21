import java.util.Scanner;

public class while_for {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		System.out.print("Please enter a number, 0 to quit: ");
		int n = in.nextInt();
		int i = 1;
		for (i = 1; Math.pow(2, i) <= n* n; i++) {
		}
		System.out.println("2 raise to " + i + " is the first power of two greater than " + n + " squared");
		/*
		int i = 1;
		while (n * n > Math.pow(2, i)) {
			i++;
		}
		System.out.println("2 raised to " + i + " is the first power of two greater than " + n + " squared");
*/
	}

}
