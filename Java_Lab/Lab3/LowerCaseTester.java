public class LowerCaseTester {

	public static void main(String[] args) {

		String greeting = "Hello, World!"; int n = greeting.length();
		System.out.println(n);
		
		String river = "Mississippi"; String bigRiver = river.toUpperCase();
		System.out.println(bigRiver);
		
		String testString = "This is a Test"; String smallTestString = testString.toLowerCase();
		System.out.println(smallTestString);
		
		String bigTestString = smallTestString.toUpperCase();
		System.out.println(bigTestString);
		
	}

}
