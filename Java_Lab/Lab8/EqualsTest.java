// **********************************************************
// EqualsTest.java
// **********************************************************

import java.util.*;

public class EqualsTest
{  
   public static void main(String[] args)
   {  
      Employee alice1 = new Employee("Alice Adams", 75000, 1987, 12, 15);
      Employee alice2 = alice1;
      Employee alice3 = new Employee("Alice Adams", 75000, 1987, 12, 15);
      Employee bob = new Employee("Bob Brandson", 50000, 1989, 10, 1);
      
      //HW1
      System.out.println("alice1 == alice2: " + (alice1 == alice2));
	   System.out.println("alice1 == alice3: " + (alice1 == alice3));
	   System.out.println("alice1.equals(alice3): " + alice1.equals(alice3));
	   System.out.println("alice1.equals(bob): " + alice1.equals(bob));
	   //HW2
	   System.out.println("bob.toString(): " + bob);
	   
	   Manager car1 = new Manager("Car1 Cracker", 80000, 1987, 12, 15);
	   Manager boss = new Manager("Car1 Cracker", 80000, 1987, 12, 15);
	   boss.setBonus(5000);
	   System.out.println("boss.toString(): " + boss);
	   //HW3
	   System.out.println("car1.equals(boss): " + car1.equals(boss));
   }
}

class Employee
{
   private String name;
   private double salary;
   private Date hireDay;
   private int year=11, month=7, day=13;

   public Employee(String n, double s, int year, int month, int day)
   {  
      name = n;
      salary = s;
      GregorianCalendar calendar = new GregorianCalendar(year, month - 1, day);
      hireDay = calendar.getTime();
   }

   public String getName()
   {  
      return name;
   }

   public double getSalary()
   {  
      return salary;
   }

   public Date getHireDay()
   {  
      return hireDay;
   }

   public void raiseSalary(double byPercent)
   {  
      double raise = salary * byPercent / 100;
      salary += raise;
   }

   public boolean equals(Object otherObject)
   {  
      // a quick test to see if the objects are identical
      if (this == otherObject) return true;

      // must return false if the explicit parameter is null
      if (otherObject == null) return false;

      // if the classes don't match, they can't be equal
      if (!(otherObject instanceof Employee) || (otherObject instanceof Manager))
         return false;

      // now we know otherObject is a non-null Employee
      Employee other = (Employee) otherObject;

      // test whether the fields have identical values
      return name.equals(other.name)
         && salary == other.salary
         && hireDay.equals(other.hireDay);
   }

   public String toString()
   {  
      return "Employee"
         + "[name=" + name
         + ",salary=" + salary
         + ",hireDay=" + hireDay
         + "]";
   }
}

class Manager extends Employee
{  
   private double bonus;

   public Manager(String n, double s, int year, int month, int day)
   {  
      super(n, s, year, month, day);
      bonus = 0;
   }

   public double getSalary()
   { 
      double baseSalary = super.getSalary();
      return baseSalary + bonus;
   }

   public void setBonus(double b)
   {  
      bonus = b;
   }

   public boolean equals(Object otherObject)
   {
      if (!(otherObject instanceof Manager)) return false;
      Manager other = (Manager) otherObject; 
      return bonus == other.bonus;
   }

   public String toString()
   {
      return "Manager"
         + "[name=" + getName()
         + ",salary=" + getSalary()
         + ",hireDay=" + getHireDay()
         + ",bonus=" + bonus
         + "]";
   }
}