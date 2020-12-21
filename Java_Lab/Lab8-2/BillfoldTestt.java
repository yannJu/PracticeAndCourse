public class BillfoldTestt {
	public static void main(String[] args) {
		ID_Card id = new ID_Card("이연주", "2019.05.19", 20191644, "인천");
		DriverLisence driver = new DriverLisence("이연주", "2019.05.19", 20191644, "인천", 3);
		Billfold bill = new Billfold();
		bill.card1 = id;
		bill.card2 = driver;
		System.out.println(bill.formatCards());
		System.out.println(bill.getExpiredCardCount());
	}
}
