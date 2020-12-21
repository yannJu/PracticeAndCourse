//필드, 콘스트럭

package academyforjava;

import java.io.*;

class AvgProgram{
	
	int[] sub = new int[4];
	float avg;
	
	void calc() throws IOException{
		int tot = 0;
		for (int i = 0; i < sub.length; i++) {
			BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
			Integer temp = Integer.parseInt(in.readLine());
			sub [i] = temp;
			tot += sub[i];
		}
 
		System.out.println(avg);
	}
}
public class 클래스 {
	
	public static void main(String [] ar) throws IOException {
		AvgProgram a = new AvgProgram();
		a.calc();
	}

}
