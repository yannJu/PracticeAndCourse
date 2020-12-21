package academyforjava;
import java.io.*;

public class fibo {
	
	public static void main(String []ar) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		Integer temp = Integer.parseInt(in.readLine());
		System.out.println(fibo(temp));
	}
	
	public static int fibo(int temp) {
		if (temp == 0) {
			return 0;
		}
		else if (temp == 1) {
			return 1;
		}
		else {
			return fibo(temp-1) + fibo(temp-2);
		}
	}

}
