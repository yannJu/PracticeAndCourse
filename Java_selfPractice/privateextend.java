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

/* private => ���� �ڽ��� Ŭ���������� ����
protected => ���� ����, ���� ��Ű��, ��ӹ��� ��
public => �׳� ����~~~~
*/