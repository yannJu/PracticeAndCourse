package 객체지향프로그램0909;

class A {
	static int s = 1;
	public int x = 3;
	{ x = 5; }
	public A() { x = 6; }
	static { s = 2; }
public class InitDemo extends A {
	static int s2 = 9;
	public int y =2;
	public static void main(String[] args) {
	InitDemo b = new InitDemo();
	System.out.println(b.x);
	}
	{ x = 7; }
}
//
//x = 6을 프린트하고 x = 7이 되는것????
// 업캐스팅, instanceof, 동적바인딩