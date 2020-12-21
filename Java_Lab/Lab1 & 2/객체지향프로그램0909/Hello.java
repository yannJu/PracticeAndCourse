package 객체지향프로그램0909;
import java.util.Arrays;
import java.util.Scanner;
class Hello{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        String strB = "" + B;
        int tmp = 1000;
        int result = 0;
        String ch = "";
        int[] ary = new int [3];
        for(int i = 0; i < strB.length(); i++){
        	ch += strB.charAt(i);
            tmp /= 10;
            ary[2-i] = A * Integer.parseInt(ch) * tmp;
            ch = "";
        }
        for(int a : ary){
        	System.out.println(a / tmp);
        	tmp *= 10;
            result += a;
        }
        System.out.println(result);
    }
}