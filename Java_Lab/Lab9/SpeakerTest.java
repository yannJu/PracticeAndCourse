class SpeakerTest {
   public static void main(String[] argc) 
   {
      Speaker guest = new Philosopher("thinking");
      guest.speak(); // Philospher's speak()
      guest = new Dog();
      guest.speak(); // Dog's speak()
   }
}