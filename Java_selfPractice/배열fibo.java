package academyforjava;

import java.io.*;

public class �迭fibo {
	
	public static void main(String[] ar) throws IOException{
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		Integer temp = Integer.parseInt(in.readLine());

	
		int[] a = new int [temp+1];
		a[0] = 0;
		a[1] = 1;
		for (int i = 2; i < temp+1; i ++) {
			
			a[i] = a[i-1] + a[i-2];
			
		}
		System.out.println(a[temp]);
	}

}
//���̳��� �˰��� -> ����Լ����� �ӵ� ����(��� �˰���)-> �Ʒ����� ���� 