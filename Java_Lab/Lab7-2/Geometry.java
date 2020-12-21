import java.util.*;

public class Geometry {
	public static double getCircleCirumference(double r) {
		return Math.PI*(r*2);
	}
	public static double getCircleArea(double r) {
		return Math.pow(r,2)*Math.PI;
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("반지름 값을 입력해주세요:");
		double r = sc.nextInt();
		double cirum = getCircleCirumference(r);
		double area = getCircleArea(cirum);
		System.out.println(cirum);
		System.out.println(area);
	}

}