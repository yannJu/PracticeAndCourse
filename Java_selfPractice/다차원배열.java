package academyforjava;

public class 다차원배열 {
	
	public static void main (String [] ar) {
		int [] [] b;
		int [] [] c;
		int [] [] a = {{1,2},{3,4}};
		float[] avg = new float[3];//3가지가 들어가야함
		b = new int [] [] {{1,2},{3,4}};
		c = new int [3] [2]; //3개의 리스트를 만드는데 2개씩 들어가게
		
		System.out.println(b[0][1]);
		System.out.println(c[0][0]);
		System.out.println(c[0].length);
	}

}
