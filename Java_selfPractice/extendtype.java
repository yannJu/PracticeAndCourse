package academyforjava;

class A4{
	int x = 100;
}
class B4 extends A4{
	int y = 200;
}
class B5 extends A4{
	int x = 300;
}
public class extendtype {

	public static void main(String[] args) {
		B4 ap = new B4();
		B5 bp = new B5();
		System.out.println("x = " + ap.x); // ���� 15��° ���� A4 ap = new B4(); ������ 16��° ���� ������ ����.
		System.out.println("y = " + ap.y);
		System.out.println("x = " + bp.x);
	}

}
