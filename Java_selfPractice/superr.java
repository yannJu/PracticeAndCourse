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
		System.out.println("A2Ŭ����");
	}
}

class B2 extends A2 {
	
	protected void disp() {
		System.out.println("B2Ŭ����");
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

/*��ӹ޴� Ŭ������ ����ϴ� Ŭ�������� ����(private...)�� �о�� �Ѵ�
���� Ŭ������ throws�� ������ �������� �־���Ѵ�
�޼ҵ� �տ� final -> ��Ӹ���
�迭�� ���� �ڷ����� ����
*/