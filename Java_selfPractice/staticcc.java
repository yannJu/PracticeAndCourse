//static 만들어지자마자 메모리로 올라감 , 객체 없이 실행됨 (class작동하자마자 실행됨)
//프로그램 내에서 자주쓰이는걸 static으로 함 남발은 xxx(프로그램 꼬임)
/* class A{
 * 
 * private int x ;
 * private static int y ;
 * 
 * static {
 * 		y = 100;(x = 100; 은 안됌)
 * }
 * public A() {
 * x = 200;
 * } ->초기화
 */
//메소드 ()에 this가 생략되있음 주소값에 집착....., 객체의 주소값
//static 은 자유롭기 때문에 this가 생략 x 주소값에 집착 xx
//inner은 outer 쓸수 있음 (반대는 xx)
//Outer ot = new Outer();
//Outer.Inner oi = ot.new Inner();

package academyforjava;

public class staticcc {

}

//this(주소),static,자바스럽게 짜기....(생성자, 기능별 함수화,exception처리),분리화,return주의
//queue,백준 문제번호 1463번 1로 만들기