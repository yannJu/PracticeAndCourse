package academyforjava;

class Inherit{
	public String toString() {
		return "Hi Hello World!";
	}
}
public class extendd {
	
	public static void main(String [] args) {
		Inherit in = new Inherit();
		
		System.out.println(in.equals(in));
		System.out.println(in.getClass());
		System.out.println(in.toString());
	}
	
}
