//�� ����(������ ������ ã������/�� �ּҰ��� ����) ������Ʈ(���)
//���� ����

package academyforjava;

class other{
	private int x = 10;
}


public class garbage {
	private int x = 10;
	public static void main(String[] args) {
		other a = new other();
		other b = a;
		System.out.println(a.x);//�������� ���� : , ���� : �迭�� ���ø���� , queue����(class)ȭ ��Ű��
	}
}
