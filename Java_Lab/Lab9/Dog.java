class Dog extends Speaker {

   // Prints this dog's philosophy.
   public void speak() {
      System.out.println("woof");
   }

   // Prints this dog's philosophy and the specified
   // announcement.
   public void announce(String announcement) {
      System.out.println("woof: " + announcement);
   }
}