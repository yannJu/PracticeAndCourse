package academyforjava;

class ThisS{
	int a = 10;
	int b = 20;
	int c = 30;
	int d = 5;
	int e = 100;
	
	public ThisS() {
		System.out.println(a);
		System.out.println(b);
		System.out.println(c);
		System.out.println(d);
		System.out.println(e);
	}
	public ThisS(int a) {
		this();
		e = a;
		System.out.println(e);
	}
	public ThisS(int a , int b) {
		this(a);
		d = a;
		c = b;
		System.out.println(d);
		System.out.println(c);
	}
}
public class thisss {

	public static void main(String[] args) {
		ThisS T = new ThisS(5,3);
	}

}
