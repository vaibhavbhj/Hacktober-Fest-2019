import java.util.*;
class Month
{
 public static void main(String args[])
 {
  System.out.println("enter no from 1-12 to get it's corresponding month");
  Scanner s=new Scanner(System.in);
  int a=s.nextInt();
  String month[]={"JAN","FEB","MAR","APRL","MAY","JUN","JUL","AUG","SEPT","OCT","NOV","DEC"};
  if(a>=1 && a<=12)
  {
   System.out.println(month[a-1]);
  }
  else
  {
   System.out.println("input a number between 1-12");
  }
 }
}
