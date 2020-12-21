class Philosopher extends Speaker
{
   private String philosophy;

   public Philosopher(String philosophy) {
      this.philosophy = philosophy;
   }
   
   public void speak() {
      System.out.println(philosophy);
   }

   public void announce(String announcement) {
      System.out.println(announcement);
   }

   public void pontificate() {
      for (int count=1; count <= 5; count++)
         System.out.println(philosophy);
   }
}