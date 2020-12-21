package academyforjava;

import java.io.*;

class Stack{
	static void makespace() throws IOException {
		BufferedReader stacklength = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("How Long>>");
		Integer sl = Integer.parseInt(stacklength.readLine());
		int [] s = new int[sl];
		int count = 0;
		BufferedReader corq = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("1.Start 2.End");
		Integer cq = Integer.parseInt(corq.readLine());
		while (cq == 1) {
			BufferedReader porp = new BufferedReader(new InputStreamReader(System.in));
			System.out.println("1.Push 2.Pop 3.Quick>>");
			Integer pp = Integer.parseInt(porp.readLine());
			if (pp == 1) {
				if (count < sl) {
					BufferedReader pushnum = new BufferedReader(new InputStreamReader(System.in));
					System.out.println("Input Num >>");
					Integer pn = Integer.parseInt(pushnum.readLine());
					s[count] = pn;
					count += 1;
				}
				else {
					System.out.println("OverFlow");
				}
			}//push일 경우
			else if (pp == 2){
				if (count == 0 ) {
					System.out.println("UnderFlow");
				}
				else {
					count -= 1;
				}
			}//pop일 경우
			else if (pp == 3){
				cq = 2;
			}//quick일 경우
			else {
				System.out.println("Only Select 1,2,3>>");
				Stack.makespace();
			}
		}//클래스 종료조건(반복)
		for (int i = 0; i < count; i ++) {
			System.out.println(s[i]);
		}
	} //스텍메소드
}
public class StackArrayy {
	
	public static void main(String[] args) throws IOException {
		Stack sa = new Stack();
		sa.makespace();
	}
}
