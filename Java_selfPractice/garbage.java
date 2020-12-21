//힙 스텍(힙으로 데이터 찾으러감/힙 주소값이 있음) 컨스턴트(상수)
//힙을 정리

package academyforjava;

class other{
	private int x = 10;
}


public class garbage {
	private int x = 10;
	public static void main(String[] args) {
		other a = new other();
		other b = a;
		System.out.println(a.x);//에러나는 이유 : , 숙제 : 배열로 스택만들기 , queue구현(class)화 시키기
	}
}
