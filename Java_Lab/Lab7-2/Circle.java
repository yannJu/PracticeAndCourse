import java.util.*;

public class Circle {
	double r;
	public Circle(double r) {
		this.r = r;
	}
	public double getCircleCirumference(double r) {
		return Math.PI*(r*2);
	}
	public double getCircleArea(double r) {
		return Math.pow(r,2)*Math.PI;
	}
	public int compareRadius(double radius) {
		final double EPSILON = 1E-12;
		double diff = r - radius;
		if (Math.abs(diff) < EPSILON) return 0;
		if (diff < 0) return -1;
		if (diff > 0) return 1;
		return 0;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("반지름 값을 입력해주세요:");
		double r = sc.nextInt();
		Circle ci = new Circle(r);
		double cirum = ci.getCircleCirumference(r);
		double area = ci.getCircleArea(cirum);
		int compare = ci.compareRadius(5);
		
		System.out.println(cirum);
		System.out.println(area);
		System.out.println(compare);
	}

}