package 객체지향프로그램0909;

import java.util.*;

public class Hw2_scoreSet {
	private int[] scores;
	private int ix = 0; //next position to add a score
	double result = 0;
	int min;
	int secondMin;
	public Hw2_scoreSet() {
		scores = new int[10];
	}
	public void add(int score) {
		if (ix >= scores.length) {
			int[] ary = new int[scores.length + 5];
			System.arraycopy(scores, 0, ary, 0, scores.length - 1);
			scores = ary;
		}
		scores[ix++] = score;
	}
	public double averageWithoutLowest2() {
		min = scores[0];
		for(int i = 0; i < ix; i++) {
			if(scores[i] <= min) {
				secondMin = min;
				min = scores[i];
			}
		}
		for (int i = 0; i < scores.length-1; i++) {
			result += scores[i];
		}
		result = result - min - secondMin;
		ix -= 2;
		return (result/ix);
		
		
	}
	public String toString() {
		String chaTer = "";
		for(int a:scores) {
			if (a == 0) {
				break;
			}
			chaTer = chaTer + " " + a;
		}
		chaTer = "["+chaTer.trim()+"]";
		return chaTer;
	}
	public static void main(String[] args) {
		Hw2_scoreSet hw = new Hw2_scoreSet();
		int tt = 0;
		while (tt == 0){
			Scanner s = new Scanner(System.in);
			System.out.println("점수를 입력하세요.");
			int sc = s.nextInt();
			if (sc == -1) {
				tt = -1;
				break;
			}
			hw.add(sc);
		}
		double a = hw.averageWithoutLowest2();
		System.out.println(a);
		String b = hw.toString();
		System.out.println(b);
		
	}

}
