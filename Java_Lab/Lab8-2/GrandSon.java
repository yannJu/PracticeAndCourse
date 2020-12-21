class  Parent {
	protected int age = 60;
	protected String msg = "I am a Parent.";

	public void printID() {
		System.out.println(msg);
	}

	public void showMessage() {
		System.out.println("Parent message: I am " + age + "years old.");
	}
}

class  Son extends  Parent {
	protected int age = 35;
	protected String msg = "I am a Son.";
	
	public void printID() {
		System.out.println(msg);
	}
}

class  GrandSon extends  Son {
	protected int age = 5;
	protected String msg = "I am a GrandSon.";
	
	public void printID() {
		System.out.println(msg);
	}

	public void showMessage() {
		System.out.println("Grand son message: I am " + age + "years old.");
	}
	
	public void doGrandSon() {
		System.out.println("do something in GrandSon.");
	}

	public void examineObjects(int age) {
		GrandSon grandSon = new GrandSon();
		Son son = grandSon;
		Parent parent = grandSon;
		
		//hw2
		grandSon.printID();
		son.printID();
		super.printID();
		
		showMessage();
		super.showMessage();
		
		//hw3
		//son.doGrandSon();
		
		//hw4
		//super.super.printID();
		
		//hw5
		System.out.println("\nage = " + age);
		System.out.println("this.age = " + this.age);
		System.out.println("super.age = " + super.age);
		
		System.out.println("son.age = " + (son.age));
		System.out.println("parent.age = " + parent.age);
		
		System.out.println("((Son) this).age = " + ((Son) this).age);
		System.out.println("((Parent) this).age = " + ((Parent) this).age);
		
		//hw6
		//super.super.age = 70;
	}

	public static void main(String args[]) {
		GrandSon grandSon = new GrandSon();
		grandSon.examineObjects(15);
	}
}