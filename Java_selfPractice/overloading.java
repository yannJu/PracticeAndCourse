package academyforjava;

import java.io.*;

class OverLoad {
	
	int a;
	
	public OverLoad(){
		System.out.println(a);
	}
	public OverLoad(int a) {
		System.out.println(a*100);
	}
	public OverLoad(int a, int b) {
		b = 5;
		System.out.println(a/b);
	}
}

public class overloading {
	
	public static void main(String []ar){
		OverLoad a = new OverLoad(2,4);
	}
}
