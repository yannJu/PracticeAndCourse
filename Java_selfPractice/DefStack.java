package academyforjava;
import java.awt.Window.Type;
import java.io.*;
import java.util.Scanner;

class Test{
	private int count ;
	private int [] s;
	private int sl;
	public Test(){
		count = -1;
		
	}//count만듬
	void makespace() throws IOException {
		BufferedReader stacklength = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("How Long>>");
		sl = Integer.parseInt(stacklength.readLine());
		s = new int[sl];
	}//배열만듬
	void push(int a) throws IOException {
		if(checkOverflow()) {
			s[++count] = a;
		}
		else {
			System.out.println("OverFlow");
		}
	}//push일 경우
	int pop() {
		if(checkUnderflow()) {
			return s[count--];
		}
		else {
			return -1000;
		}
	}//pop일 경우
	
	boolean checkOverflow() {
		if (count < sl - 1) {
			return true;
		}
		else {
			return false;
		}
	}//overflow
	boolean checkUnderflow() {
		if (count < 0) {
			return false;
		}
		else {
			return true;
		}
	}//underflow
	void quick() {
		for (int i = 0; i <= count; i++) {
			System.out.print(s[i]);
		}
	}
}
public class DefStack {
	public static void main(String[] args) throws IOException {
		Test sa = new Test();
		sa.makespace();
		BufferedReader corq = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("1.Start 2.End");
		Integer cq = Integer.parseInt(corq.readLine());
		while (cq == 1) {
			Scanner porp = new Scanner(System.in);
			System.out.println("Select Push or Pop or Quick>>");
			String pp;
			pp = porp.nextLine();
			if (pp.equals("Push")) {
				BufferedReader pushnum = new BufferedReader(new InputStreamReader(System.in));
				System.out.println("Input Number>>");
				Integer pn = Integer.parseInt(pushnum.readLine());
				sa.push(pn);
			}//pop일때
			else if (pp.equals("Pop")) {
				int value = sa.pop();
				if(value == -1000) {
					System.out.println("Under Flow");
				}else {
					System.out.println("Output value is " + value);
				}
			}//push일때
			else if(pp.equals("Quick")) {
				sa.quick();
				cq = 2;
			}
			else {
				System.out.println("Please Input Again");
			}
		}//Start눌렀을때
	}
}
