package academyforjava;

class UpperClass{
	int x;
	int y;
	
	public UpperClass() {
		x = 10;
		y = 20;
	}
	
	public UpperClass(int x, int y) {
		this(x);
		this.y = y;
	}
	
	public UpperClass(int x) {
		this();
		this.x = x;
	}
}

class LowerClass extends UpperClass{
	
	int r ;
	public LowerClass() {
		super();
		r = 30;
	}
	public LowerClass(int x) {
		super(x);
		r = 30;
	}
	public LowerClass(int x, int y) {
		super(x, y);
		r = 30;
	}
	public LowerClass(int x, int y, int r) {
		this(x,y);
		r = 30;
	}
}

class A2 {
	protected void disp() {
		System.out.println("A2클래스");
	}
}

class B2 extends A2 {
	
	protected void disp() {
		System.out.println("B2클래스");
	}
}
public class superr {

	public static void main(String[] args) {
		
		LowerClass lc = new LowerClass(2,6);
		System.out.printf("%d, %d, %d" ,lc.x,lc.y,lc.r);
		B2 bp = new B2();
		bp.disp();
	}

}

/*상속받는 클래스가 상속하는 클래스보다 범위(private...)가 넓어야 한다
하위 클래스에 throws가 있으면 상위에도 있어야한다
메소드 앞에 final -> 상속못함
배열은 같은 자료형만 가능
*/