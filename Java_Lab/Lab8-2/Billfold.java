class Billfold {
	Card card1, card2;
	
	public void addCard(Card c) {
		if (card1 == null) {
			this.card1 = c;
		}
		else if (card2 == null){
			this.card2 = c;
		}
	}
	public String formatCards() {
		String answer = "";
		answer += ("card1- \n" + card1.format() + "\n" + "card2- \n" + card2.format());
		return answer;
	}
	public int getExpiredCardCount() {
		int answer = 0;
		if (card1.isExpired()) {
			answer += 1;
		}
		if (card2.isExpired()) {
			answer += 1;
		}
		return answer;
	}
}
