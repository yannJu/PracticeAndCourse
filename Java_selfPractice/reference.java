package academyforjava;

class A5{
	int x = 100;
}

public class reference {

	public static void main(String[] args) {
		
		A5 kkk = new A5();
		A5 k2 = kkk;
		
		k2.x = 1000;
		
		System.out.println(kkk.x);
		
	}

}
