package academyforjava;
//��ȿ�� �� �ڵ�(�̷����� �غ��ϱ� ���� ����� ��)
public class extent {
	
	Dd dp = new Dd();
	
	extent(){
		this.dp = dp;
	}
	
	class Aa{
		int a = 100;
	}
	
	class Bb{
		Aa ap = new Aa();
		int b = 200;
	}
	
	class Cc{
		Bb bp = new Bb();
		int c = 300;
	}

	class Dd{
		Cc cp = new Cc();
		int d;
	}
	public static void main(String[] args) {
		
		extent temp = new extent();
		System.out.println(temp.dp.cp.bp.ap.a);

	}

}
