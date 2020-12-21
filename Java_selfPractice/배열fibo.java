package academyforjava;

import java.io.*;

public class 배열fibo {
	
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
//다이나믹 알고리즘 -> 재귀함수보다 속도 빠름(기억 알고리즘)-> 아래에서 위로 