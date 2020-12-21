import java.util.Calendar;
import java.util.GregorianCalendar;
class Card 
{
    protected String name;
    private String date;

    public Card() {
        name = "";
        date = "";
    }

    public Card(String n, String d) {
        name = n;
        date = d;
    }

    public String getName() {
        return name; 
    }

    public String getDate() {
    	return date;
    }
    public boolean isExpired() {
        return false;
    }

    public String format() {
        return "Card holder: " + name + "\n" + "Card date: " + date;
    }
}

class ID_Card extends Card
{
	private int number_ID;
	private String address_ID;
	
	
	public ID_Card() {
		number_ID = 0;
		address_ID = "";
	}
	public ID_Card(String name, String date, int number, String address) {
		super(name, date);
		number_ID = number;
		address_ID = address;	
	}
	public String toString() {
		String answer = ("ID_Card[name= " + name + "date= " + date + "number_ID= " + number_ID + "address_ID= " + address_ID);
		return answer;
	}
	public int getnumber_ID() {
		return number_ID;
	}
	public String format() {
		String answer = super.format();
		answer += ("\nNumberID: " + number_ID + "\n" + "AddressID: " + address_ID);
      return answer;
    }
	public boolean isExpired() {
        return false;
    }
}

class DriverLisence extends ID_Card
{
	private int Expiration_year;
	
	public DriverLisence() {
		Expiration_year = 0;
	}
	public DriverLisence(String name, String date, int number, String address, int a) {
		super(name, date, number, address);
		Expiration_year = a;
	}
	public int getDriverLisence() {
		return Expiration_year;
	}
	public String format() {
		String answer = super.format();
		answer += ("\nExpirationYear: " + Expiration_year);
		return answer;
	}
	public boolean isExpired() {
		GregorianCalendar calendar = new GregorianCalendar();
		if (calendar.get(Calendar.YEAR) > Expiration_year) {
			return true;
		}
		else {
			return false;
    }
}

class CallingCard extends Card
{
	private int car_Number;
	private int pin_Number;
	
	public CallingCard() {
		car_Number = 0;
		pin_Number = 0;
	}
	public CallingCard(String name, String date, int c, int d) {
		super(name, date);
		car_Number = c;
		pin_Number = d;
	}
	public int getCarNumber() {
		return car_Number;
	}
	public int getPinNumber() {
		return pin_Number;
	}
	public String format() {
		String answer = super.format();
		answer += ("\nCarNumber: " + car_Number + "\n" + pin_Number);
      return answer;
    }
	public boolean isExpired() {
        return false;
    }
}
}
