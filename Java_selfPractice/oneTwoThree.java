package academyforjava;
import java.io.*;

class oneMake {
	private int count;
	void oneMake() {
		count = 0;
	}//count
	void numOne(int innum) {
		if (innum == 1) {
			System.out.println(count);
		}
		if (innum % 3 == 0) {
			count ++;
			numOne(innum/3);
		}//3���� ������ ������ ��
		if (innum % 2 == 0) {
			count ++;
			numOne(innum/2);
		}//2�� ������ ������ ��
		count++;
		numOne(innum-1);
	}
	
}
public class oneTwoThree {

	public static void main(String[] args) throws IOException{
		BufferedReader number = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("Input Number>>");
		Integer nb = Integer.parseInt(number.readLine());
		oneMake om = new oneMake();
		om.numOne(nb);
	}

}
