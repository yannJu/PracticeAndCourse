public class substring {

	public static void main(String[] args) {
		
		String inputString = "The quick brown fox jumps over the lazy dog";
		//outstring = Tempus fugit
		String T = inputString.substring(0,1);
		String e = inputString.substring(2,3);
		String mp = inputString.substring(22,24);
		String u = inputString.substring(5,6);
		String s = inputString.substring(24,25);
		String space = inputString.substring(3,4);
		String f = inputString.substring(16,17);
		String g = inputString.substring(4,5);
		String i = inputString.substring(6,7);
		String t = inputString.substring(31,32);	
		String outString = T.concat(e).concat(m).concat(u).concat(s).concat(space).concat(f).concat(u).concat(g).concat(i).concat(t);
		System.out.println(outString);
				

	}

}