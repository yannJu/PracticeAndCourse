package academyforjava;

class Aa{
    int x = 100;
	private int y = 200;
}
class Bb extends Aa{
	private int r = 300;
}

public class privateextend {

	public static void main(String[] args) {
		Bb bp = new Bb();
		System.out.println(bp.x);
	}

}

/* private => 오직 자신의 클래스에서만 가능
protected => 같은 파일, 같은 패키지, 상속받은 곳
public => 그냥 모든곳~~~~
*/