package academyforjava;
import java.io.*;
	
class Make{
	int maxMake (String a , String b) { 
		int ai = Integer.parseInt(a.replace("5", "6"));
		int bi = Integer.parseInt(b.replace("5", "6"));
		return ai + bi;
	}
	int minMake (String a, String b) {
		int aj = Integer.parseInt(a.replace("6", "5"));
		int bj = Integer.parseInt(b.replace("6","5"));
		return aj + bj;
		
	}
}
public class fiveorsix {

	public static void main(String[] args) throws IOException{
		BufferedReader numnum = new BufferedReader(new InputStreamReader(System.in));
		System.out.println("�� ���� �Է��Ͽ� �ּ���.(�� �� ��� 1�̻� 1,000,000������ �����Դϴ�.)");
		String num1 = numnum.readLine();
		String num2 = numnum.readLine();
		Make make = new Make();
		System.out.printf("%d %d" ,make.minMake(num1, num2), make.maxMake(num1, num2));
	}

}
